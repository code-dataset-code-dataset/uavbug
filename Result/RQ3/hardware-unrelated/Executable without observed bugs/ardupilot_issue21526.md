**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software in the Loop)
- **Software environment:** Ardupilot
- **Report Author:** rmackay9
- **Report Time:** Aug 24, 2022
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 6926466

**Steps for bug reproduction:**
- **Step 1:** `param set MNT_TYPE 1` and reboot SITL.  
- **Step 2:** Execute `long MAV_CMD_DO_MOUNT_CONTROL 0 0 0 0 0 0 4`, which changes the mount to GPS_POINT mode.  

**Observed behavior by the user:**
- **Behavior after step 1:** System reboots with the updated parameter.  
- **Behavior after step 2:** AP_Mount attempts to calculate the angle to an invalid location (0,0,0), causing a crash in SITL.<font color='red'>无崩溃现象</font>

**Expected behavior:**
- **Expected behavior 1:** The software should not attempt to calculate an angle for an invalid location.  
- **Expected behavior 2:** The system should handle mode changes to GPS_POINT gracefully, even if a location is not provided.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Reproduced the issue in SITL and described the steps leading to the crash.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Fix provided via a PR (no explicit mention of the PR number).  
- **Result of the operation after the user adopted suggestion 1:** The issue was resolved by the PR.  

