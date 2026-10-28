Here is the extracted information from the Ardupilot bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned.
- **Software environment:** Not mentioned.
- **Report Author:** rmackay9
- **Report Time:** Apr 28, 2015
- **Ardupilot commit version:** Not mentioned.
- **last commit before the reporting time:** 3c9ed9b

**Steps for bug reproduction:**

- **Step 1:** Place the copter at position A and let it warm up. The EKF captures its origin, and `ahrs-home` is initially set to this EKF origin. <font color='red'>实机飞行</font>
- **Step 2:** Move the copter 10 meters away.
- **Step 3:** Arm the copter. The copter sets the home position before arming, and the EKF returns the origin location.

**Observed behavior by the user:**

- **Behavior after Step 1:** The EKF captures its initial origin and sets `ahrs-home` as this location.
- **Behavior after Step 2:** N/A
- **Behavior after Step 3:** The home location is set to the last disarm location rather than the current arming location.

**Expected behavior:**

- **Expected behavior 1:** The home location should update to the current location when arming rather than retaining the last disarm location.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Explains the steps to reproduce the behavior and describes the observed and expected behaviors.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `priseborough` provided two patches:  
  - `priseborough@dc97e92`
  - `priseborough@57d891d`
  These patches fix the issue by ensuring the raw GPS position is output pre-arming.
- **Result of the operation after the user adopted suggestion 1:** The issue was confirmed fixed. Developer `rmackay9` mentioned the fix was included in firmware version AC3.3-rc3.  
