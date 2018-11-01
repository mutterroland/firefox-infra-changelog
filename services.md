## BEETMOVERSCRIPT

| Commit Number | Message | Data | 
|:---:|:----------------------------------:|:----:| 
|0|Fix fake_session breakage by pinning pytest to 3.6.4 (#176)|2018-07-31T13:02:17Z
|1|Merge pull request #175 from escapewindow/py37require python3.7 tests to be green|2018-07-27T21:51:41Z
|2|add py37 to setup.py|2018-07-27T21:45:38Z
|3|require python3.7 tests to be green|2018-07-27T21:28:00Z
|4|7.6.0|2018-07-20T18:11:02Z
|5|Support win64-asan-reporter and mac-asan-reporter platforms (#170)* Bug 1473259 - Support win64-asan-reporter and mac-asan-reporter platforms* Add newsfragment file instead of CHANGELOG file.|2018-07-20T18:06:29Z
|6|Fix in version.|2018-07-13T14:08:18Z
|7|Bump version retroactively to 7.5.0 to cope with reality.|2018-07-13T14:05:43Z
|8|stop using scriptworker event_loop fixture (#169) This fixture is being removed in mozilla-releng/scriptworker#241 ; let's stopusing it.|2018-07-05T10:04:35Z
|9|7.5.0|2018-07-02T15:44:00Z
|10|Bug 733530: add support for tests.tar.gz (#165) Bug 733530: add support for tests.tar.gz|2018-06-29T19:26:40Z
|11|s,scl3,mdc1 (#164)|2018-06-27T10:06:02Z
|12|Production push doc update (#158)|2018-06-26T09:03:43Z
|13|Add support for Buildhub (#155) * fixed branch * should be done *  added BUILDHUB_ARTIFACT constant to imports * fixed typo - all tests pass * fixed flake8 style errors

* fixed import error

* more flake8

* added buildhub paths to templates, and added buildhub artifact to the fake task json

* fixed tests

* add fake buildhub.json for testing

* yet untested fix to url and size

* fixed tests for buildhub update

* added fake target.apk file

* fixed flake8

* fixed flake8

* added forward slash in url

* changed url to point to installer instead of buildhub.json

* flake8 fix

* flake8 fix

* flake8 fix

* added space to test to test buildhub.json url encoding

* added urlencoding to buildhub url

* only URL encode the whitespaces

* changed URL encoding to better coding practice of encoding each piece

* added production beetmover roll-out newsfragment, and changed buildhub.json move_beets logic to accomodate all beetmover types

* flake8

* using urllib.parse for all url operations in get_updated_buildhub_artifact

* fixed buildhub entries in templates

* moved newsfragment to proper location

* style changes and fixed template errors|2018-06-26T08:55:35Z
|14|Merge pull request #162 from escapewindow/dephash

update requirements-prod.txt|2018-06-21T19:54:27Z
|15|update requirements-prod.txt|2018-06-21T18:20:12Z
|16|Fix multiple omits in .coveragerc (#161)

* Fix multiple omits in .coveragerc

* Add newsfragments

* Rename the newsfragment from added to fixed|2018-06-13T18:38:00Z
|17|7.4.0|2018-06-12T22:07:35Z
|18|Create checksums for public partner builds (#150)

... namely EME-free builds which end up in firefox/releases/{version}/ on archive.mozilla.org|2018-06-12T22:03:30Z
|19|7.3.0|2018-06-07T21:07:50Z
|20|Merge pull request #153 from MihaiTabara/strip-balrog-props

Strip balrog props|2018-06-06T16:27:03Z
|21|Remove dead code|2018-06-06T02:55:21Z
|22|Remove ugly devedition hacks; cleanup comments|2018-06-06T02:45:11Z
|23|Fix flake8 to make it happy|2018-06-06T02:28:46Z
|24|Minor cleanup in testing task.json files. Fixing some tests|2018-06-06T01:51:37Z
|25|Finally remove the ugly update_props hack|2018-06-06T01:51:04Z
|26|Fix schema to enforce releaseProperties and remove stagePlatform|2018-06-06T00:26:50Z
|27|Importing Lisa's PR #149|2018-06-06T00:25:26Z
|28|nitfix in README (#154)

* nitfix in README

* Switch the puppet urls from hg to git counterparts|2018-06-06T02:40:27Z
|29|Update docs for requirements.txt (bug 1458329) (#151)|2018-06-01T03:08:39Z


