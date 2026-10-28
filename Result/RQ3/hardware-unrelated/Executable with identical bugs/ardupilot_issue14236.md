**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot
- **Report Author:** rmackay9
- **Report Time:** Apr 30, 2020
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 183ce50

**Steps for bug reproduction:**

- **Step 1:** Arm the vehicle and take off in Guided mode.
- **Step 2:** Fly 50m North (or any arbitrary distance).
- **Step 3:** Set the parameter `GPS_TYPE` to 0.
- **Step 4:** Wait for approximately 5 seconds and observe the vehicle's reported position.

**Observed behavior by the user:**

- **Behavior after step 1:** Vehicle is armed, and it takes off in Guided mode.
- **Behavior after step 2:** Vehicle moves to its instructed position (e.g., 50m North).
- **Behavior after step 3:** GPS is disabled by setting `GPS_TYPE` to 0.
- **Behavior after step 4:** The vehicle's reported position jumps back to the origin point instead of its last known position.

**Expected behavior:**

- **Expected behavior 1:** The vehicle’s position should be recorded and tracked accurately, even if GPS is disabled.
- **Expected behavior 2:** The vehicle should not appear at the origin when GPS is turned off; it should maintain its last known position.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user outlined detailed steps to reproduce the bug and referred to a previously suspected fixed issue (PR #14184) that may have only addressed cases involving external navigation.
- **URL of the flight log provided by the user:** Not mentioned

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A (no suggestions recorded in this report).
- **Result of the operation after the user adopted suggestion 1:** N/A (no further communication recorded).  
- **Note:** Developer `rmackay9` later confirmed in the comment dated **May 12, 2020**, that the issue has been fixed in the master branch, and the issue was subsequently marked as closed.
