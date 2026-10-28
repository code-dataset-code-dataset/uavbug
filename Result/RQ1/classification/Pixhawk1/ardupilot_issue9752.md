**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk autopilot (multiple versions mentioned), using a CC (Companion Computer) with APsync.
- **Software environment:** ArduRover V3.4.2 on PX4v3 board with MAVProxy and GCS software (Mission Planner and Solex).
- **Report Author:** jmachuca77
- **Report Time:** Nov 10, 2018
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 03f1dec

**Steps for bug reproduction:**

- **Step 1:** Use an APsync-enabled Companion Computer (CC) to connect to a Pixhawk autopilot.
- **Step 2:** Run MAVProxy locally on the CC to monitor telemetry packet loss.
- **Step 3:** Connect a Ground Control Station (GCS) like Mission Planner or Solex via UDP.
- **Step 4:** Monitor the reported telemetry packet loss during the GCS connection/disconnection process.

**Observed behavior by the user:**

- **Behavior after step 1:** Packet loss reported by MAVProxy is negligible (0–0.2% max).
- **Behavior after step 2:** Packet loss remains negligible.
- **Behavior after step 3:** Once a GCS is connected, packet loss spikes to approximately 80%.
- **Behavior after step 4:** Upon disconnecting the GCS, packet loss subsides back to normal levels.

**Expected behavior:**

- **Expected behavior 1:** The telemetry system should maintain negligible packet loss (e.g., 0–0.2%) regardless of whether a GCS is connected.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided detailed output logs from MAVProxy that displayed packet statistics during the issue. The user also described testing with multiple versions of ArduPilot on the Rover platform and confirmed no issue occurred with QGC (another GCS software).
- **URL of the flight log provided by the user:** Packetloss_logs.zip was shared (full URL was not mentioned).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `tridge` suggested that MAVProxy calculates packet loss based on sequence numbers, which might get miscounted due to certain scenarios, such as duplicate or out-of-order packets.
  - **Result of the operation after the user adopted suggestion 1:** No further information was provided initially about action taken based on this suggestion, though later confirmation was made about updates resolving the issue.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `peterbarker` asked for clarification regarding the system IDs of the GCSs involved.
  - **Result of the operation after the user adopted suggestion 2:** No explicit response was documented.

- **Suggestion 3 provided by developers or other personnel:** Developer `rmackay9` identified a typo in the user’s report mentioning, “Copter does show this behavior,” which the user corrected to, “Copter does not show this behavior.”
  - **Result of the operation after the user adopted suggestion 3:** Typo corrected by the user.

- **Suggestion 4 provided by developers or other personnel:** Developer `mnumanuyar` provided a code snippet explaining how the loss calculation in a customized build of MAVLink could miscount overflow during packet loss assessments.
  - **Result of the operation after the user adopted suggestion 4:** Later confirmation from the user indicated that the issue was indeed caused by miscalculation of packet loss by the telemetry system and was resolved in recent Rover releases.

- **Final resolution shared by the user:** User `jmachuca77` confirmed on Aug 7, 2020, that the misreported packet loss was due to how the loss was measured. The issue was no longer present in the latest Rover releases.
