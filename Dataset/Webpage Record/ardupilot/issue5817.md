# Basic Information:
### Title: APMRover2: motors ouput can be more than 20ms
### Issue status: Closed
### Author: khancyr
### Issue open time: Mar 04, 2017
# Report
### Report author: khancyr
### Report Time: Mar 04, 2017
### Report Content:
Issue details  
Ouput can be more that 2000 on skid steer config...    
To reproduce on sitl: arm throttle, rc 1 2000, rc 3 2000    
So it doesn't respect servo_out min and max value ...  
Version  
master : 2631bdb  
Not present on release APMrover 3.1.1  
Platform  
[  ] All    
[  ] AntennaTracker    
[  ] Copter    
[  ] Plane    
[ X] Rover
# Comment
## Comment1
### Comment author: OXINARF
### Comment Time: Mar 06, 2017
### Comment Content:
@khancyr Can you improve the title of this issue? It's not descriptive at all.
## Comment2
### Comment author: khancyr
### Comment Time: Mar 06, 2017
### Comment Content:
@OXINARF yep sorry, forget to fill it correctly
## Comment3
### Comment author: khancyr
### Comment Time: May 04, 2017
### Comment Content:
solve with SRV_Channel: limit pwm_from_angle return to +/-high_out \\\#6190