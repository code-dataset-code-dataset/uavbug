**Environment where the bug occurred:**

- **Hardware environment:** Drone with sonar attached.
- **Software environment:** Ardupilot (commit version not mentioned).
- **Report Author:** rmackay9
- **Report Time:** Dec 20, 2018
- **Ardupilot commit version:** not mentioned.
- **last commit before the reporting time:** 340429f

**Steps for bug reproduction:**

- **Step 1:** Load a mission with a takeoff to 20m.
- **Step 2:** Arm the vehicle in Loiter mode.
- **Step 3:** Switch to Auto mode and raise throttle to begin the mission.
- **Step 4:** Before the vehicle reaches 20m, switch back to Loiter mode.

**Observed behavior by the user:**

- **Behavior after step 1:** Mission loaded with takeoff requirements.
- **Behavior after step 2:** Vehicle armed in Loiter mode.
- **Behavior after step 3:** Mission starts with the vehicle taking off.
- **Behavior after step 4:** A significant throttle output spike occurs when switching from Auto mode to Loiter mode.

**Expected behavior:**

- **Expected behavior 1:** Smooth transition when switching from Auto mode to Loiter mode.
- **Expected behavior 2:** No throttle output spike.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Highlighted the potential role of sonar as part of the issue's cause.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer SergeyBokhantsev speculated whether this is an inverted case of another known bug.
- **Result of the operation after the user adopted suggestion 1:** The user rmackay9 acknowledged the possibility and referenced related issues (#7435 and #9858).

- **Suggestion 2 provided by developers or other personnel:** Developer khancyr suggested the issue may be related to the position controller reset part and expressed intentions to test without the reset.
- **Result of the operation after the user adopted suggestion 2:** Developer khancyr noted the position controller reset as a minor matter (100ms) and proposed the issue likely had another cause.

- **Suggestion 3 provided by developers or other personnel:** Developer lthall mentioned the code had been rewritten in Ardupilot version 4.1 with more stringent initialization checks, offering to reopen the issue if the problem persisted.
- **Result of the operation after user adopted suggestion 3:** N/A (no further action recorded from the user).
