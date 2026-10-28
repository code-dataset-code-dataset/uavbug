**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned  
- **Software environment:** SITL (Software In The Loop) simulation for ArduPilot  
- **Report Author:** rmackay9  
- **Report Time:** Jun 11, 2018  
- **Ardupilot commit version:** Not mentioned  

**Steps for bug reproduction:**

- **Step 1:** Set WP_SPEED to 5 (m/s).  
- **Step 2:** Create a mission with at least two commands:  
  - The first command is `DO_CHANGE_SPEED` with the second column set to 2 (m/s).  
  - The second command is a waypoint some distance away.  
- **Step 3:** Execute the mission.  

**Observed behavior by the user:**
- **Behavior after step 1:** N/A  
- **Behavior after step 2:** N/A  
- **Behavior after step 3:** The vehicle drives at 5 m/s, ignoring the `DO_CHANGE_SPEED` command.  
- As a side note, if the vehicle completes the mission and switches to HOLD mode, then if placed back into AUTO, it will drive the mission at the speed specified by the `DO_CHANGE_SPEED` command.  

**Expected behavior:**
- **Expected behavior 1:** The vehicle should adhere to the `DO_CHANGE_SPEED` command and drive at 2 m/s as specified in the mission.  
- **Expected behavior 2:** Expected consistent behavior regardless of mission transitions or mode changes.  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Steps for reproducing the issue were provided.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `IamPete1` closed the issue, referencing PR #12772.  
- **Result of the operation after the user adopted suggestion 1:** The issue was considered resolved since it was closed, but no additional user feedback on its resolution was recorded.  
