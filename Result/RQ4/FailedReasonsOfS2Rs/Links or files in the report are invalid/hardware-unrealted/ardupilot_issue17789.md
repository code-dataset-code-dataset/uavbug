Here is the information extracted and formatted for your provided Ardupilot bug report:

---

### **Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Simulation (SITL)
- **Report Author:** rmackay9
- **Report Time:** Jun 17, 2021
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** e4eb833

---

### **Steps for bug reproduction:**

- **Step 1:** Modify Ardupilot code to add debugging to `NavEKF3_core::setOrigin()` to print `EKF_Origin.alt`.<font color='red'>最近提交中无此函数的实现，仅在AP_NavEKF3_core.h中有定义，似乎已被弃用</font>
- **Step 2:** Set parameter `SIM_GPS_DISABLE` to `1` (disable GPS).
- **Step 3:** Restart the simulation.
- **Step 4:** Set flight mode to `ALT_HOLD`.
- **Step 5:** Arm the throttle.
- **Step 6:** Use RC input channel 3 set to 2000 (wait for the vehicle to climb to at least 10m).
- **Step 7:** Use RC input channel 3 set to 1500.
- **Step 8:** Set parameter `SIM_GPS_DISABLE` to `0` (re-enable GPS).

---

### **Observed behavior by the user:**

- **Behavior after step 8:** The EKF3's core's individual `EKF_origin.alt` values are often different by significant values (e.g., 56m). The discrepancy stems from code that incorrectly adjusts the altitude for certain EKF cores multiple times, causing mismatched altitudes.

---

### **Expected behavior:**

- **Expected behavior 1:** The individual EKF3 core `EKF_origin.alt` values should remain consistent across all cores.
- **Expected behavior 2:** The software should correctly account for altitude adjustments and not apply them multiple times.

---

### **Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
  - Analyzed the issue by running simulations with GPS disabled and adding debugging statements.  
  - Provided the problematic code snippet:  
    ```bash
    if (inFlight) {    
       EKF_origin.alt += (int32_t)(100.0f * stateStruct.position.z);    
    }
    ```
  - Noted PR references: PR #17786 and PR #17766 led to the discovery of this bug.

- **URL of the flight log provided by the user:** Not mentioned.

---

### **Communication between developers or other personnel and the user:**

- **Suggestion provided by developers or other personnel:** Not recorded in the document.
- **Result of the operation after the user adopted suggestion:** Not recorded in the document.

---
