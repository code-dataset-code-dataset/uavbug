**Environment where the bug occurred:**  

- **Hardware environment:** Not specified  
- **Software environment:** SITL with EKF2/EKF3 enabled in Ardupilot  
- **Report Author:** rmackay9  
- **Report Time:** Nov 28, 2018  
- **Ardupilot commit version:** Not mentioned  
- **last commit before the reporting time:** ffeeedb

**Steps for bug reproduction:**  

- **Step 1:** Follow SITL advanced testing instructions for setting up optical flow and range finder in SITL.  
- **Step 2:** Restart SITL and observe messages indicating "EKF2 IMU0 is using GPS" and "EKF2 IMU0 is using optical flow."  
- **Step 3:** Set `ARMING_CHECK = 0` to disable range finder checks when using optical flow.  
- **Step 4:** Take off in Loiter mode and fly around. 
- **Step 5:** Disable the GPS by setting `GPS_TYPE = 0`.  

**Observed behavior by the user:**  

- **Behavior after step 1:** Optical flow and range finder are correctly set up.  
- **Behavior after step 2:** Both GPS and optical flow appear to be working simultaneously.  
- **Behavior after step 3:** Range finder checks disabled.  
- **Behavior after step 4:** Vehicle flies around successfully in Loiter mode.  
- **Behavior after step 5:** An EKF failsafe triggers, switching the vehicle to LAND mode despite the EKF successfully estimating the position.  

**Expected behavior:**  
- **Expected behavior 1:** The EKF failsafe should not trigger a LAND mode because the vehicle is still controllable.  
- **Expected behavior 2:** The user should be able to switch to other flight modes (e.g., RTL).  
- **Expected behavior 3:** A failsafe should only trigger if optical flow data becomes unavailable.  
- **Expected behavior 4:** A warning should notify the user that the vehicle is only using optical flow.  

**Additional information provided by the user for bug investigation:**  

- **Actions taken by the user:**  
  - Test repeated by disabling the EKF failsafe (`FS_EKF_THRESH = 0`), which allowed the vehicle to remain in Loiter mode and hold its position without triggering LAND.  

- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**  

- **Suggestion 1 provided by developers or other personnel:** rmackay9 suggested testing with EKF3 to determine if the issue persists with this version.  
- **Result of the operation after the user adopted suggestion 1:** User did not explicitly indicate test results from earlier, but later confirmed that testing with EKF3 resolved the issue as no EKF failsafe was triggered.  

- **Suggestion 2 provided by developers or other personnel:** EosBandi inquired if RTL could work using only relative positioning (optical flow).  
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned.  

- **Suggestion 3 provided by developers or other personnel:** rmackay9 closed the issue after confirming that no EKF failsafe occurred when using EKF3.  
- **Result of the operation after the user adopted suggestion 3:** Issue resolved with EKF3 but noted that EKF3 handled the failover worse than EKF2 in other respects.  

