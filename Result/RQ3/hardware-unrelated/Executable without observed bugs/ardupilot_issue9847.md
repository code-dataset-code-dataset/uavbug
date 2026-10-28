**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot (this reference points to the master branch code).
- **Report Author:** tatsuy
- **Report Time:** Nov 18, 2018
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 723ad34

**Steps for bug reproduction:**

- **Step 1:** Wait for setting home in AHRS while seeing the message “EKF2 IMU0 is using GPS”.
- **Step 2:** Arm the system in MANUAL mode.
- **Step 3:** Simulate GPS loss (e.g., set parameter `SIM_GPS_DISABLE 1`).
- **Step 4:** Attempt to switch to Auto mode.
- **Step 5:** Start a mission.

**Observed behavior by the user:**

- **Behavior after step 1:** AHRS (attitude and heading reference system) sets the home position using GPS.
- **Behavior after step 2:** System is armed in MANUAL mode.
- **Behavior after step 3:** GPS is lost, yet the system allows switching to Auto mode.<font color='red'>切换失败</font>
- **Behavior after step 4:** Despite the loss of GPS signal and reliance on `filt_status.flags.pred_horiz_pos_rel`, the mission starts without GPS input.

**Expected behavior:**

- **Expected behavior 1:** The system should reject switching to modes that require an active GPS signal and position (like Auto mode) when GPS is lost.
- **Expected behavior 2:** The mission should not start when GPS is unavailable for Auto mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Steps to reproduce the problem were outlined, and a code reference (`APMrover2/mode.cpp: #L34`) was provided for further debugging. The user also identified a specific condition (`filt_status.flags.pred_horiz_pos_rel`) as the problematic factor.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` thanked the user (Dec 18, 2018) for raising the issue and stated a fix was included in the related pull request (PR).
- **Result of the operation after the user adopted suggestion 1:** The user `tatsuy` (Dec 20, 2018) confirmed that the problem was resolved.
