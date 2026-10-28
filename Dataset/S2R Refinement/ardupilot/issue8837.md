**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned.
- **Software environment:** Rover-3.4.1.
- **Report Author:** rmackay9.
- **Report Time:** Jul 06, 2018.
- **Ardupilot commit version:** Not mentioned.

**Steps for bug reproduction:**

- **Step 1:** Arm the vehicle and switch to ACRO mode.
- **Step 2:** Face the vehicle downstream in a strong current.
- **Step 3:** Monitor the vehicle's output throttle; it should go negative in an attempt to maintain zero velocity.
- **Step 4:** Observe the vehicle's heading behavior.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A.
- **Behavior after step 2:** N/A.
- **Behavior after step 3:** N/A.
- **Behavior after step 4:** The vehicle's heading may change wildly; it could even turn around and point upstream.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should maintain a stable heading when reversing.
- **Expected behavior 2:** Steering should properly adjust even if the throttle is reversed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user hypothesized the solution by adding a code snippet to reverse the steering direction when the throttle is negative. The user also mentioned alternative testing methods in a simulator or real vehicle.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Suggestion by rmackay9 to adapt the code in the `have_vectored_thrust` section and to test if reversing the steering direction fixes the issue.
- **Result of the operation after the user adopted suggestion 1:** In a later update (comment made on Jul 14, 2021), rmackay9 mentioned that the issue with vectored thrust had been addressed in version 4.1 of the software with a rework of the feature.
