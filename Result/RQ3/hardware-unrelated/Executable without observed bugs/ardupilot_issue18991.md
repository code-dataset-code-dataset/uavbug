**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot Rover-4.2.0-DEV
- **Report Author:** rmackay9  
- **Report Time:** Oct 20, 2021  
- **Ardupilot commit version:** Not mentioned  
- **last commit before the reporting time:** d7ef63d

**Steps for bug reproduction:**

- **Step 1:** Navigate to the Rover directory (`cd Rover`).  
- **Step 2:** Execute the following command: `Tools/autotest/sim_vehicle.py --map --console`.  
- **Step 3:** Set the parameter for simulated RC failsafe: `param set SIM_RC_FAIL 1`.  
- **Step 4:** Attempt to arm the throttle: `arm throttle`.  

**Observed behavior by the user:**

- **Behavior after step 1:** Not specified.  
- **Behavior after step 2:** SITL (Software-In-The-Loop) initialized, showing console and map view.  
- **Behavior after step 3:** RC failsafe is simulated.  
- **Behavior after step 4:** The Rover is allowed to arm in Manual mode, even when in RC failsafe, despite having `ARMING_CHECK = 1`.  

**Expected behavior:**

- **Expected behavior 1:** The Rover should disallow arming in Manual, Acro, or Steering modes when under RC failsafe conditions.  
- **Expected behavior 2:** This behavior is expected even if `ARMING_CHECK` is set to 1.  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Simulated the bug in SITL and described steps clearly.  
- **URL of the flight log provided by the user:** Not mentioned.  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A  
- **Result of the operation after the user adopted suggestion 1:** N/A  
- **Additional communication:**  
    - **Comment by rmackay9 on Oct 30, 2021:** The issue was resolved by the PR linked in the issue discussion thread.  
