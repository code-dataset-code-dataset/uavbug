**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned, but test performed using SITL (Software-In-The-Loop).
- **Software environment:** ArduPilot Copter (Simulated - via `sim_vehicle.py`).
- **Report Author:** rmackay9
- **Report Time:** Jul 01, 2023
- **ArduPilot commit version:** Not mentioned
- **last commit before the reporting time:** 670873d

**Steps for bug reproduction:**
- **Step 1:** Run simulation using `sim_vehicle.py --map --console -L CMAC2`.
- **Step 2:** Set the parameter `EK3_SRC1_YAW` to 8 (GSF) using the command `param set EK3_SRC1_YAW 8`.
- **Step 3:** Reboot the vehicle.
- **Step 4:** Switch to ALT_HOLD flight mode.
- **Step 5:** Arm the throttle.
- **Step 6:** Set RC channel 3 to 2000 (wait ~5 seconds for the vehicle to climb).
- **Step 7:** Set RC channel 3 to 1500 to level out the drone.
- **Step 8:** Set RC channel 2 to 1400, then to 1600, and finally back to 1500.

**Observed behavior by the user:**
- **Behavior:** At Step 8, an expected message "EKF yaw reset to GPS" does not appear when the vehicle is traveling below 5m/s.

**Expected behavior:**
- **Expected behavior 1:** GSF alignment should occur when the vehicle completes the prescribed motion steps.
- **Expected behavior 2:** The expected message "EKF yaw reset to GPS" should appear, indicating proper yaw alignment.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** The user repeated the test by adjusting the GPS_VEL_YAW_ALIGN_MIN_SPD parameter to a lower value (1.0 m/s), which bypasses the 5 m/s threshold and allows the behavior to work as expected.
- **URL of the flight log provided by the user:** Not mentioned in the report.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `priseborough` suggested using different values of GPS_VEL_YAW_ALIGN_MIN_SPD for different vehicle types. For smaller copters, which may not involve magnetometers, a smaller threshold like 1.0 m/s may be more appropriate.
- **Result of the operation after the user adopted suggestion 1:** No direct implementation feedback was recorded for this suggestion in the report.
- **Suggestion 2 provided by developers or other personnel:** `rmackay9` later suggested the issue could be related to another problem discussed here [https://discuss.ardupilot.org/t/copter-4-4-1-released/107005/9].
- **Result of the operation after the user adopted suggestion 2:** No update provided regarding testing after considering this new issue.
- **Additional developer comment:** `rmackay9` confirmed on May 14, 2024, that the issue has been resolved in the master branch and the fix is included in version Copter-4.5.2.
