**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software in the Loop) environment
- **Software environment:** Ardupilot Rover
- **Report Author:** rmackay9
- **Report Time:** Feb 14, 2017
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** acddf6b

**Steps for bug reproduction:**

- **Step 1:** Start APMRover2 in SITL environment using the command `../Tools/autotest/sim_vehicle.py -D -G --map --console`.
- **Step 2:** Set the parameter `RNGFND_GNDCLEAR` to `0`.
- **Step 3:** Restart SITL.
- **Step 4:** Arm throttle.
- **Step 5:** Set RC channel 3 to 1800 using the command `rc 3 1800`.

**Observed behavior by the user:**

- **Behavior after step 1:** SITL starts successfully.
- **Behavior after step 2:** Parameter `RNGFND_GNDCLEAR` is set to zero.
- **Behavior after step 3:** SITL restarts successfully.
- **Behavior after step 4:** Throttle is armed successfully.
- **Behavior after step 5:** A floating-point exception occurs after a few seconds. The error arises in `NavEKF2_core::EstimateTerrainOffset` at the line `float losRateSq = velHorizSq / sq(heightAboveGndEst);`, as `heightAboveGndEst` is zero.

**Expected behavior:**

- **Expected behavior 1:** The EKF2 (or EKF3) algorithm in Ardupilot Rover should properly handle situations where `RNGFND_GNDCLEAR` is set to zero without triggering a floating-point exception.
- **Expected behavior 2:** The software should ensure safe and robust calculations even when ground clearance values become zero.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided step-by-step reproduction instructions and included specific code references tied to the issue.
- **URL of the flight log provided by the user:** Not mentioned

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned
- **Result of the operation after the user adopted suggestion 1:** N/A
