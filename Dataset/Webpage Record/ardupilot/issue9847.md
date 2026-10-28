# Basic Information:
### Title: Rover: fix the check of switching to other mode which requires position when GPS lost while arming
### Issue status: Closed
### Author: tatsuy
### Issue open time: Nov 18, 2018
# Report
### Report author: tatsuy
### Report Time: Nov 18, 2018
### Report Content:
If armed, we can change to GPS mode despite losing GPS.  
1. Waiting for setting home in AHRS (wait for the message "EKF2 IMU0 is using GPS")  
2. Arming in MANUAL mode  
3. GPS lost (param set SIM_GPS_DISABLE 1)  
4. switching to Auto mode  
After these steps, start mission without GPS.  
The cause is that filt_status.flags.pred_horiz_pos_rel is true while losting GPS.    
https://github.com/ArduPilot/ardupilot/blob/master/APMrover2/mode.cpp\\\#L34  
If you remove filt_status.flags.pred_horiz_pos_rel from the condition, it works.    
It means that changing to GPS required mode is fail when GPS lost.
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Dec 18, 2018
### Comment Content:
Thanks for raising this issue. I've included a fix in this PR.
## Comment2
### Comment author: tatsuy
### Comment Time: Dec 20, 2018
### Comment Content:
Thank you!    
I confirmed that this problem was solved.