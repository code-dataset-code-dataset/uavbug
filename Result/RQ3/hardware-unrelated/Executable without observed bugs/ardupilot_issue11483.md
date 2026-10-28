**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot (commit version: not mentioned).
- **Report Author:** rmackay9
- **Report time:** Jun 04, 2019
- **Ardupilot commit version:** not mentioned.
- **last commit before the reporting time:** de5ace2

**Steps for bug reproduction:**

- **Step 1:** Set `FENCE_ENABLE` parameter to 1.
- **Step 2:** Set `FENCE_TYPE` parameter to 1.
- **Step 3:** Set `FENCE_RADIUS` parameter to 50.
- **Step 4:** Set `AVOID_ENABLE` parameter to 1.
- **Step 5:** Set `AVOID_BEHAVE` parameter to 1.
- **Step 6:** Arm the vehicle in Loiter mode (for Copter) or Acro mode (for Rover).
- **Step 7:** Drive the vehicle towards the circular fence.

**Observed behavior by the user:**

- **Behavior after step 6:** The vehicle operates normally in Loiter/Acro mode.
- **Behavior after step 7:** The vehicle slows down but eventually breaches the circular fence. The failsafe triggers, switching the vehicle to RTL (Return to Launch) mode.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should stop at the circular fence in Loiter (Copter) or Acro (Rover) mode when `AVOID_BEHAVE` is set to 1.
- **Expected behavior 2:** The vehicle should comply with circular fence limitations without breaching, regardless of the `AVOID_BEHAVE` parameter.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User tested the functionality in SITL with specific parameter settings.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` suggested they believe they found and fixed the issue in a branch and mentioned they would raise a PR the next day.
- **Result of the operation after the user adopted suggestion 1:** The issue was fixed, and the status of the bug was marked as closed.
