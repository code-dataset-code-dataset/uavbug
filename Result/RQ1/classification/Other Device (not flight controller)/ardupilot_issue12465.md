**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** ArduPilot.
- **Report Author:** rmackay9.
- **Report Time:** Oct 02, 2019.
- **Ardupilot commit version:** Not mentioned.
- **last commit before the reporting time:** 9405fd6

**Steps for bug reproduction:**

- **Step 1:** Plug in a battery.
- **Step 2:** Connect and set `ESC_CALIBRATION = 3` to indicate the "auto" ESC calibration should be performed (easily done through the Mission Planner (MP) interface under the Initial Setup / Mandatory Hardware / ESC Calibration screen).<font color='red'>实际需求硬件</font>
- **Step 3:** Reboot the flight controller from the Ground Control Station (GCS) without disconnecting the battery (e.g., in Mission Planner's Action tab, set the top-left drop-down to `PREFLIGHT_REBOOT_SHUTDOWN` and press "Do Action").
- **Step 4:** Observe the behavior after reboot, specifically whether the motors start spinning when they should not.

**Observed behavior by the user:**

- **Behavior after Step 1:** N/A.
- **Behavior after Step 2:** ESC calibration mode is set to auto (ESC_CALIBRATION = 3).
- **Behavior after Step 3:** Flight controller reboots without disconnecting the battery.
- **Behavior after Step 4:** Motors unexpectedly start spinning due to the ESCs being previously initialized and the flight controller outputting high PWM values upon reboot.

**Expected behavior:**

- **Expected behavior 1:** The flight controller should refuse to reboot if `ESC_CALIBRATION = 3`.
- **Expected behavior 2:** A message should be sent to the GCS to alert the user that the reboot was refused because the ESC calibration parameter is set to 3.
- **Expected behavior 3:** The user should be forced to reboot the flight controller by disconnecting the battery, preventing unintended motor spin-up.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Steps to reproduce the issue were clearly outlined along with the specific GCS actions.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` suggested modifying the `GCS_MAVLINK::handle_preflight_reboot()` function to refuse reboot if `ESC_CALIBRATION` is set to 3, while also providing a message back to the GCS.
- **Result of the operation after the user adopted suggestion 1:** The bug was resolved in the master branch as stated by `rmackay9` in a comment on Dec 09, 2019. The issue was then marked as closed.
