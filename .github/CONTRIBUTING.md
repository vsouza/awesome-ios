# Contribution Guidelines

Awesome iOS is a curated list that aims to highlight the **iOS projects that genuinely matter to the community** — well-maintained, widely adopted, free for everyone, and actively used. To keep the bar high, we enforce the rules below. Please read them carefully **before** opening a pull request.

If your project does not meet every **hard rule**, please do not open a PR. We will close it.

---

## Hard rules (all of these must be true)

A project is only accepted if it meets **every** item in this list:

1. **More than 100 GitHub stargazers.**
2. **More than one contributor**, excluding bots (Dependabot, Renovate, etc.).
3. **Not archived.** The repository must load on GitHub (no 404, no 451).
4. **Has an OSI-approved open-source license** — MIT, Apache-2.0, BSD-2/3-Clause, MPL-2.0, ISC, or similar. Source-available licenses (BSL, SSPL, Elastic, Commons Clause) are **not** accepted.
5. **Is not a paid product.** Specifically:
   - **Not a paid library** — a functional free tier must exist. Freemium SDKs with a free plan are allowed; libraries gated behind a paid license are not.
   - **Not a paid app.**
   - **Not a paid course.**
6. **Supports Swift Package Manager.** CocoaPods is fine as an additional manager, but SPM is required.
7. **Targets iOS 14+ / tvOS 14+ / macOS 11+ / watchOS 7+** as its declared minimum deployment target.
8. **Built with Swift 5.5 or later**, or Objective-C that compiles cleanly with the Xcode 15+ toolchain.
9. **README is in English** and contains at least installation instructions and a usage example.

## Soft signals (project may be rejected for several of these)

These aren't hard rejections, but a project that fails several of them is unlikely to be accepted:

- **No commit in the last 24 months.** Long inactivity is a warning sign, but many stable libraries are "complete" and don't need frequent updates — we weigh this alongside other signals rather than auto-rejecting.
- **No tests** of any kind (unit, integration, or UI). Tests are strongly preferred, especially for non-trivial networking, persistence, or parsing libraries.
- **No SemVer release tag** (`vX.Y.Z`).
- **Repository is less than 30 days old** — we need to see sustained activity.
- **Still labeled alpha / beta / experimental** in the README or release notes.
- **Duplicates** an already-listed project's functionality without clear differentiation ("yet another X").
- **Promotional language** in the description ("best", "ultimate", "blazing-fast", "world-class").
- **Category minimum** — the category would still contain fewer than 3 entries after your addition.

## Hidden-gem exception

Projects with **75–100 stars** can still be accepted if the PR body explains why the project is exceptional (novel approach, solves a real ecosystem gap, notable adoption by known apps). This exception still requires:

- At least 6 months of repository history.
- More than one contributor.
- All other hard rules satisfied.

---

## Submission rules

- **One project per pull request.** PRs adding multiple projects will be asked to split.
- **Entry format:** `- [Name](URL) - Description.` (dash, single space, no em-dash).
- **Alphabetical placement** within the category (case-insensitive).
- **No iOS / Swift version numbers** in the description — they date quickly.
- **No trailing whitespace.** Set your editor to strip it on save.
- **Emojis in descriptions**: use sparingly — GitHub's renderer has historically had issues.
- **End descriptions with a full stop/period.**
- **Check your spelling and grammar** before submitting.

## Deletion criteria

We periodically re-audit the list. An entry is removed when any of these becomes true:

- The repository is **archived** or returns **404 / 451**.
- **Stars drop below 100**.
- The repo ends up with **only one contributor** after previous co-authors leave.
- The **license changes** to a non-OSI-approved or source-available license.
- The project becomes **paid-only** (loses its free tier).

Prolonged inactivity (no commits for 24+ months) is flagged as a **soft signal**, not an automatic deletion. Truly abandoned projects will be removed through periodic audits and can be proposed for removal via issues or PRs.

If you notice an entry that no longer meets the rules, please open an issue or a PR to remove it.

---

Your contributions are always welcome! Thank you for helping keep Awesome iOS high-quality. :smiley:
