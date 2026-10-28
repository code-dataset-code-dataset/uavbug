### **Parsed Output for the Ardupilot Bug Report**

**Environment where the bug occurred:**
- **Hardware environment:** Flight controller with Rover firmware installed.
- **Software environment:** Ardupilot, mavlink communication with Mission Planner.
- **Report Author:** rmackay9
- **Report Time:** Aug 23, 2018
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** e878558

**Steps for bug reproduction:**
- **Step 1:** Install Rover on a flight controller.
- **Step 2:** Connect with Mission Planner and on the Config/Tuning >> Planner page, set the "Sensor" drop-down to 1.
- **Step 3:** Open the mavlink inspector window by navigating to the Flight Data screen, pressing `Ctrl-F`, and selecting "MAVLink In." Expand Vehicle1/Comp1 and observe the update rate of the `RAW_IMU` message.
- **Step 4:** Increase `SCHED_LOOP_RATE` to 100 (from the default of 50) and reboot the flight controller.
- **Step 5:** Reconnect and recheck that the Config/Tuning >> Planner page still has "Sensor" set to 1. If it has reverted, set it back to 1.
- **Step 6:** Recheck the mavlink explorer and note the update rate, which should now be 2 Hz instead of the expected rate.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** The configuration allows the user to observe the mavlink messages.
- **Behavior after step 6:** The `RAW_IMU` message update rate increased to 2 Hz (faster than expected), indicating that changing `SCHED_LOOP_RATE` influences the message rate incorrectly.

**Expected behavior:**
- **Expected behavior 1:** The mavlink message update rate to the GCS should remain at the configured rate, regardless of changes to `SCHED_LOOP_RATE`.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Steps provided to reproduce the behavior, detailed observations of mavlink message rates.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** N/A (no explicit suggestions were made in the comments).
- **Result of the operation after the user adopted suggestion 1:** N/A.
- **Additional notes from developers:** On Aug 25, 2018, the issue commenter `rmackay9` noted that this was fixed in the master branch and would be included in Rover-3.5.
