# Basic Information:
### Title: SITL octa-quad failed to flight after autotune
### Issue status: Closed
### Author: khancyr
### Issue open time: Nov 13, 2018
# Report
### Report author: khancyr
### Report Time: Nov 13, 2018
### Report Content:
Bug report  
After doing an autune in SITL for the default octa-quad, it cannot takeoff anymore.    
To reproduce :    
takeoff in loiter    
switch to autotune    
wait completion    
land    
get back to stabilize    
arm throttle    
rc 3 1700  
The copter won't pass 3m and complain of thrust lose.  
Please describe the problem  
Version    
Confirmed on d824cf0  
not present on 3.6.1  
Platform    
[  ] All    
[  ] AntennaTracker    
[ X] Copter    
[  ] Plane    
[  ] Rover    
[  ] Submarine  
Airframe type    
octa-quad . I didn't test on other frames
# Comment
## Comment1
### Comment author: KimHyungSub
### Comment Time: Jun 01, 2021
### Comment Content:
I tested this bug on 0bb18a1. It seems that the bug is fixed.
## Comment2
### Comment author: rmackay9
### Comment Time: Jun 01, 2021
### Comment Content:
OK great thanks.  I think I might close this one.  @khancyr feel free to re-open if I've made a mistake closing this.