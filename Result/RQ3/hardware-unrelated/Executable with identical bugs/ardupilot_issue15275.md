**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** SITL simulation environment with Ardupilot.
- **Report Author:** rmackay9
- **Report Time:** September 8, 2020
- **Ardupilot commit version:** Not mentioned.
- **last commit before the reporting time:** bc21e50

**Steps for bug reproduction:**

- **Step 1:** Arm and take off in PosHold mode.
- **Step 2:** Set parameter `ANGLE_MAX` to 2500 (limits vehicle lean angle to 25 degrees).
- **Step 3:** Set parameter `SIM_WIND_SPD` to 16 (simulates wind from the South, causing the vehicle to pitch back to +24 degrees to resist the wind).
- **Step 4:** Send RC input `rc 2 1540` (causes the vehicle to maintain about +25 degrees pitch, flying slightly backward against the wind—expected behavior).
- **Step 5:** Change parameter `SIM_WIND_SPD` to 0 (the vehicle maintains a +24 degrees pitch and continues to fly away to the South until switched to another mode like RTL or Loiter).
- **Step 6:** Send RC input `rc 2 1000` (simulates the pilot pushing the pitch stick full forward to stop the flyaway, but the vehicle only leans forward by 1 degree, barely returning home).

**Observed behavior by the user:**

- **Behavior after step 1 to 4:** The vehicle flies as expected with appropriate responses to input and environmental conditions.
- **Behavior after step 5:** The vehicle continues to fly away to the South due to wind compensation not being reset.
- **Behavior after step 6:** The vehicle leans forward by only 1 degree and does not adequately return.

**Expected behavior:**

- **Expected behavior 1:** When the wind speed drops (step 5), the vehicle should stabilize and not continue to fly away.
- **Expected behavior 2:** Proper response to pilot RC input to recover the vehicle from flyaway (step 6).

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified a potential issue with wind compensation being updated only when the vehicle is stopped and suggested limiting wind compensation to ensure the pilot can always override it.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The report author, rmackay9, suggested limiting wind compensation to 1/2 or 2/3rds of the angle-max and updating wind compensation behavior.
- **Result of the operation after the user adopted suggestion 1:** The issue was fixed in the master branch (no specific commit version mentioned) and subsequently marked as closed.
  

