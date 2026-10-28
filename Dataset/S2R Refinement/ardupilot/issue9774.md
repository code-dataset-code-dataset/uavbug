**Environment where the bug occurred:**

- **Hardware environment:** Octa-quad
- **Software environment:** ArduPilot with commit version d824cf0
- **Report Author:** khancyr
- **Report Time:** Nov 13, 2018
- **Ardupilot commit version:** d824cf0

**Steps for bug reproduction:**

- **Step 1:** Take off in loiter mode.
- **Step 2:** Switch to autotune mode.
- **Step 3:** Wait for completion.
- **Step 4:** Land the copter.
- **Step 5:** Switch back to stabilize mode.
- **Step 6:** Arm the throttle.
- **Step 7:** Set `rc 3 1700`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The autotuning completes and the drone lands.
- **Behavior after step 4:** N/A
- **Behavior after step 5:** N/A
- **Behavior after step 6:** The throttle arms successfully.
- **Behavior after step 7:** The copter cannot take off beyond 3m altitude and reports a thrust loss error.

**Expected behavior:**

- **Expected behavior 1:** After autotuning, the drone should behave normally.
- **Expected behavior 2:** The drone should take off without issues and exhibit stable flight.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested in SITL for the default octa-quad configuration, provided reproduction steps.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `KimHyungSub` indicated on Jun 01, 2021, that the bug appears to be resolved on commit `0bb18a1`.
- **Result of the operation after the user adopted suggestion 1:** No further feedback from the user `khancyr`, which led to developer `rmackay9` closing the issue while also inviting the user to reopen it if the issue persists.

