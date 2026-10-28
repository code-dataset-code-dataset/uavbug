**Environment where the bug occurred:**

- **Hardware environment:** Cube Black  
- **Software environment:** Ardupilot EKF3  
- **Report Author:** rmackay9  
- **Report Time:** Jun 25, 2020  
- **Ardupilot commit version:** Not mentioned  
- **last commit before the reporting time:** fd96cdf

**Steps for bug reproduction:**

- **Step 1:** Upload master Copter to a board (Cube Black in this case).  
- **Step 2:** Reset all parameters to defaults.  
- **Step 3:** Enable EKF3 by setting the following parameters:  
  - `AHRS_EKF_TYPE = 3`  
  - `EK2_ENABLE = 0`  
  - `EK3_ENABLE = 1`  
- **Step 4:** Perform accelerometer and compass calibration.  
- **Step 5:** Enable a CAN GPS but do not actually connect one:  
  - `CAN_P1_DRIVER = 1`  
  - `GPS_TYPE = 9`.  

**Observed behavior by the user:**

- **Behavior after step 1:** N/A  
- **Behavior after step 2:** Parameters reset successfully.  
- **Behavior after step 3:** EKF3 is enabled.  
- **Behavior after step 4:** Calibration is performed, but a blank pre-arm failure message is observed prior to arming.  
- **Behavior after step 5:** The blank pre-arm failure message remains.  

**Expected behavior:**

- **Expected behavior 1:** EKF3 should provide clear and detailed pre-arm failure messages when issues occur.  
- **Expected behavior 2:** No blank messages should be presented in the pre-arm warning system.  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the issue, provided steps to reproduce it, and specified versions of hardware and several parameter settings for testing.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A (no explicit suggestions provided in the report).  
- **Result of the operation after the user adopted suggestion 1:** The issue was fixed by [PR #15503](https://github.com/ArduPilot/ardupilot/pull/15503), and the bug was closed as of October 8, 2020.  

