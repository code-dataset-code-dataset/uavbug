**Environment where the bug occurred:**

- **Hardware environment:** Pixracer flight controller with standard ESCs.
- **Software environment:** Ardupilot for Copter (specific version not mentioned, but includes fixed master branch with -rc1 as discussed in the comments).
- **Report Author:** rmackay9
- **Report time:** Jan 25, 2017
- **Ardupilot commit version:** Not mentioned

**Steps for bug reproduction:**

- **Step 1:** Hold the transmitter throttle high.
- **Step 2:** Restart the flight controller board (expecting it to enter "ready-to-start-ESC-calibration-on-next-reboot" mode).
- **Step 3:** Restart the flight controller board a second time (expecting it to enter "ESC calibration mode").
- **Step 4:** Wait for ESC beeps and lower transmitter throttle.

**Observed behavior by the user:**

- **Behavior after step 1:** Throttle is held high as instructed.
- **Behavior after step 2:** Flight controller fails to recognize that the throttle is high immediately after startup and doesn't enter "ready-to-start-ESC-calibration-on-next-reboot" mode as expected.
- **Behavior after step 3:** The board does not enter "ESC calibration mode" due to the failure in step 2.

**Expected behavior:**

- **Expected behavior 1:** Upon high throttle and board restart, the flight controller should correctly enter "ready-to-start-ESC-calibration-on-next-reboot" mode.
- **Expected behavior 2:** Upon the second restart, the board should transition into "ESC calibration mode" and allow throttle to pass through to the motors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User provided a temporary workaround to set the `ESC_CALIBRATION` parameter to "3," perform a board reboot, and use automatic calibration.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `lvale` asked about ESC configuration and suggested testing with a logic analyzer connected to motor outputs and potentially to RCIN (SBus).
- **Result of the operation after the user adopted suggestion 1:** No clear results were discussed further by `lvale`.
- **Suggestion 2 provided by developers or other personnel:** `rmackay9` clarified that the issue was unrelated to ESCs and was due to the board not recognizing the high throttle on startup.
- **Result of the operation after the user adopted suggestion 2:** Bug was fixed in the master branch and included in the -rc1 release (noted by `rmackay9` on Feb 15, 2017).
