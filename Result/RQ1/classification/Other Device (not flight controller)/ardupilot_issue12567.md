**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software In The Loop), physical camera connected to ArduCopter via a USB Serial Adapter to uartE
- **Software environment:** ArduCopter rev 05d1046
- **Report author:** pklapperich
- **Report time:** Oct 15, 2019
- **Ardupilot commit version:** 05d1046
- **last commit before the reporting time:** 37566d0

**Steps for bug reproduction:**

- **Step 1:** Start the simulator using:  
  ```bash
  ~/ardupilot/ArduCopter $ ../Tools/autotest/sim_vehicle.py -v ArduCopter -f quad -L Pyramid -j $(nproc) -A "--uartE=uart:/dev/ttyUSB1"
  ```
- **Step 2:** Connect a ground station and configure the port parameters:  
  ```bash
  SERIAL2_BAUD 115200  
  SERIAL2_OPTIONS 0  
  SERIAL2_PROTOCOL MAVLink1  
  SR2_EXTRA1 10hz  
  SR2_EXTRA3 2hz  
  SR2_POSITION 4hz  
  ```
- **Step 3:** Restart the simulator using the same command as Step 1.
- **Step 4:** Monitor the traffic from the camera's RX line (all messages use a Mavlink1 delimiter).
- **Step 5:** Monitor the traffic from the drone's RX line (all messages use a Mavlink1 delimiter).
- **Step 6:** Upload a mission containing `MAV_CMD_DO_SET_CAM_TRIGG_DIST` and observe the messages sent to the camera.
- **Step 7:** Use the manual trigger button in the ground control station (GCS) and observe the behavior.

**Observed behavior by the user:**

- **Behavior after step 4:** Traffic from the camera showed heartbeats with a Mavlink1 delimiter.
- **Behavior after step 5:** Traffic from the drone showed messages (e.g., ATTITUDE, SIMSTATE) all using a Mavlink1 delimiter.
- **Behavior after step 6:** The `COMMAND_LONG` messages (e.g., MAV_CMD_DO_DIGICAM_CONTROL) sent to the camera during a mission are unexpectedly using a Mavlink2 delimiter, even when SERIAL4_PROTOCOL is set to Mavlink1.
- **Behavior after step 7:** Triggering the camera manually from the GCS showed the same issue as Step 6.

**Expected behavior:**
- **Expected behavior 1:** The `COMMAND_LONG` messages intended for the camera (e.g., MAV_CMD_DO_DIGICAM_CONTROL) should use the Mavlink1 delimiter, respecting the SERIAL4_PROTOCOL setting.
- **Expected behavior 2:** Any communication to the peripheral devices should adhere to the configured Mavlink protocol version.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
  The user noted the apparent misbehavior in communication with the camera when using missions versus ground station commands and observed differences when changing the SERIAL4_PROTOCOL setting from Mavlink1 to other options.
- **URL of the flight log provided by the user:** None explicitly mentioned; logs embedded in the report.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  Developer `rmackay9` acknowledged the detailed report, discussed it with expert `peterbarker`, and committed to investigating further.
- **Result of the operation after the user adopted suggestion 1:** Developer `peterbarker` prepared a fix (#12576), and it was planned for testing.
  
- **Suggestion 2 provided by developers or other personnel:**  
  `rmackay9` asked the user to re-test the patch and offered help in generating binaries for their hardware.
- **Result of the operation after the user adopted suggestion 2:**  
  The user re-tested with the patch, confirming the issue was resolved with revision 871305b. The camera now received trigger commands in Mavlink1 as expected.

- **Suggestion 3 provided by developers or other personnel:**  
  `peterbarker` clarified the behavior regarding how ArduPilot switches between Mavlink1 and Mavlink2 and confirmed the observed behavior was expected.
- **Result of the operation after the user adopted suggestion 3:**  
  The user observed that the camera behaved correctly following parameter changes, despite some initial confusion regarding the protocol switching logic.
