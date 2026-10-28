**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot software
- **Report Author:** magicrub
- **Report Time:** Jun 23, 2015
- **Ardupilot commit version:** Not mentioned

**Steps for bug reproduction:**

- **Step 1:** Boot up a drone with some unknown previously uploaded mission.
- **Step 2:** Switch to AUTO mode.
- **Step 3:** Switch back to MANUAL mode.
- **Step 4:** Upload a new mission.
- **Step 5:** Switch to AUTO mode and launch.

**Observed behavior by the user:**

- **Behavior after step 1:** The flight control system retains the mission command index in RAM.
- **Behavior after step 2:** The auto mode executes the old mission's first command instead of the new one.
- **Behavior after step 5:** The drone continues executing the cached/old mission commands instead of the newly uploaded mission commands.

**Expected behavior:**

- **Expected behavior 1:** On mission upload, the mission index should reset to 1.
- **Expected behavior 2:** Switching to AUTO mode should always execute the most recent mission stored in flash memory.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user implemented a partial fix by adding logic to reset the mission index when the current index was 1, but noted this was not a general solution.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` noted the importance of ensuring that partial mission uploads do not disrupt the mission.
- **Result of the operation after the user adopted suggestion 1:** No specific result mentioned as the discussion was ongoing.

- **Suggestion 2 provided by developers or other personnel:** After discussion with developers `tridge` and `rmackay9`, the solution identified was to reset the cached mission item only when switching from non-AUTO to AUTO mode and when not currently executing it.
- **Result of the operation after the user adopted suggestion 2:** The issue was resolved by implementing the fix referenced in pull request `#2448`.
