**Environment where the bug occurred:**

- **Hardware environment:** PX4 board (Pixhawk px4 board used in comments); SITL (Software in the Loop) for simulation.
- **Software environment:** ArduPilot with commit version `0c1ba48` (referenced in the comments).
- **Report Author:** rmackay9
- **Report time:** May 05, 2020
- **Ardupilot commit version:** 0c1ba48 (fixed the primary issue in SITL according to comments).
- **last commit before the reporting time:** 40cc5a5

**Steps for bug reproduction:**

- **Step 1:** Set parameter EK2_ENABLE to 0.
- **Step 2:** Set parameter EK3_ENABLE to 1.
- **Step 3:** Fetch parameters.
- **Step 4:** Set parameter EK3_GPS_TYPE to 3.
- **Step 5:** Set parameter EK3_MAG_CAL to 5 ("Use external yaw sensor").
- **Step 6:** Set parameter AHRS_EKF_TYPE to 3.
- **Step 7:** Set parameter VISO_TYPE to 1.
- **Step 8:** Set parameter COMPASS_USE to 0, COMPASS_USE2 to 0, and COMPASS_US3 to 0.
- **Step 9:** Set parameter SERIAL3_PROTOCOL to 1.
- **Step 10:** Reboot SITL and enable Vicon with the following command:
  ```bash
  ../Tools/autotest/sim_vehicle.py --map --console -A "--uartB=sim:vicon:"
  ```
- **Step 11:** Right-click on the MAVProxy map and select “Set Origin (with height).”

**Observed behavior by the user:**

- **Behavior after step 11:** 
  1. Normally, the vehicle would appear on the map but it won't if the compass is disabled (`COMPASS_USE = 0`).
  2. With the compass (`COMPASS_USE = 1`), the vehicle appears on the map and works as expected.
  3. In a real flight (or when manually moved on the ground), the EKF variance becomes very high when using an external yaw source with `COMPASS_USE = 0` and `EK3_MAG_CAL = 5`. This leads to significant yaw, pitch, and roll drift on the HUD, rendering the vehicle unflyable.

**Expected behavior:**

- **Expected behavior 1:** When using "external navigation" for yaw (`EK3_MAG_CAL = 5`), the vehicle should properly appear on the map in SITL without requiring the compass.
- **Expected behavior 2:** In real flight, the vehicle should remain stable with low EKF variance, even when using an external yaw source without the compass.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - The user attempted different parameter configurations and provided steps to reproduce the issue in SITL.
  - The user tested the real drone and SITL environments.
  - Logs for the real drone were not explicitly provided, but the user offered to collect logs using `LOG_DISARMED=1`.
- **URL of the flight log provided by the user:** None explicitly provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - Developer `anbello` pointed out that the commit `0c1ba48` resolved the issue in SITL and asked for confirmation from `rmackay9`.
- **Result of the operation after the user adopted suggestion 1:** 
  - User `rmackay9` confirmed the issue was fixed in SITL but stated no problems were observed in SITL that matched the issue in the real drone.
- **Suggestion 2 provided by developers or other personnel:** 
  - Developer `rmackay9` suggested the issue might be related to bad yaw data from the external sensor.
- **Result of the operation after the user adopted suggestion 2:** 
  - User `anbello` confirmed the problem occurred during real-world testing, even when manually moving the copter, as the vehicle was unflyable due to high EKF errors.
- **Suggestion 3 provided by developers or other personnel:** 
  - Developer `rmackay9` confirmed reproducing the issue in SITL and raised a new GitHub issue (`#14356`) for further investigation.
- **Result of the operation after the user adopted suggestion 3:** 
  - User `anbello` confirmed the issue in real-world tests and offered to collect more logs if required.


