Here’s the extracted information based on your markdown document:

---

**Environment where the bug occurred:**

- **Hardware environment:** APM with XL-MB1240 sonar sensor
- **Software environment:** Ardupilot software
- **Report Author:** TimGFoley
- **Report Time:** Aug 14, 2013
- **Ardupilot commit version:** Not mentioned
- **last commit before the reporting time:** a7e7084

**Steps for bug reproduction:**

- **Step 1:** Set the Sonar enable/disable parameter to 1 (Enable).
- **Step 2:** Assign channel (CH8) to turn Sonar on and off.
- **Step 3:** Leave the radio switch in the disable position (Sonar Off).
- **Step 4:** Power up the APM.
- **Step 5:** Read parameters and observe that Sonar is still set to 1 (Enabled) when it should be disabled.
- **Step 6:** Toggle CH8 back and forth on the radio, then refresh parameters. It will correctly follow the CH8 setting at this point.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The Sonar enable/disable parameter is not refreshed correctly, showing it as "Enabled" instead of "Disabled."
- **Behavior after step 5:** The settings mismatch continues until CH8 is toggled.
- **Behavior after step 6:** Sonar enable/disable begins working properly when CH8 is toggled.

**Expected behavior:**

- **Expected behavior 1:** The Sonar enable/disable parameter should reflect the CH8 switch position immediately upon power-up without requiring manual toggling.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User detailed steps to reproduce the issue, including hardware and parameter configurations.
- **URL of the flight log provided by the user:** Not mentioned

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `rmackay9` mentioned the bug has been fixed in the master branch and will be included in AC3.1. The user was asked to verify with the release candidate when it's available in approximately a week.
- **Result of the operation after the user adopted suggestion 1:** Not documented (no follow-up from the user is provided in the report).

---
