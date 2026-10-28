### Extracted Information:

**Environment where the bug occurred:**

- **Hardware environment:** Software In The Loop (SITL) with quad airframe type
- **Software environment:** Ardupilot master branch
- **Report Author:** peterbarker
- **Report Time:** Apr 05, 2021
- **Ardupilot Commit Version:** not mentioned
- **last commit before the reporting time:** 9a7f807

**Steps for bug reproduction:**

- **Step 1:** Start SITL running Copter (e.g., navigate to the `ArduCopter` directory and run `../Tools/autotest/sim_vehicle.py --map --console`).
- **Step 2:** Switch the vehicle to "Guided" mode.
- **Step 3:** Arm the throttle of the vehicle.
- **Step 4:** Command a takeoff to a height of 10 meters using `takeoff 10`.
- **Step 5:** Disable GPS by setting the parameter `GPS_TYPE` to `0`.
- **Step 6:** Wait for 30 seconds for the vehicle to enter the `Land` mode and automatically land.
- **Step 7:** Re-enable GPS by setting the parameter `GPS_TYPE` to `2`.
- **Step 8:** Switch back to "Guided" mode.
- **Step 9:** Attempt to arm the throttle. This is expected to fail because EKF is unable to regain its position estimate.<font color='red'>成功arm</font>

**Observed behavior by the user:**

- **Behavior after step 1 to step 4:** Vehicle successfully enters "Guided" mode, arms, and takes off to 10 meters.
- **Behavior after step 5:** GPS is disabled.
- **Behavior after step 6:** Vehicle enters "Land" mode and lands.
- **Behavior after step 7:** GPS is re-enabled.
- **Behavior after step 9:** The throttle cannot be armed as the EKF fails to recover its position estimate.

**Expected behavior:**

- **Expected behavior 1:** The EKF should recover its position estimate after GPS is re-enabled.
- **Expected behavior 2:** Instead of an EKF failsafe, the EKF should execute a position-reset or similar, and allow throttle arming.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reproduced the issue in SITL as described in the steps.
- **URL of the flight log provided by the user:** ArduCopter-RefindGPS-00000003.TXT, log file in replay `.BIN` format.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `priseborough` analyzed solution statuses, flags, and fault statuses and confirmed that the EKF begins using the GPS based on innovation sequences. 
- **Result of the operation after the user adopted suggestion 1:** The fault was further investigated, showing intermittent solution state changes (relevant flags for takeoff and touchdown being toggled briefly).
- **Suggestion 2 provided by developers or other personnel:** Developer `rmackay9` suggested closing the bug report, reasoning that the user's test used the position estimate before EKF recovery.
- **Result of the operation after the user adopted suggestion 2:** `peterbarker` agreed to close the issue but noted the bug was fixed in the master branch, ensuring it will not reappear in autotests.

