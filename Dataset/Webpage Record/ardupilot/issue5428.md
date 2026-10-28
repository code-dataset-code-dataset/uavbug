# Basic Information:
### Title: EKF: GPS failure doesn't trigger EKF failsafe (master)
### Issue status: Closed
### Author: rmackay9
### Issue open time: Dec 21, 2016
# Report
### Report author: rmackay9
### Report Time: Dec 21, 2016
### Report Content:
There appears to be a bug in master (not in AC3.4) that leads to the EKF failsafe not triggering if the GPS is lost.  
The issue can be recreated by doing this in SITL:  
- wp load ../Tools/autotest/copter_mission.txt  
- LOITER  
- arm throttle  
- rc 3 1100  
- AUTO  
- param set SIM_GPS_DISABLE 1  
What should happen is after about 10 seconds the EKF failsafe will trigger and the vehicle will switch to LAND mode.  In Copter-3.4 this is what happens.  In master however the vehicle flies off.  
The issue seems to have appeared with the addition of the Beacon/Pozyx code on Nov 30th somewhere between these two commits:  
- this commit from Nov 30th doesn't work: 74c9c4a  
- this earlier commit from Nov 30th works: 8af192e  

# Comment
## Comment1
### Comment author: OXINARF
### Comment Time: Dec 21, 2016
### Comment Content:
Here is the comparison between the two: 8af192e...74c9c4a  
There are quite a few changes on the EKF2, at first sight I couldn't find any bug. Almost certain that the bug isn't in the beacon stuff, but in the changes to position timeout/aiding mode checks.
## Comment2
### Comment author: EShamaev
### Comment Time: Dec 21, 2016
### Comment Content:
I think the problem is in file AP_NavEKF2_Control.cpp where you rely on beacon to be present to decide if PV_AidingMode is OK.  
```cpp   
 /*ardupilot/libraries/AP_NavEKF2/AP_NavEKF2_Control.cppLine 171  
      in74c9c4a*/if (canUseGPS || canUseRangeBeacon) {  
```  
So the GPS health gets replaced by beacon and AID_ABSOLUTE stays armed when using beacon even when GPS is lost.  
```cpp   
 /*ardupilot/libraries/AP_NavEKF2/AP_NavEKF2_Control.cppLine 212  
      in74c9c4a*/bool posAiding = gpsPosUsed || rngBcnUsed;  
```  

## Comment3
### Comment author: tridge
### Comment Time: Dec 21, 2016
### Comment Content:
this is fixed in master, thanks to Paul