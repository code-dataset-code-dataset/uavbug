**Environment where the bug occurred:**

- **Hardware environment:** Windows 10 / Cygwin
- **Software environment:** Ardupilot Copter 3.4.4
- **Report Author:** kshahar
- **Report time:** Feb 17, 2017
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 1bd863e

**Steps for bug reproduction:**  
- **Step 1:** Run SITL (Software in the Loop) on Windows (Cygwin) using the command: `$ sim_vehicle.py --model quad --mavlink-gimbal`.  
- **Step 2:** Attempt to send commands in `MAVProxy` on TCP port 5760.  

**Observed behavior by the user:**  
- **Behavior after step 1:** The application starts and appears to bind to TCP port 5760, but connections on this port are not being accepted as expected.  
- **Behavior after step 2:** TCP connection issues are observed, including a SYN_SENT status on certain attempts (as detailed in the `netstat` output).

**Expected behavior:**  
- **Expected behavior 1:** SITL should accept connections on TCP port 5760 when started with the `--gimbal` option.
- **Expected behavior 2:** TCP communication with SITL should work without issues.

**Additional information provided by the user for bug investigation:**  
- **Actions taken by the user:** Identified a potential fix by referencing and modifying the code in `SIM_ADSB.cpp` (ensuring simulated aircraft appear only after 10 seconds to address a threading issue).  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**  
- **Suggestion 1 provided by developers or other personnel:** Developer `OXINARF` suggested that the user open a Pull Request (PR) to address the issue, as the user already identified a potential fix.
- **Result of the operation after the user adopted suggestion 1:** No explicit action recorded, but the issue was later resolved.
- **Suggestion 2 provided by developers or other personnel:** Developer `OXINARF` indicated that the bug was fixed via PR #5879.
- **Result of the operation after the user adopted suggestion 2:** The issue was resolved and the status of the bug report was marked as closed.
