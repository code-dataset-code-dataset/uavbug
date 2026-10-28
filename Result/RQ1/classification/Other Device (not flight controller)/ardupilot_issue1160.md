**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot AC3.2
- **Report Author:** sgofferj
- **Report time:** Jun 21, 2014
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 165993d

**Steps for bug reproduction:**

- **Step 1:** Wait for the "green light."
- **Step 2:** Switch to ALTH mode (Altitude Hold).
- **Step 3:** Take off.
- **Step 4:** Fly over a safe area.
- **Step 5:** Activate autotune.
- **Step 6:** After autotune, return to the takeoff position.
- **Step 7:** Land.
- **Step 8:** Attempt to disarm in ALTH mode.

**Observed behavior by the user:**

- **Behavior after step 7:** The copter would not disarm in ALTH mode.
- **Behavior after step 8:** Switching to STAB (Stabilize) mode was required to successfully disarm. The copter also failed to disarm automatically after waiting for over 20 seconds.

**Expected behavior:**

- **Expected behavior 1:** The copter should disarm in ALTH mode when sitting on the ground.
- **Expected behavior 2:** It should be possible to disarm the copter in any mode if the vehicle is on the ground.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to disarm both manually and automatically in ALTH mode but switched to STAB mode to disarm after failing.
- **URL of the flight log provided by the user:** [Flight Log](http://home.gofferje.net/copter/)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` noted that disarming in AutoTune mode was not allowed in AC3.2 and suggested adding AutoTune to the allowed modes for disarming.
- **Result of the operation after the user adopted suggestion 1:** Developer `Jonathan` added AutoTune to the allowed modes, as mentioned by `rmackay9`. Commit `ff1f54b` was made to address this issue, but it did not entirely resolve the original request to allow disarming in all modes when the vehicle is on the ground.

