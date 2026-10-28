**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Master branch of the TradHeli firmware on Ardupilot.
- **Report Author:** rmackay9
- **Report Time:** Jul 13, 2019
- **Ardupilot commit version:** Not mentioned.
- **last commit before the reporting time:** d587836

**Steps for bug reproduction:**

- **Step 1:** Load the latest TradHeli firmware.
- **Step 2:** Clear all parameters and reboot the vehicle.
- **Step 3:** Use Mission Planner (MP) and check the messages window.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The messages in MP included a blank "PreArm" message, as seen in the message list below:
  - EKF2 IMU1 initial yaw alignment complete.
  - EKF2 IMU1 forced reset.
  - PreArm:
  - PreArm: Compass not calibrated.
  - PreArm: Compass not calibrated.
  - PreArm: 3D Accel calibration needed.
  - PreArm: Hardware safety switch.
  - PreArm: Collective below Failsafe.<font color='red'>QGC上未发现空的PreArm，且提示motor interlock enabled</font>

**Expected behavior:**

- **Expected behavior 1:** The "PreArm" messages should contain relevant and accurate pre-arm warnings or notifications.
- **Expected behavior 2:** There should be no blank "PreArm" messages displayed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided detailed steps to replicate the issue and a transcript of the observed message log.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A (no explicit suggestions recorded from other developers).
- **Result of the operation after the user adopted suggestion 1:** N/A.
- **Suggestion 2 provided by developers or other personnel:** The user (rmackay9) identified that this issue was not limited to TradHeli but also occurred with multicopters.
- **Result of the operation after the user adopted suggestion 2:** N/A.

**Resolution:**

- The issue was fixed in the master branch as of Oct 31, 2019. The status of the issue was marked as **Closed**.
