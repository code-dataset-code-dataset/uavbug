**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot master branch with commit version between `8af192e` (working commit) and `74c9c4a` (non-working commit)
- **Report Author:** rmackay9
- **Report Time:** Dec 21, 2016
- **Ardupilot commit version:** Not explicitly mentioned, but the bug is present in commit `74c9c4a`.
- **last commit before the reporting time:** 22fd202

**Steps for bug reproduction:**

- **Step 1:** Load the mission: `wp load ../Tools/autotest/copter_mission.txt`.
- **Step 2:** Set the mode to LOITER.
- **Step 3:** Arm the throttle.
- **Step 4:** Simulate automatic mode: `AUTO`.
- **Step 5:** Disable GPS: `param set SIM_GPS_DISABLE 1`.

**Observed behavior by the user:**

- **Behavior after step 5:** After GPS is disabled, the vehicle does not trigger the EKF failsafe as expected and flies off in `master`. However, in the earlier version (Copter-3.4), EKF failsafe triggers, and the vehicle switches to LAND mode.

**Expected behavior:**

- **Expected behavior 1:** After disabling GPS, the EKF failsafe should trigger.
- **Expected behavior 2:** The vehicle should switch to LAND mode after approximately 10 seconds.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user noted that the issue appeared between two specific commits:
  - Working commit: `8af192e`
  - Non-working commit: `74c9c4a`
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `OXINARF` provided a comparison between the working and non-working commits and noted significant changes in EKF2 related to position timeout/aiding mode checks. They suspected the bug might be related to these changes and not the new beacon code.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** Developer `EShamaev` pinpointed potential code issues in `AP_NavEKF2_Control.cpp`, suggesting that reliance on beacons replaced checks for GPS health, which allowed AID_ABSOLUTE to stay armed when GPS was lost.
- **Result of the operation after the user adopted suggestion 2:** N/A
- **Suggestion 3 provided by developers or other personnel:** Developer `tridge` mentioned that the issue had been fixed in the master branch, thanks to Paul's contribution.
- **Result of the operation after the user adopted suggestion 3:** The issue was resolved in the master branch.
