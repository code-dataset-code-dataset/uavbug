**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot
- **Report Author:** rmackay9
- **Report Time:** Jun 03, 2018
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** f0a6cd5

**Steps for bug reproduction:**

- **Step 1:** Create a rover mission with a `DO_SET_REVERSE` mission command (with 1 as the first field).
- **Step 2:** Run the mission.
- **Step 3:** Remove the `DO_SET_REVERSE` from the mission.
- **Step 4:** Run the mission again.

**Observed behavior by the user:**

- **Behavior after step 4:** The vehicle starts in reverse, even after the `DO_SET_REVERSE` command is removed. This is incorrect behavior.

**Expected behavior:**

- **Expected behavior 1:** After removing the `DO_SET_REVERSE` command from the mission, subsequent mission runs should not cause the vehicle to operate in reverse unless explicitly commanded.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified the issue with the `ModeAuto::_reversed` parameter in the `mode.h` file not being reset to `false`. Suggested adding a call to `set_reversed(false)` in `mode_auto.cpp`'s `enter()` method.
- **URL of the flight log provided by the user:** Not mentioned

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `WickedShell` pointed out that automatically setting `reversed` to `false` might be problematic if a mission is resumed while the vehicle is in a reversed segment, as this could deviate from the mission profile.
  
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific action noted).

- **Suggestion 2 provided by developers or other personnel:** Developer `WickedShell` mentioned that the issue applies to all vehicles and is relevant for similar `DO_SET_SPEED` commands or related commands.
  
- **Result of the operation after the user adopted suggestion 2:** N/A (no specific action noted).

- **Follow-up resolution:** Developer `rmackay9` stated on Aug 22, 2018, that the issue was resolved in the master branch and would be included with Rover-3.5.
