**Environment where the bug occurred:**

- **Hardware environment:** mindpx-v2
- **Software environment:** Ardupilot with commit version not mentioned (referred to "master branch today" by the author)
- **Report Author:** liang-tang
- **Report Time:** Dec 20, 2019
- **Ardupilot commit version:** not mentioned
- **last commit before the reporting time:** 1bd6ade

**Steps for bug reproduction:**

- **Step 1:** Clean up waypoints.
- **Step 2:** Reboot.
- **Step 3:** Use CTRL+X to show FTP window.
- **Step 4:** Delete the entire TERRAIN directory.
- **Step 5:** Reboot.
- **Step 6:** Write waypoints (remake TERRAIN directory).
- **Step 7:** Use CTRL+X to show FTP window.
- **Step 8:** Observe the results: nothing retrievable from the APM directory and possibly FCU reboot.

**Observed behavior by the user:**

- **Behavior after Step 1 - Step 6:** No issues observed.
- **Behavior after Step 7:** Nothing retrievable from the APM directory and FCU (Flight Control Unit) reboot likely occurs.

**Expected behavior:**

- **Expected behavior 1:** MAVFTP (MAVLink File Transfer Protocol) should not get stuck.
- **Expected behavior 2:** FCU should not reboot unexpectedly.
- **Expected behavior 3:** FTP operations should function normally, retrieving data as expected.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The author swapped the order of Steps 6 and 7 (write waypoints before opening the FTP window), which resolves the issue.
- **URL of the flight log provided by the user:** No log provided. Instead, a video reproducing the issue was shared: [Video Link](https://drive.google.com/open?id=10vKB2JaKgDaKCpUyhL3DW2G_Hw0QPcJB).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `WickedShell` mentioned an inability to reproduce the issue.
- **Result of the operation after the user adopted suggestion 1:** User `liang-tang` attempted again and reproduced it successfully with additional supporting video.

- **Suggestion 2 provided by developers or other personnel:** Developer `rmackay9` and others described step-by-step reproduction methods and continued testing across different versions (Copter-4.0.1, Copter-4.0.2-rc4, and Plane-4.0.5beta1).
- **Result of the operation after the user adopted suggestion 2:** Stack overflow was observed in the FTP thread when reproducing in SITL Plane-4.0.5beta1.

- **Suggestion 3 provided by developers or other personnel:** Developer `peterbarker` asked for stack traces and steps to reproduce for better diagnosis.
- **Result of the operation after the user adopted suggestion 3:** User `liang-tang` confirmed stack overflows occur when many files are read and noted that increasing the stack size of the FTP thread to 8K resolved the issue.

- **Suggestion 4 provided by developers or other personnel:** Developers discussed missing patches (f504009) to address stack overflow issues.
- **Result of the operation after the user adopted suggestion 4:** Discussions confirmed patches were integrated into beta versions, resolving the problem on Plane-4.0.6 and later.

- **Final Updates:** 
  - Developer `rmackay9` confirmed the issue is resolved in the "master" branch.
  - Developer `Davidsastresas` later confirmed the fix works properly in both Plane and Copter betas.

