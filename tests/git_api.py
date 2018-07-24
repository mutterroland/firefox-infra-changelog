import urllib2
f =  urllib2.urlopen(https://api.github.com/repos/Akhliskun/firefox-infra-changelog/commits)
print f.read()