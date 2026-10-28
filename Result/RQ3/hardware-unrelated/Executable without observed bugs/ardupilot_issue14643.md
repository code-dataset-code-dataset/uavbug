**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned  
- **Software environment:** Mission Planner Simulator combined with Ardupilot firmware  
- **Report Author:** rmackay9  
- **Report Time:** Jun 20, 2020  
- **Ardupilot commit version:** Not mentioned  
- **last commit before the reporting time:** 523a97d

**Steps for bug reproduction:**

- **Step 1:** Open Mission Planner  
- **Step 2:** Open the Simulation page  
- **Step 3:** Ensure the "wipe" checkbox is checked  
- **Step 4:** Press the Copter icon at the bottom  
- **Step 5:** Open Config, MAVFtp, and perform operations on the "@RomfS" directory  

**Observed behavior by the user:**

- **Behavior after step 1 - Step 4:** N/A  
- **Behavior after step 5:**  
  1. Clicking on "@RomfS" and then immediately clicking on the unnamed (top directory?) causes a 5-second delay before the directory listing is displayed.  
  2. Attempting to create a directory with the same name as an existing directory causes Mission Planner to lock up for 30 seconds, resulting in no directory creation or error message displayed.  
  3. Attempting to delete an empty directory causes Mission Planner to lock up for 30 seconds, with a "Failed to delete file" message displayed and the directory not deleted.  
  4. Attempting to create the "scripts" directory under "@RomfS" causes Mission Planner to lock up for 30 seconds, with no directory created or error message displayed.  <font color='red'>没有锁定，直接弹出错误，可能跟mission planner版本有关，现在官方网站提供的最旧版本为2024年</font>

**Expected behavior:**

- **Expected behavior 1:** A directory listing should be displayed quickly when navigating the ROMFS directory.  
- **Expected behavior 2:** The system should either prevent users from attempting invalid operations or display a clear message explaining the Read-Only nature of the ROMFS file system, rather than locking up for 30 seconds.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reported the issue on both the ArduPilot and Mission Planner issue lists for broader investigation.  
- **URL of the flight log provided by the user:** Not mentioned  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  Developer `tridge` clarified that the ROMFS filesystem is read-only and that creating directories or files there is invalid as these are created during the firmware build process.    
  - **Result of the operation after the user adopted suggestion 1:**  
    User `rmackay9` acknowledged this clarification but highlighted that the GCS (Ground Control Station) should not lock up for 30 seconds in such cases, indicating the need for improved handling of errors or feedback for users.  

- **Suggestion 2 provided by developers or other personnel:**  
  Developer `davidbuzz` reiterated that ROMFS is "Read-Only."  
  - **Result of the operation after the user adopted suggestion 2:**  
    User `rmackay9` agreed but emphasized that the user experience remained unsatisfactory, as GCS lock-ups were still occurring.  

- **Final update from the user:**  
  User `rmackay9` reported on Jun 25, 2020, that the Mission Planner issues were resolved, and the bug report was closed.
