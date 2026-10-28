Here's the extracted information for the Ardupilot bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Not mentioned
- **Report Author:** magicrub
- **Report Time:** May 07, 2015
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** a2a0d83

**Steps for bug reproduction:**

1. Perform an autoland maneuver.  
2. Abort the landing by switching out of AUTO to a different flight mode, e.g., STABILIZE.  
3. Manually gain altitude.  
4. Switch back to AUTO to continue the landing mission.  

**Observed behavior by the user:**  
- **Behavior after step 1:** Autoland starts as expected.  
- **Behavior after step 2:** Landing aborted.  
- **Behavior after step 3:** Altitude gained manually.  
- **Behavior after step 4:**  
  - The plane operates in AUTO mode again.  
  - It has a heavily constrained roll angle.  
  - The plane starts dropping altitude via the glide slope from the unintended altitude instead of resetting to the correct altitude for landing.  
  - The plane may approach the landing waypoint from an unplanned heading and altitude, potentially initiating the landing from the wrong direction if it descends too low.  

**Expected behavior:**
1. **Expected behavior 1:** When resuming AUTO from a different mode during a LAND mission, the waypoint index should decrement.  
2. **Expected behavior 2:** AUTO mode should ensure the plane adjusts its heading, altitude, and position appropriately before reinitiating the glide slope for landing.  

**Additional information provided by the user for bug investigation:**  
- **Actions taken by the user:** The user reported the scenario, described the issue, and proposed a solution to decrement the waypoint index when switching out of AUTO during LAND.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**  
- **Suggestion 1 provided by developers or other personnel:** The report mentions a pending Pull Request (`#2269`) that might address the issue.  
- **Result of the operation after the user adopted suggestion 1:** No specific result mentioned after the PR recommendation.  

---
