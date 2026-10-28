Here is the extracted information from your markdown document:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** ArduPilot with EKF3 enabled
- **Report Author:** rmackay9
- **Report Time:** Aug 22, 2020
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** d7c569c

**Steps for bug reproduction:**

- **Step 1:** Follow the wiki instructions to enable wheel encoders.<font color='red'>wiki上已经没有开启wheel encoder的指令</font>
- **Step 2:** Set `ARMING_CHECK` to 0 (to disable the pre-arm check complaining about high HDOP).
- **Step 3:** Set `GPS_TYPE` to 1 (to enable GPS).
- **Step 4:** Create a small mission and switch the vehicle to Auto mode.

**Observed behavior by the user:**

- **Behavior after Step 4:**  
    - The EKF failsafe triggers and the vehicle is switched to Hold mode.  
    - The reported altitude jumps between 0 and 584.  

**Expected behavior:**

- **Expected behavior 1:** The EKF3 should be able to use GPS primarily with wheel encoders as a backup.  
- **Expected behavior 2:** No failsafe condition should occur under normal operations.  
- **Expected behavior 3:** Altitude readings should remain consistent and accurate.  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Steps to reproduce the issue were provided.  
- **URL of the flight log provided by the user:** Not mentioned.  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned in the document.  
- **Result of the operation after the user adopted suggestion 1:** Bug was fixed in master branch.  
- **Additional Comment:** The issue was confirmed resolved with the master branch and the issue was closed on Nov 25, 2020.  

---
