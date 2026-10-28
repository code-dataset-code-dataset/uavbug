Here's the extracted information based on the markdown document provided:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Ardupilot.
- **Report Author:** rmackay9.
- **Report Time:** Mar 11, 2013.
- **Ardupilot commit version:** Not mentioned.

**Steps for bug reproduction:**

- **Step 1:** Enter AUTO mode and put the throttle to zero (note: throttle is ignored in AUTO mode).
- **Step 2:** Switch to LOITER mode while keeping the throttle at zero.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A.
- **Behavior after step 2:** Motors go to minimum throttle. This behavior causes the drone to drop rapidly, rather than descending at the maximum allowed rate in LOITER mode. The throttle resumes normal behavior once it is raised above zero.

**Expected behavior:**

- **Expected behavior 1:** The drone should descend at the maximum rate allowed in LOITER mode, rather than falling out of the sky.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified the bug behavior during mode switching.
- **URL of the flight log provided by the user:** Not mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A (the report author and developer appear to be the same person, rmackay9).
- **Result of the operation after the user adopted suggestion 1:** N/A.
- **Suggestion 2 provided by developers or other personnel:** rmackay9 moved `auto_armed` out of the `motors` class and implemented a fix.
- **Result of the operation after the user adopted suggestion 2:** The bug was fixed in the master branch and released with AC3.0 (comment added by rmackay9 on May 05, 2013).

---
