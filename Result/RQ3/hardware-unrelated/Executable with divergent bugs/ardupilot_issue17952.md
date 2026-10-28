**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot Copter-4.1 in SITL simulation.
- **Report Author:** rmackay9
- **Report Time:** Jul 07, 2021
- **Ardupilot commit version:** Not mentioned.
- **last commit before the reporting time:** 2ba6ae6

**Steps for bug reproduction:**

- **Step 1:** Start SITL in Karuizawa (a mountainous region of Japan) using the command `../Tools/autotest/sim_vehicle.py --map --console --speedup=10`.
- **Step 2:** Set the parameter `WPNAV_SPEED` to 1000 (horizontal speed in Guided+Auto mode set to 10m/s).
- **Step 3:** Use real-time graphing to monitor `TERRAIN_REPORT.current_height`.
- **Step 4:** Enter GUIDED mode.
- **Step 5:** Arm throttle.
- **Step 6:** Takeoff to 20m above terrain.
- **Step 7:** Load the message module.
- **Step 8:** Send the specific message `SET_POSITION_TARGET_GLOBAL_INT 0 1 0 11 3576 363215670  1386596701 20 0 0 0 0 0 0 0 0`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A.
- **Behavior after step 2:** The vehicle is observed to move horizontally much faster than its vertical movement capacity (limited by WPNAV_SPEED_UP/DN).
- **Behavior after step 8:** The drone climbs to an excessively high altitude above the terrain in steep environments, then descends back to 20m-above-terrain only upon reaching the destination.<font color='red'>无人机快速移动到目的地，但高度一直在下降，甚至变成负数</font>

**Expected behavior:**

- **Expected behavior 1:** The vehicle should maintain the set altitude-above-terrain (e.g., 20m-above-terrain) consistently during its movement, regardless of terrain steepness.
- **Expected behavior 2:** The drone's behavior should adapt horizontal speed appropriately to ensure target altitude-above-terrain is not violated even on steep terrain.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Altered `WPNAV_SPEED` to 200 (2m/s), which resulted in correct behavior in the tests.
- **URL of the flight log provided by the user:** None explicitly mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Fix implemented in PR #17539 to address the issue in Guided mode.
- **Result of the operation after the user adopted suggestion 1:** The issue was resolved in master and Copter-4.1.0-beta6, as confirmed in the comment by `rmackay9`.
