Here is the extracted information from the provided markdown document regarding the Ardupilot bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Copter (latest/master/3.6-dev)
- **Report Author:** rmackay9
- **Report Time:** Mar 16, 2018
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 8511c2c

**Steps for bug reproduction:**

- **Step 1:** Create a mission with an RTL (Return to Launch) command at the end, specifying an altitude of 100m.
- **Step 2:** Run the mission in the Copter firmware version (latest/master/3.6-dev).
- **Step 3:** Observe the behavior during the initial climb stage of RTL.

**Observed behavior by the user:**

- **Behavior after step 3:** The vehicle climbs to 100m and remains stuck there, unable to proceed further. The behavior appears to be caused by non-standard handling of the RTL altitude command.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should disregard the latitude, longitude, and altitude specified in the RTL command and complete the mission without getting stuck.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified that the issue was a user error due to setting the final command as a waypoint instead of an RTL (Return to Launch) command using the MAVProxy waypoint editor.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** No explicit suggestions were provided in the documented communication.
- **Result of the operation after the user adopted suggestion 1:** N/A (issue was determined to be user error). 

---
