# Ensure there is a summary for a pull request
fail 'Please provide a summary in the Pull Request description' if github.pr_body.length < 5

# Warn when there are merge commits in the diff
warn 'Please rebase to get rid of the merge commits in this Pull Request' if git.commits.any? { |c| c.message =~ /^Merge branch 'master'/ }

# Only one library per pull request
warn 'Please only add one library per Pull Request' if git.lines_of_code > 1

# Warn if pull request is not updated
warn 'Please update the Pull Request title' if github.pr_title.include? 'Update README.md'
