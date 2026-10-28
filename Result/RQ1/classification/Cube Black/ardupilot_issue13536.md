**Environment where the bug occurred:**

- **Hardware environment:** Cube Black autopilot
- **Software environment:** ArduCopter V4.0.3-dev 0cf747c flashed on Cube Black
- **Report Author:** rmackay9
- **Report Time:** Feb 10, 2020
- **Ardupilot commit version:** 0cf747c
- **last commit before the reporting time:** 27e825b

**Steps for bug reproduction:**

- **Step 1:** Flash the ArduCopter V4.0.3-dev 0cf747c onto the Cube Black autopilot.
- **Step 2:** Restore all parameters to their default values.
- **Step 3:** Open Mission Planner and press `Ctrl-X` to connect using MAVFTP.
- **Step 4:** Attempt to open the APM directory.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Connection established with MAVFTP.
- **Behavior after step 4:** The autopilot reboots, and the connection to the autopilot is lost. Mission Planner displays an error message.

**Expected behavior:**
- **Expected behavior 1:** The connection to the autopilot remains stable while using MAVFTP.
- **Expected behavior 2:** The APM directory opens without causing the reboot of the autopilot.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Provided steps to reproduce the bug.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `WickedShell` mentioned this issue duplicates #13085 and stated they were unable to reproduce the issue on that report. They would try the provided steps to see if they could reproduce the bug.
- **Result of the operation after the user adopted suggestion 1:** N/A (no further updates recorded as the issue was marked closed).
