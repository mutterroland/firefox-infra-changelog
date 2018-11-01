## BEETMOVERSCRIPT

| Commit Number | Message | Data | 
|:---:|:----------------------------------:|:----:| 
|ship-it|Nightly 65: Merge and deply when 65 builds are available for all locales (#238)|2018-10-23T09:27:10Z
|release-services|staticanalysis/frontend: Load all tasks & support http errors (#1651)|2018-10-26T09:44:46Z
|beetmoverscript|Bug 1408083 - Drop support for beta/releases of single locale repacks for Fennec (#187)|2018-10-03T10:31:17Z
|addonscript|Merge pull request #96 from mozilla-releng/pyup-update-scriptworker-14.0.0-to-15.0.0  Update scriptworker to 15.0.0|2018-08-06T02:31:08Z
|shipit-v2|RM ALL|2018-09-06T19:59:08Z
|build-cloud-tools|Merge pull request #368 from garbas/remove-uplift-frontend  terraform: remove uplift frontend domains|2018-10-23T14:44:31Z
|build-puppet|Bug 1481203 - allow worker to use new thunderbird ship-it scopes (#278)  The release-mark-as-shipped task for Thunderbird has new scopes  assigned to it. This patch updates the scriptworker configuration  to recognize those scopes, preventing the 'This worker is not configured  to handle scope "project:comm:thunderbird:releng:ship-it:server:production"'  error when run.|2018-10-26T20:11:29Z
|shipitscript|Merge pull request #13 from escapewindow/py37  require py37 to be green|2018-07-27T23:05:59Z
|bouncerscript|Merge pull request #41 from tp-tc/stub-path-platforms   Check that paths exist per-platform.|2018-09-04T22:05:15Z
|treescript|Merge pull request #111 from tp-tc/bump-robustcheckout.py  Bump robustcheckout.py.|2018-10-02T16:43:57Z
|mozapkpublisher|0.9.0|2018-10-19T12:42:47Z
|OpenCloudConfig|Bug 1501609 - debug log forwarder  split eventlogs to prevent skipping all logs when one filter is unavailable|2018-10-26T14:55:35Z
|scriptworker|Merge pull request #253 from Callek/1486970   Bug 1486970 - Need to pass push info to cron decision task validation|2018-10-19T19:51:57Z
|pushsnapscript|0.2.4|2018-10-05T13:09:12Z
|signingscript|Merge pull request #85 from escapewindow/py37-tests  switch to oracle java 8 to fix autograph integration tests|2018-10-24T17:55:39Z
|cot-gpg-keys|remove expiring 2018-05-25_2018-09-25_gecko-3-b-win2012|2018-09-14T17:32:19Z
|pushapkscript|Update documentation (#47)    Update documentation to not reference `dry_run` anymore    Remove rst README in favor of the md one    Fix warning at packaging time    Change where the worker-type should point.|2018-10-19T16:33:54Z
|balrogscript|Merge pull request #39 from tp-tc/bz2  Bug 1481121: Add support for specifying bz2 full update blobs.|2018-08-30T17:51:09Z
|funsize|No expires (#82)    Do not set task `expires`    It causes some issues with artifact uploads. By default Tascluster sets  this field to `deadline` + 1 year.      Version bump|2017-08-30T13:55:46Z
|signtool|Merge pull request #12 from escapewindow/retry-connectionerror  Retry for ConnectionError during upload.|2018-08-27T17:31:58Z


