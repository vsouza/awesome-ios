#!/usr/bin/env python3
"""Check added GitHub repo entries in a PR against Awesome iOS inclusion rules.

Inputs (via env vars):
  BASE_SHA         — base commit SHA (target branch)
  HEAD_SHA         — head commit SHA (PR branch)
  GH_TOKEN         — GitHub token with `repo` read scope
  PR_BODY          — full PR body text (used to detect a hidden-gem justification)

Output:
  Writes a markdown report to `quality-report.md` in the current directory.
  Exits 0 if all added repos pass the hard rules, 1 otherwise.

Only the HARD rules that are programmatically verifiable are checked here:
  1. More than 100 stargazers (or ≥75 with a hidden-gem justification in the PR body).
  2. Commit in the last 24 months (pushed_at).
  3. More than one contributor (excluding bots).
  4. Not archived.
  5. OSI-approved license.

The rest (SPM support, iOS/Swift version floors, paid-product checks, README
quality, category placement) remain a human-review responsibility.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

MIN_STARS = 100
HIDDEN_GEM_MIN_STARS = 75
RECENT_COMMIT_MONTHS = 24

# SPDX identifiers considered OSI-approved and open-source-friendly.
# Source-available (BSL, SSPL, Elastic, Commons Clause) deliberately not here.
ACCEPTED_LICENSES = {
    "mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause", "mpl-2.0", "isc",
    "unlicense", "cc0-1.0", "0bsd", "wtfpl", "zlib", "artistic-2.0",
    "lgpl-2.1", "lgpl-3.0", "gpl-2.0", "gpl-3.0", "agpl-3.0", "epl-2.0",
    "bsd-3-clause-clear", "postgresql", "ncsa",
}

BOT_PATTERNS = re.compile(r"(\[bot\]|dependabot|renovate|github-actions|greenkeeper)", re.IGNORECASE)

URL_RE = re.compile(r"https://github\.com/([\w.-]+)/([\w.-]+?)(?=[/)\s#?]|$)")
ENTRY_RE = re.compile(r"^\+-\s+\[([^\]]+)\]\((https?://[^)]+)\)")


def run(cmd: list[str]) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout


def added_entries(base_sha: str, head_sha: str) -> list[tuple[str, str, str]]:
    """Return (entry_name, owner, repo) for each new list entry added to README.md."""
    diff = run(["git", "diff", "--unified=0", f"{base_sha}..{head_sha}", "--", "README.md"])
    out = []
    for line in diff.splitlines():
        m = ENTRY_RE.match(line)
        if not m:
            continue
        name, url = m.group(1), m.group(2)
        u = URL_RE.search(url)
        if not u:
            continue
        owner, repo = u.group(1), u.group(2).rstrip("/")
        if not owner or not repo or repo in (".", ".."):
            continue
        out.append((name, owner, repo))
    return out


def check_repo(owner: str, repo: str) -> dict:
    """Query GitHub API; return a status dict."""
    try:
        data = json.loads(run(["gh", "api", f"repos/{owner}/{repo}"]))
    except RuntimeError as exc:
        msg = str(exc)
        if "HTTP 404" in msg or "Not Found" in msg:
            return {"ok": False, "reason": "404 not found"}
        if "HTTP 451" in msg:
            return {"ok": False, "reason": "451 (unavailable for legal reasons)"}
        return {"ok": False, "reason": f"api error: {msg[:200]}"}

    # Contributor count — first page, anon included. If we see >1 on page 1, we're done.
    contributors_count = 0
    try:
        contribs = json.loads(run([
            "gh", "api", f"repos/{owner}/{repo}/contributors?per_page=10&anon=1",
        ]))
        for c in contribs:
            login = c.get("login") or c.get("name") or ""
            if BOT_PATTERNS.search(login):
                continue
            contributors_count += 1
    except RuntimeError:
        pass  # tolerate — will show as "unknown" in report

    return {
        "ok": True,
        "archived": bool(data.get("archived")),
        "stars": int(data.get("stargazers_count") or 0),
        "pushed_at": data.get("pushed_at"),
        "license": ((data.get("license") or {}).get("spdx_id") or "").lower(),
        "html_url": data.get("html_url"),
        "contributors": contributors_count,
    }


def evaluate(status: dict, allow_hidden_gem: bool) -> list[tuple[bool, str]]:
    """Return list of (passed, message) per rule."""
    results = []
    if not status["ok"]:
        results.append((False, f"Repository unreachable: {status['reason']}"))
        return results

    # Archived
    results.append((
        not status["archived"],
        "Not archived" if not status["archived"] else "Archived on GitHub",
    ))

    # Stars
    stars = status["stars"]
    min_stars = HIDDEN_GEM_MIN_STARS if allow_hidden_gem else MIN_STARS
    passed = stars > min_stars
    label = f"More than {min_stars} stars ({stars} stars" + (" — hidden-gem rule in effect)" if allow_hidden_gem else ")")
    results.append((passed, label))

    # Recent commit
    pushed = status.get("pushed_at")
    passed_commit = False
    label_commit = "Could not determine last commit date"
    if pushed:
        try:
            dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
            cutoff = datetime.now(timezone.utc) - timedelta(days=RECENT_COMMIT_MONTHS * 30)
            passed_commit = dt >= cutoff
            label_commit = f"Commit in last {RECENT_COMMIT_MONTHS} months (last pushed {pushed[:10]})"
            if not passed_commit:
                label_commit = f"No commit in last {RECENT_COMMIT_MONTHS} months (last pushed {pushed[:10]})"
        except ValueError:
            pass
    results.append((passed_commit, label_commit))

    # Contributors
    contribs = status["contributors"]
    results.append((
        contribs > 1,
        f"More than 1 contributor ({contribs} found)" if contribs > 1 else f"Only {contribs} contributor(s) found (need >1)",
    ))

    # License
    lic = status["license"]
    if lic and lic in ACCEPTED_LICENSES:
        results.append((True, f"OSI-approved license ({lic.upper()})"))
    elif lic:
        results.append((False, f"License `{lic.upper()}` is not in the accepted list"))
    else:
        results.append((False, "No license detected on the repository"))

    return results


def has_hidden_gem_justification(pr_body: str) -> bool:
    """Detect a ticked hidden-gem checkbox in the PR body."""
    if not pr_body:
        return False
    return bool(re.search(r"^\s*-\s*\[x\]\s+Hidden-gem", pr_body, re.IGNORECASE | re.MULTILINE))


def render_report(entries: list[dict]) -> str:
    if not entries:
        return ("## ✅ Quality check — no new repositories added\n\n"
                "No new GitHub repository entries were added in this PR, so the automated "
                "quality check has nothing to verify. A maintainer will still review manually.\n")

    any_failed = any(not e["overall_pass"] for e in entries)
    lines = []
    header = "## ❌ Quality check — failures" if any_failed else "## ✅ Quality check — all added repos pass the hard rules"
    lines.append(header)
    lines.append("")
    if any_failed:
        lines.append("One or more repositories added in this PR do not meet the hard inclusion rules. "
                     "See the breakdown below. Full rules are in "
                     "[CONTRIBUTING.md](../blob/master/.github/CONTRIBUTING.md).")
    else:
        lines.append("Every new repository in this PR passes the **automated** hard rules "
                     "(stars, recent commit, contributors, archived, license). A human maintainer "
                     "will still review the remaining rules (SPM support, version floors, paid-product "
                     "check, README quality, alphabetical placement).")
    lines.append("")
    for e in entries:
        icon = "✅" if e["overall_pass"] else "❌"
        lines.append(f"### {icon} [{e['name']}]({e['url']})")
        lines.append("")
        for ok, msg in e["results"]:
            bullet = "- ✅" if ok else "- ❌"
            lines.append(f"{bullet} {msg}")
        lines.append("")
    lines.append("---")
    lines.append("_Automated check. The remaining hard rules — Swift Package Manager support, "
                 "iOS 14+ / Swift 5.5+ floors, \"not a paid library / app / course\", README quality — "
                 "are verified by a human reviewer._")
    return "\n".join(lines)


def main() -> int:
    base = os.environ.get("BASE_SHA")
    head = os.environ.get("HEAD_SHA")
    pr_body = os.environ.get("PR_BODY", "")
    if not base or not head:
        print("BASE_SHA and HEAD_SHA are required", file=sys.stderr)
        return 2

    raw_entries = added_entries(base, head)
    print(f"Found {len(raw_entries)} added repo entries in README.md diff", file=sys.stderr)
    allow_hidden_gem = has_hidden_gem_justification(pr_body)
    if allow_hidden_gem:
        print("Hidden-gem justification detected — star minimum relaxed to 75", file=sys.stderr)

    report_entries = []
    overall_pass = True
    for name, owner, repo in raw_entries:
        status = check_repo(owner, repo)
        results = evaluate(status, allow_hidden_gem=allow_hidden_gem)
        passed = all(r[0] for r in results)
        if not passed:
            overall_pass = False
        report_entries.append({
            "name": name,
            "url": f"https://github.com/{owner}/{repo}",
            "results": results,
            "overall_pass": passed,
        })

    Path("quality-report.md").write_text(render_report(report_entries))
    return 0 if overall_pass else 1


if __name__ == "__main__":
    sys.exit(main())
