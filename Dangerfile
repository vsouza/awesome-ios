# Ensure there is a summary for a pull request
fail 'Please provide a summary in the Pull Request description' if github.pr_body.length < 5

# Warn when there are merge commits in the diff
warn 'Please rebase to get rid of the merge commits in this Pull Request' if git.commits.any? { |c| c.message =~ /^Merge branch 'master'/ }

# Only one library per pull request
warn 'Please only add one library per Pull Request' if git.lines_of_code > 1

# Warn if pull request is not updated
warn 'Please update the Pull Request title' if github.pr_title.include? 'Update README.md'

# Check links
require 'json'
results = File.read 'ab-results-README.md-filtered.json'
j = JSON.parse results
unless j.count==0
  fail 'Found links issues'
  message = "#### Link issues by [`awesome_bot`](https://github.com/dkhamsing/awesome_bot)\n\n"
  message << "Line | Status | Link\n"
  message << "| ---: | :---: | --- |\n"

  j.sort_by { |h| h['loc'] }.each do |i|
    error = i['error']
    loc   = i['loc']
    link  = i['link']
    s     = i['status']

    if error=='Dupe'
      message << "#{loc} | Dupe | #{link}"
    else
      message << "#{loc} | [#{s}](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/#{s}) | #{link}"
      message << "<br> #{error}" unless error ==''
      message << " redirects to<br>#{i['redirect']}" unless i['redirect']==''
    end
    message << "\n"
  end

  markdown message
end
