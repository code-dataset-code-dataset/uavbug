**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** ArduCopter with the latest RC version and QGroundControl (QGC) daily build
- **Report Author:** DonLakeFlyer
- **Report Time:** May 26, 2017
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 710594e

**Steps for bug reproduction:**

- **Step 1:** Create a mission which has a RETURN_TO_LAUNCH (RTL) at the end using the Mission Settings in QGC.
- **Step 2:** Fly the mission.
- **Step 3:** Wait for the copter to come back, land, and disarm.
- **Step 4:** Send a MISSION_CLEAR_ALL command via QGC to clear the mission from the vehicle.<font color='red'>成功清除任务</font>

**Observed behavior by the user:**

- **Behavior after step 1:** Mission creation completes successfully.
- **Behavior after step 2:** The drone successfully flies the mission.
- **Behavior after step 3:** The drone returns, lands, and disarms successfully.
- **Behavior after step 4:** Sending a MISSION_CLEAR_ALL command fails with a MAV_MISSION_ERROR, even though the vehicle is grounded and disarmed. `_flags.state == MISSION_RUNNING` remains true, which appears to be incorrect.

**Expected behavior:**

- **Expected behavior 1:** The MISSION_CLEAR_ALL command should successfully clear the mission from the vehicle after it has returned, landed, and disarmed.
- **Expected behavior 2:** `_flags.state` should not indicate `MISSION_RUNNING` when the vehicle is on the ground and disarmed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested using latest ArduCopter RC and QGC daily build; traced the error to the following code logic:
  ```bash     
  bool AP_Mission::clear()    
  {    
      // do not allow clearing the mission while it is running    
      if (_flags.state == MISSION_RUNNING) {    
          return false;    
      }    
  }    
  ```
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned in the report.
- **Result of the operation after the user adopted suggestion 1:** Not applicable.

