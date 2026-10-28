# Basic Information:
### Title: Copter: failover from GPS to optical flow results in EKF failsafe triggering
### Issue status: Closed
### Author: rmackay9
### Issue open time: Nov 28, 2018
# Report
### Report author: rmackay9
### Report Time: Nov 28, 2018
### Report Content:
The EKF can fuse both GPS and optical flow data at the same time (I think) but it doesn't seem possible in practice to failover from GPS+opticalflow to just optical flow.  
To recreate this do the following:  
- follow SITL advanced testing instructions for setting up optical flow and range finder in SITL.  
- restart SITL and there should be messages like, "EKF2 IMU0 is using GPS" and "EKF2 IMU0 is using optical  flow" meaning that both GPS and optical flow are being used  
- set ARMING_CHECK = 0 to disable the range finder checks when using optical flow  
- take-off in Loiter and fly around a bit.  
- disable the GPS by setting GPS_TYPE = 0  
- an EKF failsafe will trigger and the vehicle will switch to LAND mode  
In fact, the EKF is able to estimate it's position and keep the vehicle flying and this can be shown to be true by repeating the above test but first set FS_EKF_THRESH = 0 to disable the EKF failsafe.  Now you will find that the vehicle remains in Loiter and holds position.  Sadly we cannot switch the vehicle into RTL though.  
I think the best behaviour would be:  
- the EKF failsafe does not trigger a LAND because the vehicle is still controllable.  
- the user should be able to switch to other flight modes like RTL  
- it should be possible to trigger an EKF failsafe if the optical flow is also disabled.  
- perhaps a warning should be sent to the user that the vehicle is only using Optical flow?  

# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Dec 21, 2018
### Comment Content:
It may be that this only works when using EKF3 so we should test failover using EKF3.
## Comment2
### Comment author: EosBandi
### Comment Time: Dec 29, 2018
### Comment Content:
Randy, this is exactly what I was testing with GPS jamming and spoofing detection. To make such detection work in an automated manner instead of giving only a warning, a capability to fail-over to optical flow is needed. DO you think that RTL could work with only relative positioning (optical flow) ?
## Comment3
### Comment author: EosBandi
### Comment Time: Feb 13, 2019
### Comment Content:
@rmackay9 Unfortunately mending with the internals of EKF is above my head, but if you could give some pointers perhaps i can start working on this.
## Comment4
### Comment author: rmackay9
### Comment Time: Feb 15, 2019
### Comment Content:
I think it might be good to re-test this issue using EKF3.  It may not be an issue with EKF3.
## Comment5
### Comment author: rmackay9
### Comment Time: Feb 06, 2020
### Comment Content:
I'm going to close this issue because I've tested this with EKF3 and it doesn't trigger the EKF failsafe.  It seems to handle the failback much worse than the EKF2 now does (see above PR) but this is a different issue.