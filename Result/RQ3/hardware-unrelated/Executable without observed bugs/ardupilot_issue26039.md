**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned (but affecting all platforms in ArduPilot).
- **Software environment:** Git version 2.34.1, Ubuntu 22.04.3.
- **Report Author:** Ryanf55.
- **Report Time:** Jan 20, 2024.
- **ArduPilot commit version:** Not mentioned.
- **last commit before the reporting time:** e602aa6

**Steps for bug reproduction:**

- **Step 1:** Start with an empty directory.
- **Step 2:** Clone the repository `ryanf55/ardupilot` with `--recurse-submodules` at hash `5c1ed96`.
- **Step 3:** Change directory into `ardupilot`.
- **Step 4:** Add an "upstream" remote `ardupilot/ardupilot`.
- **Step 5:** Fetch upstream.
- **Step 6:** Rebase origin on upstream.
- **Step 7:** Attempt recovery actions as detailed below when the issue is encountered.

**Observed behavior by the user:**

- **Behavior after step 6:** Git work-tree becomes unstable and unusable following rebase; user encounters errors related to submodules including:<font color='red'>rebase到最近提交并执行递归更新子模块没有发现如下错误</font>
```bash
fatal: not a git repository: ../../.git/modules/modules/lwip
error: Submodule 'modules/lwip' could not be updated.
error: Submodule 'modules/lwip' cannot checkout new HEAD.
```

**Expected behavior:**

- **Expected behavior 1:** Successfully rebase origin repository on the upstream repository considering submodules without causing issues.
- **Expected behavior 2:** Submodules should correctly sync without requiring additional manual intervention.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user attempted the following recovery actions:
    ```bash
    git submodule deinit --all --force
    git clean -dxf
    git reset --hard origin/master
    ./Tools/gittools/submodule-sync.sh
    git reset --hard upstream/master
    git reset --hard upstream/master
    ```
    These steps did not fully resolve the issue.
- **URL of flight log provided by the user:** Link to full logs not included, but referenced as `log.txt`.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `tridge` followed the provided steps initially but did not encounter the issue. Later, they reproduced the error, stating that the user-setting "`git config submodule.recurse true`" was not mentioned in the bug report.
- **Result of the operation after the user adopted suggestion 1:** The user acknowledged the finding and agreed to create a Wiki note recommending turning off `submodule.recurse` in the ArduPilot repository.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `peterbarker` followed up in May 2025, asking whether the Wiki note was created.
- **Result of the operation after the user adopted suggestion 2:** User `Ryanf55` clarified that the issue was ultimately identified as a bug within Git itself and only occurred under nondefault settings.

