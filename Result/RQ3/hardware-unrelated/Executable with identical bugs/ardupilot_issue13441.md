Following the format provided for the Ardupilot bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Not mentioned
- **Report Author:** rmackay9
- **Report Time:** Feb 01, 2020
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 4afdff7

**Steps for bug reproduction:**

- **Step 1:** Wait until the "EK2 IMU0 origin set" message is displayed.
- **Step 2:** Set the parameter `GND_ALT_OFFSET` to `-3`.
- **Step 3:** Set the parameter `RTL_ALT` to `500`.
- **Step 4:** Put the drone in loiter mode.
- **Step 5:** Arm the throttle.
- **Step 6:** Increase throttle and forward pitch to fly the vehicle at least 10m above and away from home.
- **Step 7:** Activate RTL mode.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** N/A
- **Behavior after step 6:** N/A
- **Behavior after step 7:** The vehicle descends 3m before returning home.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should never descend when it enters RTL mode.
- **Expected behavior 2:** The vehicle should return at the current altitude or climb to the greater of `RTL_ALT` and (`current altitude` + `RTL_CLIMB_MIN`).

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested the scenario during `Copter-4.0.2` testing and identified the issue during these steps. Additionally, provided a graph of `CTUN.Alt` indicating the altitude during test conditions.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `rmackay9` indicated that the issue might be caused by PR #10587, which changed `current_loc.alt` to be an altitude above origin instead of an altitude above home.
- **Result of the operation after the user adopted suggestion 1:** The user `rmackay9` tested and confirmed that the issue was fixed in the master version and would also be resolved in Copter-4.0.2-rc4.
