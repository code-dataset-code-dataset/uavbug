**Environment where the bug occurred:**

- **Hardware environment:** Skid steering rover in SITL (Software In The Loop)
- **Software environment:** Ardupilot
- **Report Author:** rmackay9
- **Report Time:** Oct 29, 2020
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** fd0e822

**Steps for bug reproduction:**

- **Step 1:** Start a skid steering rover using the command `../Tools/autotest/sim_vehicle --map --console -f rover-skid`.
- **Step 2:** Switch the vehicle to GUIDED mode.
- **Step 3:** Arm the throttle.
- **Step 4:** Perform a right-mouse-button click on the map at a point approximately 90 degrees off from the vehicle's heading.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** 
  - If `OA_TYPE = 0`: The vehicle rotates on the spot and then heads towards the target.
  - If `OA_TYPE = 1`: The vehicle drives forward and then turns towards the target.

**Expected behavior:**

- **Expected behavior 1:** With `OA_TYPE = 1`, the vehicle should rotate on the spot (like with `OA_TYPE = 0`) and then head towards the target.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User provided steps to reproduce the issue and screenshots of the differences observed in SITL.
- **URL of the flight log provided by the user:** Not mentioned

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** Issue was resolved in `master` by PR #15442.
- **Result of the operation after the user adopted suggestion 2:** The issue was considered resolved and the ticket was closed by `rmackay9`.
