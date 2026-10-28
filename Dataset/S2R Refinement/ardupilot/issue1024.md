Here is the processed output based on the Ardupilot bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot (commit version not mentioned).
- **Report Author:** AndKe.
- **Report Time:** Apr 25, 2014.
- **Ardupilot commit version:** Not mentioned.

---

**Steps for bug reproduction:**

- **Step 1:** Set up pitch stabilization.
- **Step 2:** Assign the channel for manual pitch angle control.
- **Step 3:** Shut down the transmitter (TX) and autopilot.
- **Step 4:** Start the autopilot only (do not turn on the Remote Control—RC).

---

**Observed behavior by the user:**

- **Behavior after step 1:** Stabilization works as expected.
- **Behavior after step 2:** Stabilization continues to work as intended.
- **Behavior after step 3:** N/A.
- **Behavior after step 4:** Pitch stabilization becomes extreme and non-functional until the RC transmitter is turned on. Once the RC transmitter is turned on, stabilization works as expected again, even if the radio subsequently goes off.

---

**Expected behavior:**

- **Expected behavior 1:** Pitch stabilization should work correctly even if the RC transmitter is not turned on.

---

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described steps for bug reproduction but did not provide any flight logs or further diagnostic information.
- **URL of the flight log provided by the user:** Not mentioned.

---

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `Naterater` asked if this was still a bug on Jan 18, 2019.
  - **Result of the operation after the user adopted suggestion 1:** Not applicable. No action recorded by the user.

- **Suggestion 2 provided by developers or other personnel:** Developer `rmackay9` commented on Jan 18, 2019, stating that the issue was recently fixed in Copter-3.6.5.
  - **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but the issue status was updated to “Closed.” 

---


