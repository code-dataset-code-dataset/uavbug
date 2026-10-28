**Environment where the bug occurred:**

- **Hardware environment:** CubeOrangePlus autopilot (two daisy-chained)
- **Software environment:** Ardupilot Copter-4.6.0-dev
- **Report Author:** rmackay9
- **Report Time:** Apr 16, 2024
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** dce2492

**Steps for bug reproduction:**

- **Step 1:** Load Ardupilot Copter-4.6.0-dev onto both autopilots. Wipe parameters, then perform accel, compass, and RC calibration.
- **Step 2:** Set the 1st autopilot's parameters:
  - `BRD_SBUS_OUT = 3 (100Hz)`
  - `SERVO5_FUNCTION = (RCIN6)`
- **Step 3:** Connect the SBus output of the 1st autopilot to the RC input port of the 2nd autopilot.
- **Step 4:** Connect the RC input port of the 1st autopilot to an RC receiver. Use the transmitter's tuning knob to change the RC 6 input, which thereby adjusts the SERVO5 output.
- **Step 5:** Switch between firmware versions:
  - When running Copter-4.4.4 on the 1st autopilot, observe that only channel 5 correctly changes on the 2nd autopilot.
  - When running Copter-4.6.0-dev on the 1st autopilot, observe that both channels 5 and 13 incorrectly change on the 2nd autopilot.

**Observed behavior by the user:**

- **Behavior after step 5 (Copter-4.6.0-dev):** Channel 5's value is also being output as channel 13 on the 2nd autopilot, indicating there is a duplication occurring. This bug was consistent regardless of the Ardupilot version on the 2nd autopilot.

**Expected behavior:**

- **Expected behavior 1:** Only channel 5 should change on the 2nd autopilot while channel 13 remains unaffected.
- **Expected behavior 2:** The SBus output should correctly reflect only the intended RC channels without duplication.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Performed multiple tests using different firmware versions (e.g., Copter-4.4.4, Copter-4.6.0-dev).
  - Investigated and ruled out a potential cause (PR #25169) for the bug by testing before and after the PR was implemented.
- **URL of the flight log provided by the user:** Not mentioned

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `andyp1per` speculated that iomcu changes might be the cause.
  - **Result of the operation after the user adopted suggestion 1:** Fixed in PR #26825.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `tridge` suggested performing a Saleae trace on the SBus out signal with Copter-4.5.1 to observe the actual bits being transmitted.
  - **Result of the operation after the user adopted suggestion 2:** No recorded action by the user.

- **Suggestion 3 provided by developers or other personnel:** Developer `tridge` explained the issue as duplication of the lower 8 channels into the upper 8 channels due to how `reg_direct.pwm` values are read in memory, noting that the bug does not cause a crash but leads to predictable duplication.
  - **Result of the operation after the user adopted suggestion 3:** Likely informed debugging efforts and resolution in PR #26825.
