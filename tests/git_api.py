import requests

'''
Not a final version. TODO: Get everything in a dict for an easy JSON generation pattern.
For now, this script takes call commits api from every repo listen in reposApi dict ,
sorts the response and prints useful data for us. This script will be useful when
it will generate a usable JSON file.

BE CAREFULL ON HOW MANY CALLS YOU DO WITH THIS SCRIPT. THERE IS A LIMIT OF CALLS THAT
YOU CAN DO PER HOUR.
'''


reposApi = {'shipit': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
            'services': 'https://api.github.com/repos/mozilla/release-services/commits',
            'beetmoverscript': 'https://api.github.com/repos/mozilla-releng/beetmoverscript/commits',
            'addonscript': 'https://api.github.com/repos/mozilla-releng/addonscript/commits',
            'shipitv2': 'https://api.github.com/repos/mozilla-releng/shipit-v2/commits',
            'build-cloud-tools': 'https://api.github.com/repos/mozilla-releng/build-cloud-tools/commits',
            'build-puppet': 'https://api.github.com/repos/mozilla-releng/build-puppet/commits',
            'shipitscript': 'https://api.github.com/repos/mozilla-releng/shipitscript/commits',
            'bouncerscript': 'https://api.github.com/repos/mozilla-releng/bouncerscript/commits',
            'treescript': 'https://api.github.com/repos/mozilla-releng/treescript/commits',
            'mozapkpublisher': 'https://api.github.com/repos/mozilla-releng/mozapkpublisher/commits',
            'OpenCloudConfig': 'https://api.github.com/repos/mozilla-releng/OpenCloudConfig/commits',
            'scriptworker': 'https://api.github.com/repos/mozilla-releng/scriptworker/commits',
            'pushsnapscript': 'https://api.github.com/repos/mozilla-releng/pushsnapscript/commits',
            'signingscript': 'https://api.github.com/repos/mozilla-releng/signingscript/commits',
            'cot-gpg-keys': 'https://api.github.com/repos/mozilla-releng/cot-gpg-keys/commits',
            'pushapkscript': 'https://api.github.com/repos/mozilla-releng/pushapkscript/commits',
            'balrogscript': 'https://api.github.com/repos/mozilla-releng/balrogscript/commits',
            'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits',
            'signtool': 'https://api.github.com/repos/mozilla-releng/signtool/commits'}


for key in reposApi:      #classic "for" that looks down into reposApi
    r = requests.get(reposApi.get(key))        #this one gets the value stored in every key
    p = r.json()      #converts variable r into a json that can be accesed like a dict
    print (key + ':')      #print the repo for the specific commits
    for keys in p:      #classic "for" that looks down into p. P is a json.
        print ('sha:' + keys['sha'] + '\n' +
                ' name: ' + keys['commit']['author']['name'] + '\n' +
                ' email: ' + keys['commit']['author']['email'] + '\n' +
                ' date:  ' + keys['commit']['author']['date'] + '\n' +
                ' url: ' + keys['url'])
        ''' ^^ Prints only what we call useful informations out of the long json we have
               For now: like a dict, it only prints sha, name, date and url of that commit.'''
