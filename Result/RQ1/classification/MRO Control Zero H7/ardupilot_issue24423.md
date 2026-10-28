**Environment where the bug occurred:**

- **Hardware environment:** mRoControlZeroH7 and mRo SAM GPS + IST8308 Mag (Full Size) M10037
- **Software environment:** ArduPilot Copter-4.3.7 Stable
- **Report Author:** joshanne
- **Report Time:** Jul 28, 2023
- **ArduPilot commit version:** Not mentioned
- **last commit before the reporting time:** d5b064b

**Steps for bug reproduction:**

- **Step 1:** Configure the flight controller with an external GPS/Compass module.
- **Step 2:** Use the parameter set:
  ```bash
  EK3_IMU_MASK  7
  LOG_REPLAY 1
  ```
- **Step 3:** Enable `LOG_DISARMED`, reboot.
- **Step 4:** Generate approximately 1 minute of log data.
- **Step 5:** Disable `LOG_DISARMED`, reboot.
- **Step 6:** Download and review the log with the command:
  ```bash
  graph sum(RISI[0].DADT,1) sum(RISI[1].DADT,2) sum(RISI[2].DADT,3) IMU[0].TimeUS/1E6
  ```

**Observed behavior by the user:**

- When configured with the external GPS/Compass module, IMU data loss occurs. IMU logs show time slippage in recorded data.

**Expected behavior:**

- **Expected behavior 1:** All IMUs should be read without data loss.
- **Expected behavior 2:** Accumulated time should rise at the same gradient as elapsed time.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided the commit links to cherry-pick as an interim solution and attached log files.
- **URL of the flight log provided by the user:** [log-copter-4.3.7.zip](https://store.mrobotics.io/product-p/m10037a.htm) (contains logs of issue present and resolved states)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `andyp1per` suggested trying change #24454, suspecting DMA sharing as the cause.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly stated in the logs.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `tridge` suggested an alternative change: #24456.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly stated in the logs.

- **Outcome as per final communication:** User `joshanne` confirmed the bug was fixed in Copter-4.4.0 and expressed approval to close the issue.
