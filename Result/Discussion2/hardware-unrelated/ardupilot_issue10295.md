Below is the detailed extraction for the ArduCopter bug report in the requested format:

---

**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software In The Loop)
- **Software environment:** ArduCopter (master branch)
- **Report Author:** amilcarlucas
- **Report Time:** Jan 21, 2019
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** 7219ec3

**Steps for bug reproduction:**

- **Step 1:** Navigate to the ArduCopter directory (`cd arducopter`).
- **Step 2:** Execute the autotest script - `./Tools/autotest/autotest.py build.ArduCopter defaults.ArduCopter fly.ArduCopter --frame octa-quad`.

**Observed behavior by the user:**

- **Behavior after step 1:** Not explicitly mentioned.
- **Behavior after step 2:** Pre-arm checks fail because `ATC_RAT_RLL_D` is zeroed instead of remaining at the parameter file's original value. The specific pre-arm error message observed is:  
  `APM: PreArm: Check PIDs - ATC_RAT_RLL_D`.

**Expected behavior:**

- **Expected behavior 1:** The pre-arm check should pass without any errors.
- **Expected behavior 2:** The parameter `ATC_RAT_RLL_D` should retain its intended value (e.g., 0.022 from the octa-quad-frame parameter file).

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reported issue with specific steps to reproduce and highlighted the key parameter affecting the pre-arm check.
- **URL of the flight log provided by the user:** [Flight Log](https://gist.github.com/karthikdesai/89a883f075e87c8e9557dc0576cd48f9#file-log-txt)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** On Feb 09, 2020, developer `richardor-cell` asked for the location of an X8 sdf example file to assist in reproducing the issue.
  - **Result of the operation after the user adopted suggestion 1:** No response or follow-up recorded.

- **Suggestion 2 provided by developers or other personnel:** On Aug 29, 2021, developer `IamPete1` noted the issue was resolved via PR #10214. It allowed for a 0 `d` term but restricted negative values.
  - **Result of the operation after the user adopted suggestion 2:** The issue was marked as fixed, and the bug report was closed.
