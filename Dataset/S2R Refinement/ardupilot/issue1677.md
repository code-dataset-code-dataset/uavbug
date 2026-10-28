**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** Ardupilot
- **Report Author:** rmackay9
- **Report Time:** Dec 09, 2014
- **Ardupilot commit version:** Not mentioned

**Steps for bug reproduction:**

- **Step 1:** Create a mission with a do-set-home command with zero latitude, longitude, and altitude followed by a waypoint.
- **Step 2:** Execute the mission.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:**  
  1. EKF produces a very large position variance, causing AHRS to switch back and forth between DCM and EKF.  
  2. The variance causes an arithmetic exception in the dataflash logging of EKF as it attempts to compress the variance into an `int16_t`.  
  3. The vehicle tries to fly to a location that seems to be the waypoint target location plus the offset from the original home to the new home.  
  4. In some cases, all motor outputs logged as the same values for channels 1 through 4, causing a crash.

**Expected behavior:**

- **Expected behavior 1:** Proper handling of the do-set-home mission command without producing large position variances.  
- **Expected behavior 2:** Vehicles should only fly to the intended waypoint rather than a miscalculated location.  
- **Expected behavior 3:** No arithmetic exceptions or logging errors should occur.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided a reproduction scenario.
- **URL of the flight log provided by the user:** Forum links referenced for both the original issue and a similar subsequent event:  
  [Link 1](http://ardupilot.com/forum/viewtopic.php?f=100&t=10587) - Original issue.  
  [Link 2](http://ardupilot.com/forum/viewtopic.php?f=100&t=10676&p=26845#p26845) - Another occurrence of the issue.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** rmackay9 suggested rejecting the do-set-home mission command in the short term to prevent problems.  
- **Result of the operation after the user adopted suggestion 1:** Log suggests that motor outputs for all channels appeared the same, leading to a crash.  
- **Suggestion 2 provided by developers or other personnel:** rmackay9 mentioned pushing a change to remove support for the do-set-home mission command for AC3.2.1.  
- **Result of the operation after the user adopted suggestion 2:** Issue resolved in AC3.3 with proper support for both the mission command and immediate command.  


