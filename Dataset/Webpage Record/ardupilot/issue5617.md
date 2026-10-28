# Basic Information:
### Title: Copter: ESC calibration on Pixracer can't be initiated with high throttle on startup
### Issue status: Closed
### Author: rmackay9
### Issue open time: Jan 25, 2017
# Report
### Report author: rmackay9
### Report Time: Jan 25, 2017
### Report Content:
Normally we ask users to calibrate the ESCs by doing this:  
1. hold transmitter throttle high  
2. restart board (board goes into ready-to-start-ESC-calibration-on-next-reboot mode)  
3. restart board again (now in ESC calibration and throttle is passed through to motors)  
4. wait for ESC beeps, lower throttle  
Sadly step 2 fails because it doesn't see the throttle as high immediately after startup.  This is different than the behaviour of the Pixhawk1/2.  
The temporary work around is for the user to set the ESC_CALIBRATION parameter to "3" and reboot the board.  on start-up it will do the "automatic calibration" which involves outputting maximum throttle for 5 seconds and then minimum throttle.
# Comment
## Comment1
### Comment author: lvale
### Comment Time: Jan 25, 2017
### Comment Content:
@rmackay9 which mode are the ESC's ? I've had no issues on normal PWM, but can retest again tonight    
Also, are MOT_PWM_MIN/MAX zero ?
## Comment2
### Comment author: rmackay9
### Comment Time: Jan 25, 2017
### Comment Content:
@lvale, it's actually not ESC related.  It's not even getting into the ESC calibration mode because it's not recognising that the throttle is held high on startup.
## Comment3
### Comment author: lvale
### Comment Time: Jan 25, 2017
### Comment Content:
@rmackay9 ok, I'll test tonight with logic analyser attached to mot_outputs and if I can manage the wiring also to RCIN (SBus)
## Comment4
### Comment author: rmackay9
### Comment Time: Feb 15, 2017
### Comment Content:
This is fixed in master and has gone out with -rc1.