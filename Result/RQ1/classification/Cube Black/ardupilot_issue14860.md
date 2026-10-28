**Environment where the bug occurred:**

- **Hardware environment:** CubeBlack flight controller
- **Software environment:** Ardupilot MAVFTP 
- **Report Author:** rmackay9
- **Report Time:** Jul 20, 2020
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 683df64

**Steps for bug reproduction:**

- **Step 1:** Set `SCR_ENABLE` = 1 and `TERRAIN_ENABLE` = 0 on a CubeBlack flight controller and reboot the autopilot.
- **Step 2:** Use Mission Planner (MP)'s Config >> MAVFTP screen to check if an `APM/scripts` directory exists.
- **Step 3:** If the directory exists:
  - **Step 3a:** Attempt to create a new directory `test`, which will succeed.
  - **Step 3b:** Delete the `scripts` directory and its contents.
  - **Step 3c:** Reboot the autopilot, open the `APM` directory, and attempt to create a directory `test2`, causing failure.
- **Step 4:** If the `scripts` directory does not exist:
  - **Step 4a:** Open the `APM` directory and attempt to create a directory `test3`, again causing failure.
  - **Step 4b:** Power off the autopilot, remove the SD card, create an `APM/scripts` directory manually on the SD card using a PC, and insert it back into the flight controller.
  - **Step 4c:** Power on the autopilot and use MAVFTP to create a directory `APM/test4`, which succeeds.

**Observed behavior by the user:**

- **Behavior after step 2:** N/A
- **Behavior after step 3:** If the `scripts` directory is deleted or does not exist, the creation of a new directory (`test2` or `test3`) fails.
- **Behavior after step 4:** After manually adding the `scripts` directory to the SD card, directory creation (`test4`) succeeds.

**Expected behavior:**

- **Expected behavior 1:** The MAVFTP feature should allow the creation of new directories regardless of whether the `scripts` folder exists or not.
- **Expected behavior 2:** Directory creation should not fail due to the absence of a `scripts` directory.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described detailed reproduction steps, including manual intervention by creating the `scripts` directory on the SD card using a PC.
- **URL of the flight log provided by the user:** N/A (no flight log included).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `IamPete1` mentioned that the issue was closed by PRs `#19267` and `#19271`.
- **Result of the operation after the user adopted suggestion 1:** The issue status was updated to “Closed” based on the mentioned PRs (`#19267` and `#19271`), indicating that the problem was resolved.
