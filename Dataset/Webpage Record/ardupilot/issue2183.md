# Basic Information:
### Title: AC3.3: home location is at EKF origin or last disarm location not arming location
### Issue status: Closed
### Author: rmackay9
### Issue open time: Apr 28, 2015
# Report
### Report author: rmackay9
### Report Time: Apr 28, 2015
### Report Content:
The EKF does not update it's position/location while disarmed.  This has the subtle effect of causing the ahrs-home location to be incorrect if the vehicle is moved while disarmed.  
This example shows the issue:  
1. put the copter at position A and let it warm up.  The EKF will capture it's origin and ahrs-home will be initially set to this EKF origin.  
2. move the copter 10m away  
3. arm the copter.  The copter will set the home position before arming so when asked, the EKF will return the origin location again  
This results in the home always being the last place that the copter disarmed, not it's current location at arming
# Comment
## Comment1
### Comment author: priseborough
### Comment Time: Apr 30, 2015
### Comment Content:
These patches that should fix this:  
priseborough@dc97e92    
priseborough@57d891d  
I have tested and the raw GPS position is now output pre-armed.
## Comment2
### Comment author: rmackay9
### Comment Time: May 02, 2015
### Comment Content:
Fixed in AC3.3-rc3