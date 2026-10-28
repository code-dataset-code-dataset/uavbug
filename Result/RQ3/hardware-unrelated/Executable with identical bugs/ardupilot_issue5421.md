**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot, confirmed as occurring from version `802206b` and likely for earlier versions as well.
- **Report Author:** khancyr
- **Report time:** Dec 20, 2016
- **Ardupilot commit version:** `802206b`
- **last commit before the reporting time:** b114d39

**Steps for bug reproduction:**

- **Step 1:** Set up a mission in the simulator (SITL).
- **Step 2:** Start the mission.
- **Step 3:** Change the parameter `SIM_GPS_DISABLE` to `1` or `SIM_GPS_NUMSATS` to `0` to simulate a GPS failure.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The rover continues to the final waypoint because it can use the correct bearing, but after reaching the last waypoint, it gets lost and begins to act in an erratic way.

**Expected behavior:**

- **Expected behavior 1:** The rover should detect that the GPS has failed and trigger a failsafe (EKF health check).
- **Expected behavior 2:** The rover should stop or take appropriate action rather than continuing erratically after the final waypoint.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user tested the issue on SITL with reproducible steps and provided the specific commands to replicate the problem. There was no flight log or external documentation attached explicitly.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `OXINARF` indicated the issue lacked an EKF failsafe and marked the bug appropriately, inviting `gmorph` to make changes as needed.
- **Result of the operation after the user adopted suggestion 1:** N/A (no follow-up by `OXINARF` beyond marking the issue).
- **Suggestion 2 provided by developers or other personnel:** Developer `gmorph` acknowledged the issue and indicated they would look into the problem.
- **Result of the operation after the user adopted suggestion 2:** N/A (no specific follow-up or testing updates from `gmorph` recorded in the conversation).
- **Suggestion 3 provided by developers or other personnel:** Developer `rmackay9` noted that the issue had been resolved in `Rover-3.5` and closed the ticket.
- **Result of the operation after the user adopted suggestion 3:** The resolution was verified and no further input from the user was necessary. The issue was considered fixed.
