## SERVICES

| Commit Number | Message | Data | 
|:---:|:----------------------------------:|:----:| 
|0|staticanalysis/frontend: change s3 buckets (#1360) * staticanalysis/frontend: change s3 buckets * please_cli: fail when deploy to S3 fails because of permissions|2018-08-08T12:16:51Z
|1|please_cli: Normalize tmp_dir for S3 upload for sub projects (#1359)|2018-08-08T10:45:59Z
|2|please_cli: Use skopeo to push docker images (#1342)Closes #1335This PR replaces the unmaintained push Python library with[skopeo](https://github.com/projectatomic/skopeo). At the same time itunifies the deployment methods pushing docker images to dockerregistries.|2018-08-07T11:07:44Z
|3|static-analysis/frontend: Import existing project (#1340)|2018-08-06T13:34:51Z
|4|shipit-workflow: don't hide decorated exceptions (#1344)|2018-08-03T13:21:47Z
|5|setup: bumping to v45 (#1345)|2018-08-03T10:21:30Z
|6|shipi-workflow: fix typos (#1343)|2018-08-02T18:55:19Z
|7|shipit-workflow: removing deployment to heroku and commenting out deployment to cloudops (#1333)we are commenting the deployment out because currently we don't support pushingmulti layer docker images.|2018-08-01T12:15:34Z
|8|shipit-workflow: Use decision task for in action context's `taskGroupId`. (#1228) The action specification[1] documents this as being set to the decisiontask id of the task that defined the actions There is also discussion in scriptworker docs[2] suggesting that it is setdifferently for release promotion tasks, so that the created tasks get created in a new graph. However, it turns out that release-promotion always creates tasks in a task group named after the action tasks[3][4][5]. [1] https://docs.taskcluster.net/docs/manual/using/actions/spec#json-e-context [2] https://github.com/mozilla-releng/scriptworker/blob/77bb2f2adfd08ddb22e6cec4d8bc377a58222e87/scriptworker/cot/verify.py#L1240-L1245 [3] https://searchfox.org/mozilla-central/rev/f822a0b61631cbb38901569e69b4967176314aa8/taskcluster/taskgraph/actions/release_promotion.py#313 [4] https://searchfox.org/mozilla-central/rev/f822a0b61631cbb38901569e69b4967176314aa8/taskcluster/taskgraph/decision.py#173 [5] https://searchfox.org/mozilla-central/rev/f822a0b61631cbb38901569e69b4967176314aa8/taskcluster/taskgraph/create.py#41-47|2018-08-01T01:32:40Z
|9|shipit-workflow: prefer env variables (#1326) * shipit-workflow: prefer env variables cli_common.taskcluster.get_secrets() when called wit `existing` prefers the Taskcluster secrets over `existing`. This patch should change the behaviour, so we can override the shared TC secrets with environment variables per project, that will be set by Dockerflow.* Explicit DB settings* Add comments* Re-enable dockerhub deployment|2018-07-31T19:54:14Z
|10|shipit_code_coverage: Rename `get_commit` and `get_mercurial` functions in shipit_code_coverage (#1332)|2018-07-31T19:21:48Z
|11| shipit_code_coverage_crawler: Update firefox-code-coverage and coverage-crawler dependencies (#1331)* shipit_code_coverage_crawler: Update firefox-code-coverage and coverage-crawler dependencies* nix: Override pluggy dependency coming from pytest 3.7.0|2018-07-31T18:37:17Z
|12|please_cli: Add name of the project to the exception thrown when running a not-runnable application (#1330)|2018-07-31T16:45:24Z
|13|shipit_code_coverage_crawler: Add an entry point script for shipit-code-coverage-crawler (#1329)|2018-07-31T14:03:52Z
|14|misc: enable sub folder project (eg. shipit/backend), ... (#1295)|2018-07-30T20:47:34Z
|15|shipit_frontend: v2 (#1318)|2018-07-30T19:22:10Z
|16|backend_common: has_permission for Taskcluster user was not working ... (#1316).. correctly when only single permission (string) was passed in, which was thecase in releng_tokens and releng_tooltool|2018-07-30T18:56:54Z
|17|misc: wrap every binary with LANG and LOCALE_ARCHIVE environment variable (#1317)|2018-07-30T18:19:54Z
|18|shipit_code_coverage_crawler: Add coverage-crawler as a dependency (#1323)|2018-07-30T13:36:57Z
|19|shipit_code_coverage_crawler: add CODEOWNERS for this project (#1324)|2018-07-30T09:06:12Z
|20|releng-notification-*: switch to python 3.6 and update dependencies (#1312)|2018-07-30T08:52:16Z
|21|shipit_code_coverage_ backend: Add endpoint for mapping PHIDs to hgmo revisions (#1313)|2018-07-26T14:39:23Z
|22|shipit_code_coverage_crawler: Create coverage-crawler project (#1289)|2018-07-26T12:59:42Z
|23|shipit-code-coverage-backend: Add new endpoint /v2/path, fixes #1160 (#1310)|2018-07-26T12:39:34Z
|24|shipit-static-analysis: mach lint is doing more than only js/python (yaml, spell, etc) (#1304)|2018-07-26T06:52:54Z
|25|shipit-code-coverage-backend: Load push data from ES (#1262)|2018-07-25T15:03:44Z
|26|shipit_pulse_listener: Update to Python 3.6 (#1281)|2018-07-25T13:54:25Z
|27|shipit-static-analysis: Add unit test for clang repeated issues (#1302)|2018-07-25T13:12:38Z
|28|shipit_static_analysis: Update to Python 3.6 (#1282)|2018-07-25T12:18:28Z
|29|shipit_code_coverage: Update to Python 3.6 (#1280)|2018-07-25T12:17:55Z


