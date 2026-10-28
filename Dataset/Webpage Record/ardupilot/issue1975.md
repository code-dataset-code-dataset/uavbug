# Basic Information:
### Title: Copter: SIGFPE crash while taking off in POSHOLD (SITL)
### Issue status: Closed
### Author: claymation
### Issue open time: Mar 12, 2015
# Report
### Report author: claymation
### Report Time: Mar 12, 2015
### Report Content:
As of 007c96a, attempting to take off in POSHOLD mode crashes with:  
    
```bash     
 Program received signal SIGFPE, Arithmetic exception.    
0x00000000004586a0 in AP_MotorsMatrix::output_armed (this=0x702ec0 <motors>)    
    at /home/clay/ardupilot/libraries/AP_Motors/AP_MotorsMatrix.cpp:293    
293                 rpy_scale = (float)(out_min_pwm-thr_adj-out_best_thr_pwm)/rpy_low;    
```  
The culprit: rpy_low is zero.  
Steps to reproduce:  
- Check out 007c96a  
- sim_vehicle.sh -G --console --map --aircraft test  
- arm throttle  
- mode poshold  
- rc 3 1800  
/cc: @lthall
# Comment
## Comment1
### Comment author: claymation
### Comment Time: Mar 12, 2015
### Comment Content:
To be honest, I'm not sure if that's a valid use case, but I use it regularly in SITL to keep the copter centered over a simulated landing target while developing some vision-aided navigation software (yet another precision lander).
## Comment2
### Comment author: rmackay9
### Comment Time: Mar 13, 2015
### Comment Content:
@claymation, thanks for that I'll try and reproduce.
## Comment3
### Comment author: rmackay9
### Comment Time: Mar 13, 2015
### Comment Content:
Ok, I've reproduced it!  We will fix asap!
## Comment4
### Comment author: rmackay9
### Comment Time: Mar 16, 2015
### Comment Content:
This should be fixed in master now, thanks!    
31a55b2