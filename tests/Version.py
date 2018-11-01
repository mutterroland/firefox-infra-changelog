import requests
import json
import re

versionsLIST = {
            'services': 'https://api.github.com/repos/mozilla/release-services/tags'

}
for reposLIST_key in versionsLIST:     # for loop to scroll through the reposLIST
    r = requests.get(versionsLIST.get(reposLIST_key))     # get infos from gitAPI page
    p = r.json()     # turn into JSON content
    commit = {}
    commit_number = 0    # dictionary with key = SHA and values=name, email, date, URL and message
    for keys in p:    # loop to scroll through json content
        url_message = keys['commit']['url']
        rm = requests.get(url_message)
        pm = rm.json()
        print(pm)
        for key in pm:
            #print(key)
            commit_message = [key]['commit']
            author = {}    # dictionary with personal infor about commiter and commit
            author.update({ 'Version: ': keys['name'],
                            'Commiter name ': name,
                            'Commit message': commit_message})
                            #commit.update({ keys['sha'] : author })     # add info in commit dictionary
            commit.update({commit_number: author})
    versionsLIST.update({reposLIST_key : commit})     # add all the info into the main dictionary
with open('./jsonversion.json', 'w') as fp:     # open .json file with write permission
    json.dump(versionsLIST, fp)     # write in the .json file as a string



''' Using this Json viewer " http://www.jsonviewer.com/ ", 
        you can copy the content from github_changelog.json into RAW json data: 
            and see all the commits '''