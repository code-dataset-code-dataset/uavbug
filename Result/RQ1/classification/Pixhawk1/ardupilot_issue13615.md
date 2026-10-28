Here is the extracted and formatted information based on your document about the Ardupilot bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk1, likely all fmuv3 boards, possibly all ChibiOS boards.
- **Software environment:** Ardupilot master branch.
- **Report Author:** Jaaaky
- **Report Time:** Feb 19, 2020
- **Ardupilot commit version:** not mentioned
- **last commit before the reporting time:** d8f6089

**Steps for bug reproduction:**

- **Step 1:** Add `env OPTIMIZE -O3` to `hwdef.dat` (optional, but increases the probability of the issue occurring).
- **Step 2:** Build and upload firmware.
- **Step 3:** Using `mavproxy`, run signing setup configuration.
- **Step 4:** Reboot the board.
- **Step 5:** Wait until the long failsafe is triggered and RTL (Return to Launch) is active. (Optional, but increases the probability of encountering the issue.)
- **Step 6:** Connect any SBUS RC receiver into the RC-IN port, or have the receiver connected and turn on the transmitter at this point.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** N/A
- **Behavior after step 6:** An FMU WATCHDOG reset is triggered in over 50% of cases. If optimization level `-O3` is enabled, the system can completely freeze, making the watchdog unresponsive, requiring a power cycle. The issue only occurs once per boot cycle.

**Expected behavior:**
- **Expected behavior 1:** The board should not crash or reset when receiving RC input.
- **Expected behavior 2:** The system should remain stable and fully operational during normal use.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Bisected the bug and identified the first problematic commit `[7168a02] HAL_ChibiOS: display RC protocol for iocmu`. Reported the issue in prior platforms (e.g., forums and chat), but the issue was not reproducible until this test. Shared reproduction steps and details about optimization levels and SCHED_LOOP_RATE.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` pointed out a related forum post for possible reference.
  - **Result of the operation after the user adopted suggestion 1:** User `Jaaaky` acknowledged the reference but noted that earlier logs (such as the MON log) were unhelpful for bug analysis.

- **Suggestion 2 provided by developers or other personnel:** Developer `tridge` reproduced the issue and investigated, confirming the RCIN thread was running out of stack space due to extra bytes used when signing packets. He identified the cause and worked on a fix.
  - **Result of the operation after the user adopted suggestion 2:** Developer `tridge` fixed the issue and determined that signing added 576 bytes to the stack cost of `send_text()`. The fix was implemented.

- **Final Update:** Developer `rmackay9` confirmed that the issue was fixed in master and would be released as part of Copter-4.0.3-rc1. The issue was subsequently closed.

--- 

Let me know if further clarifications or reports are needed!
