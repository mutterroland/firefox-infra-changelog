import requests
import json
import re

###That's just a test where I tried to take version of a repo and use that information

versionsLIST = {
            'services': 'https://api.github.com/repos/mozilla/release-services/tags'

}
for reposLIST_key, reposLIST_value in versionsLIST.items():     # for loop to scroll through the reposLIST
    r = requests.get(versionsLIST.get(reposLIST_key))     # get infos from gitAPI page
    p = r.json()     # turn into JSON content
    commit = {}
    commit_number = 0
    for key in p:
        version = key['name']
        url_commit = key['commit']['url']
        url_open = requests.get(url_commit)
        url_json = url_open.json()
        author = {}
        author.update(url_json)
        versionsLIST.update({author})
with open('./jsonversion.json', 'w') as fp:     # open .json file with write permission
    json.dump(versionsLIST, fp)     # write in the .json file as a string



''' Using this Json viewer " http://www.jsonviewer.com/ ", 
        you can copy the content from github_changelog.json into RAW json data: 
            and see all the commits '''