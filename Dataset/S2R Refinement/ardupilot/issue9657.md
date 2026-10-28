Here is the formatted output for the Ardupilot bug report:

---

**Environment where the bug occurred:**  

- **Hardware environment:** SITL simulation environment  
- **Software environment:** Copter-3.6.0 Ardupilot  
- **Report Author:** rmackay9  
- **Report time:** Oct 30, 2018  
- **Ardupilot commit version:** Not mentioned  

**Steps for bug reproduction:**  

- **Step 1:** Start master or Copter-3.6 branch in SITL.  
- **Step 2:** Create a mission including a takeoff, a spline waypoint, and a return-to-launch command.  
- **Step 3:** Type LOITER to switch to Loiter mode.  
- **Step 4:** Arm throttle (to arm the vehicle).  
- **Step 5:** Execute: `rc 3 1100` (to slightly raise throttle).  

**Observed behavior by the user:**  

- **Behavior after step 1:** N/A  
- **Behavior after step 2:** N/A  
- **Behavior after step 3:** N/A  
- **Behavior after step 4:** N/A  
- **Behavior after step 5:** The vehicle climbs to the takeoff altitude, immediately completes the first spline waypoint command, and begins executing the second spline waypoint command.  

**Expected behavior:**  

- **Expected behavior 1:** The vehicle should proceed to the first spline waypoint and complete it normally.  
- **Expected behavior 2:** Execution of subsequent spline waypoint commands should proceed seamlessly.  

**Additional information provided by the user for bug investigation:**  

- **Actions taken by the user:** Recreated the issue in SITL using testing steps.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**  

- **Suggestion 1 provided by developers or other personnel:** Developer `arjun7965` noted that the issue happens regardless of the position of the first spline waypoint (e.g., skipped WP5).  
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific feedback action recorded from the user).  

- **Suggestion 2 provided by developers or other personnel:** Developer `SwiftGust` pointed out potential issues with the spline time and a feature called `fast_waypoint`. Also provided observations in SITL-Gazebo regarding waypoints skipping.  
- **Result of the operation after the user adopted suggestion 2:** Developer `SwiftGust` submitted PR #9710 as a possible solution to the issue.  

- **Suggestion 3 provided by developers or other personnel:** Developer `rmackay9` confirmed the issue was resolved in the master branch and released with Copter-3.6.6.  
- **Result of the operation after the user adopted suggestion 3:** N/A (issue reported as fixed in the latest release).  

---
