Here’s the information extracted from the given markdown document following the required format:

---

### Basic Information:
- **Title:** Crash on Quadplane Simulation
- **Issue Status:** Closed
- **Author:** RMIShane
- **Issue Open Time:** May 15, 2017
- **Ardupilot Commit Version:** commit 92d5055 (as mentioned in the report)

### **Environment where the bug occurred:**

- **Hardware environment:** Vagrant Virtual Machine (32-bit instance; the issue replicates in this environment).  
- **Software environment:** ArduPlane 3.8beta5 (git Tag: ArduPlane-beta)  

- **Report Author:** RMIShane
- **Report Time:** May 15, 2017  
- **Ardupilot Commit Version:** commit 92d5055  

### **Steps for bug reproduction:**

- **Step 1:** Run `vagrant ssh -c "sim_vehicle.py -L KSFO -j 2 -v ArduPlane -f quadplane --console --map"`.  
- **Step 2:** Load mission `wp load ../Tools/autotest/ArduPlane-Missions/KSFO-VTOL.txt`.  
- **Step 3:** Arm the throttle with `arm throttle`.  
- **Step 4:** Set to AUTO mode using `AUTO`.  

### **Observed behavior by the user:**
- **Behavior after step 1:** The mission starts in a quadplane simulation environment.
- **Behavior after step 4:** The simulation crashes with the following error:  
  ```bash 
  /vagrant/Tools/autotest/run_in_terminal_window.sh: line 54: 26969 Aborted
  ```
- Additionally, floating-point exceptions and core dumps are observed, indicated by:
  ```bash
  ERROR: Floating point exception - aborting
  ```
  and other related messages.

### **Expected behavior:**
- **Expected behavior 1:** The simulation should proceed without crashing upon entering AUTO mode.
- **Expected behavior 2:** The user can execute and analyze the mission successfully without encountering floating-point exceptions.

### **Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
  - Repeatedly pulled the repository and re-tested to verify behavior consistently.
  - Provided multiple logs of the MAVLink messages and terminal outputs before and during the crash.  
  - Test environment included commit version `92d5055` of ArduPlane.  

- **URL of the flight log provided by the user:** None specific to an external link; however, logs are included in the comments.

---

### **Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  Peter Barker asked the user to provide a specific git hash for more accurate debugging since the generic tag (`ArduPlane-beta`) was insufficient for precise identification.

  - **Result of the operation after the user adopted suggestion 1:**  
    The user updated to confirm using commit `92d5055`. Peter Barker replicated the issue based on this commit version.

- **Suggestion 2 provided by developers or other personnel:**  
  Peter Barker, after reproducing the issue, suggested running SITL with `--debug --gdb` for further detailed tracing. He also recommended a temporary workaround to switch the Vagrant virtual machine to a 64-bit instance.  

  - **Result of the operation after the user adopted suggestion 2:**  
    No explicit user feedback regarding these suggestions was recorded; however, the communication hinted at ongoing debugging efforts.

- **Suggestion 3 provided by developers or other personnel:**  
  Developer `tridge` noticed a potential issue in the `SITL::Plane::liftCoeff` function, suggesting the need for a `constrain_float()` function to sanitize `alpha` values and remove invalid inputs.
  
  - **Result of the operation after the user adopted suggestion 3:**  
    Issue resolution resulted in a commit (fix ID: `85ebe92`) applied on September 15, 2017.

- **Outcome:**  
  The issue was fixed as indicated by developer `OXINARF` and acknowledged by the user `RMIShane` with thanks. The fix addressed the floating-point exceptions that caused crashes.

### **Conclusion:**
- The issue was successfully fixed as of commit `85ebe92`.  
- Developers identified the root cause as floating-point arithmetic anomalies within the `liftCoeff` function while simulating quadplane behavior.
