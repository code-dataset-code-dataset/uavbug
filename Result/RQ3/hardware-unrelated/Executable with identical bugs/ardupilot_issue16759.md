Here is the extracted information in the required format based on the markdown document about the Ardupilot bug report:

---

**Environment where the bug occurred:**
- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot
- **Report Author:** rmackay9
- **Report time:** Feb 26, 2021
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** b2d4cef

**Steps for bug reproduction:**
- **Step 1:** Set speed controller parameters so the vehicle requires a lot of I-term:
    - `param set CRUISE_THROTTLE 100`
    - `param set CRUISE_SPEED 5`
    - `param set ATC_SPEED_P 0`
- **Step 2:** Graph `VFR_HUD.throttle` to make the output throttle visible.
- **Step 3:** Make the speed controller I-term visible:
    - `param set GCS_PID_MASK 2`
    - Graph `PID_TUNING.I`.
- **Step 4:** Create a simple auto mission (using "wp editor") with a long straight segment.
- **Step 5:** Arm the rover and switch to Auto mode.
- **Step 6:** Once the I-term has risen, switch to Manual mode.
- **Step 7:** Change to Acro mode and observe for throttle spike and/or I-term not being reset to 0.

**Observed behavior by the user:**
- **Behavior after Step 5:** During a large Ackerman steering Rover test, while driving in Auto mode, interrupting the mission and switching to Acro mode caused the throttle to spike to nearly 100% without manually raising the throttle.
- **Behavior after Step 7:** The user observed that the I-term was not reset to 0 when it hadn’t been used recently.

**Expected behavior:**
- **Expected behavior 1:** The throttle should not spike to nearly 100% when changing from Auto to Acro mode.
- **Expected behavior 2:** The I-term should reset to 0 if it has not been used recently (within the last second or so).

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** The user provided specific reproduction steps, including parameter settings and observation methods.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Not explicitly outlined in the document.
- **Result of the operation after the user adopted suggestion 1:** The developer `rmackay9` analyzed the issue and implemented a fix.
- **Final resolution:** Fix merged to master, and the issue was declared closed by the developer on Mar 19, 2021.

---
