# Basic Information:
### Title: Copter: fix loiter throttle bug when engaged with zero throttle
### Issue status: Closed
### Author: rmackay9
### Issue open time: Mar 11, 2013
# Report
### Report author: rmackay9
### Report Time: Mar 11, 2013
### Report Content:
The way to recreate the problem is to do this:    
1. enter AUTO mode and put throttle to zero (this is possible because throttle is ignored)    
2. switch to LOITER mode with throttle zero    
Result is motors will go to minimum (it should descend but only at the maximum rate possible in loiter mode not drop out of the sky).    
Note: throttle will resume to normal the moment that throttle is raised above zero.  
Reason:    
ap.auto_armed and motors.auto_armed are set to false in set_mode incorrectly.    
motors class resets to motors.auto_armed as soon as throttle is above zero  
Notes:    
auto_armed should be moved out of the motors class.
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: May 05, 2013
### Comment Content:
fixed in master.  Will go out with AC3.0