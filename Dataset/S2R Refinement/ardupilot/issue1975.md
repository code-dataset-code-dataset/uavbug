**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software in the Loop)
- **Software environment:** Ardupilot with commit version 007c96a
- **Report Author:** claymation
- **Report Time:** Mar 12, 2015
- **Ardupilot commit version:** 007c96a

**Steps for bug reproduction:**

- **Step 1:** Checkout commit 007c96a.
- **Step 2:** Run `sim_vehicle.sh -G --console --map --aircraft test`.
- **Step 3:** Arm the throttle.
- **Step 4:** Set mode to `POSHOLD`.
- **Step 5:** Execute `rc 3 1800`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Taking off in `POSHOLD` mode causes a crash with a SIGFPE (arithmetic exception), which is due to `rpy_low` being zero.

**Expected behavior:**

- **Expected behavior 1:** The drone should take off smoothly without any crashes in `POSHOLD` mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Identified the specific line of code causing the crash:
    ```cpp
    rpy_scale = (float)(out_min_pwm-thr_adj-out_best_thr_pwm)/rpy_low;
    ```
  - Flagged that `rpy_low` is zero in this case.
  - Mentioned they used `POSHOLD` mode in SITL for testing vision-aided navigation as part of precision landing software development.

- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` said they would try to reproduce the issue.
- **Result of the operation after the user adopted suggestion 1:** Developer successfully reproduced the issue.

- **Suggestion 2 provided by developers or other personnel:** Developer `rmackay9` mentioned the fix would follow promptly.
- **Result of the operation after the user adopted suggestion 2:** Developer later confirmed the issue was resolved in the master branch with commit `31a55b2`.
