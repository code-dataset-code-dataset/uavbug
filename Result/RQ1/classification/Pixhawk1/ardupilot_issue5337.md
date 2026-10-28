**Environment where the bug occurred:**

- **Hardware environment:** px4-v2  
- **Software environment:** Ardupilot master branch
- **Report Author:** priseborough  
- **Report Time:** Dec 06, 2016  
- **Ardupilot commit version:** 8d87751  
- **last commit before the reporting time:** 7202acc

**Steps for bug reproduction:**

- **Step 1:** Execute `git fetch origin`.
- **Step 2:** Execute `git checkout master`.
- **Step 3:** Execute `git reset --hard origin/master`.
- **Step 4:** Execute `git submodule update --init --recursive`.
- **Step 5:** Execute `./waf clean`.
- **Step 6:** Execute `./waf configure --board px4-v2`.
- **Step 7:** Execute `./waf --targets bin/arduplane --upload`.

**Observed behavior by the user:**
- **Behavior after step 7:** Compilation fails with the error:  
  `../../libraries/AP_Landing/AP_Landing.cpp: In member function 'void AP_Landing::setup_landing_glide_slope(const Location&, const Location&, const Location&, int32_t&)':`  
  `../../libraries/AP_Landing/AP_Landing.cpp:190:36: error: qualified-id in declaration before '(' token`  

**Expected behavior:**
- **Expected behavior 1:** Successful compilation of the software with no errors.
- **Expected behavior 2:** Correct functionality in the `AP_Landing` library without any qualified-id errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
  Execution of multiple steps to reproduce the issue, as described above.
- **URL of the flight log provided by the user:** N/A

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `tridge` mentioned that the issue was fixed in the master branch by reverting 2 patches.
- **Result of the operation after the user adopted suggestion 1:** The issue was marked as resolved after the patches were reverted.
- **Suggestion 2 provided by developers or other personnel:** Developer `magicrub` acknowledged `tridge` for the quick fix and apologized for the inconvenience caused.
- **Result of the operation after the user adopted suggestion 2:** N/A (no further action required after the quick fix and apology).
