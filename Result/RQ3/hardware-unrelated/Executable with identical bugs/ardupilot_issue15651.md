**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software in the Loop)
- **Software environment:** Ardupilot with EKF3 enabled
- **Report Author:** rmackay9
- **Report Time:** Oct 26, 2020
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** e4f4868

**Steps for bug reproduction:**

- **Step 1:** Start Copter in SITL.
- **Step 2:** Enable EKF3.
- **Step 3:** Arm and takeoff in Loiter mode.
- **Step 4:** Set the parameter `GPS_TYPE = 0` to disable GPS.
- **Step 5:** Wait for a few seconds.

**Observed behavior by the user:**

- **Behavior after step 1:** SITL simulation starts running.
- **Behavior after step 2:** EKF3 is enabled.
- **Behavior after step 3:** Copter is armed and hovering in Loiter mode.
- **Behavior after step 4:** GPS is disabled.
- **Behavior after step 5:** "EKF3 IMU0 emergency yaw reset" is displayed, which leads to a position and velocity reset. The velocity reset causes the EKF's velocity estimate to jump to zero.

**Expected behavior:**

- **Expected behavior 1:** The EKF3 should not trigger a yaw reset when GPS is disabled.
- **Expected behavior 2:** In the absence of GPS data, the GSF feature should not operate or cause position and velocity resets.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Steps to reproduce the bug scenario in SITL were detailed, including parameter modification and specific conditions causing the issue.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `priseborough` noted GPS failing externally (using `SIM_GPS_DISABLE = 1`) worked correctly without triggering the yaw reset and provided relevant log timestamps.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, but logs provided helped in investigation.
- **Suggestion 2 provided by developers or other personnel:** Developer `priseborough` pointed out a possible race condition in the code due to EKFGSF yaw estimator validity remaining high after GPS stops.
- **Result of the operation after the user adopted suggestion 2:** Developer `priseborough` replicated the bug by using RC inputs to build horizontal velocity before turning off GPS.
- **Suggestion 3 provided by developers or other personnel:** Developer `priseborough` identified the underlying cause related to `ekf_position_ok()` and `ekf_over_threshold()` functions, highlighting faulty yaw reset logic when GPS is disabled.
- **Result of the operation after the user adopted suggestion 3:** Developer `rmackay9` resolved the issue in the master branch with PR #15670.


