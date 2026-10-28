**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned  
- **Software environment:** Ardupilot Copter AC3.5-dev with master branch  
- **Report Author:** rmackay9  
- **Report Time:** Mar 04, 2017  
- **Ardupilot commit version:** Not mentioned  

**Steps for bug reproduction:**

- **Step 1:** Map set showgpspos 1 (to make the raw GPS position visible as the blue vehicle).  
- **Step 2:** Set SIM_GPS_GLITCH_Y=0.  
- **Step 3:** Loiter, arm throttle, rc 3 1800, rc 2 1400 (to get the vehicle gently flying forward).  
- **Step 4:** Set SIM_GPS_GLITCH_Y=0.002.  

**Observed behavior by the user:**

- **Behavior after step 1:** N/A  
- **Behavior after step 2:** N/A  
- **Behavior after step 3:** Vehicle gently flying forward.  
- **Behavior after step 4:** The EKF maintains an offset after a GPS glitch. The raw GPS position and EKF estimate appear as two separate vehicles flying next to each other.  

**Expected behavior:**

- **Expected behavior 1:** After a GPS glitch, the EKF estimate (red vehicle) should reset to match the raw GPS position (blue vehicle), as observed in AC3.4.5.  

**Additional information provided by the user for bug investigation:**  

- **Actions taken by the user:** Identified the problem through simulations and noted a specific difference in behavior between AC3.4.5 and AC3.5-dev versions of Ardupilot.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**  

- **Suggestion 1 provided by developers or other personnel:**  
   - priseborough identified an issue with the reworked reset logic and its interaction with GPS velocity observations, which prevented position resets under specific conditions. Fix implemented in PR #5816.  

- **Result of the operation after the user adopted suggestion 1:**  
   - rmackay9 confirmed on Mar 06, 2017, that the issue was fixed in the master branch.  


