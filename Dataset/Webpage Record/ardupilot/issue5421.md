# Basic Information:
### Title: Rover: add missing GPS and EKF failsafe
### Issue status: Closed
### Author: khancyr
### Issue open time: Dec 20, 2016
# Report
### Report author: khancyr
### Report Time: Dec 20, 2016
### Report Content:
Issue details  
Reproducible with SITL : set a mission, launch a mission, use PARAM set SIM_GPS_DISABLE 1 or PARAM SET SIM_GPS_NUMSATS 0 . The rover will reach the last waypoint because the bearing is good and after get lost and go weird  
Version  
from 802206b and surly long before that  
Platform  
[  ] All    
[  ] AntennaTracker    
[  ] Copter    
[  ] Plane    
[X] Rover
# Comment
## Comment1
### Comment author: OXINARF
### Comment Time: Dec 20, 2016
### Comment Content:
@gmorph I've marked this has a bug as I couldn't find an EKF failsafe and I think that indeed Rover should check the EKF health. Feel free to change the label though.
## Comment2
### Comment author: gmorph
### Comment Time: Dec 21, 2016
### Comment Content:
Ok thanks - I'll have a look.
## Comment3
### Comment author: rmackay9
### Comment Time: Mar 13, 2019
### Comment Content:
this has been included in Rover-3.5 so closing