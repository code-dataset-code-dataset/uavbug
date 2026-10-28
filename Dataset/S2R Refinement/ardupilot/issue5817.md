**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** ArduPilot Rover software (master commit 2631bdb).
- **Report Author:** khancyr
- **Report Time:** Mar 04, 2017
- **Ardupilot commit version:** 2631bdb

**Steps for bug reproduction:**

- **Step 1:** Arm the throttle in SITL (Software In The Loop simulation).
- **Step 2:** Set `rc 1 2000` (RC channel 1 to 2000).
- **Step 3:** Set `rc 3 2000` (RC channel 3 to 2000).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The motor output can exceed 2000 in a skid steer configuration, consequently not respecting the servo_out min and max range.

**Expected behavior:**

- **Expected behavior 1:** Motor output should adhere to the servo_out min and max values.
- **Expected behavior 2:** Motor output should not exceed the defined upper limit (20ms or 2000) in skid steer configuration.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided reproduction steps and mentioned that the issue is not present in version `APMrover 3.1.1`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `OXINARF` asked the user (`khancyr`) to improve the issue title to make it more descriptive.
- **Result of the operation after the user adopted suggestion 1:** User acknowledged the request and apologized, stating they forgot to fill it correctly.

- **Comment from the user:** On May 04, 2017, user `khancyr` mentioned that the issue was resolved with the implementation of `SRV_Channel`: limiting `pwm_from_angle` return to +/- `high_out` via PR #6190.
