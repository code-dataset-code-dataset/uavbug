# Basic Information:
### Title: Copter: support do-set-home mission command
### Issue status: Closed
### Author: rmackay9
### Issue open time: Dec 09, 2014
# Report
### Report author: rmackay9
### Report Time: Dec 09, 2014
### Report Content:
There seem to be some issues in the handling of the do-set-home mission command.  
To reproduce the issue try this:  
1. create a mission with a do-set-home command with zero lat, lon and alt followed by a waypoint.  
2. when the do-set-home command executes, EKF produces a very large position variance which leads to the AHRS switching back and forth between DCM and EKF  
3. the large position variance leads to an arithmetic exception in the dataflash logging of EKF as it tries to squeeze the variance into an int16_t.  
4. the vehicle tries to fly off to a location that seems to be the waypoint target location plus the offset from the original home to the new home  
Issue reported in the APM forum:    
http://ardupilot.com/forum/viewtopic.php?f=100&t=10587
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Dec 09, 2014
### Comment Content:
I've moved this item to the AC3.2.1 milestone so that we remember to do something about it.  The minimum we should do is reject the command so that it doesn't cause problems.  Apparently in the issue reported above the motor outputs logged became the same for all channels (ch1 ~ ch4) and the vehicle crashed so perhaps the arithmetic errors propagated through the system.
## Comment2
### Comment author: R-Lefebvre
### Comment Time: Dec 17, 2014
### Comment Content:
This happened again:  
http://ardupilot.com/forum/viewtopic.php?f=100&t=10676&p=26845\\\#p26845  
This one seems to be slightly different as the motors do not lock up.
## Comment3
### Comment author: rmackay9
### Comment Time: Dec 26, 2014
### Comment Content:
I've pushed in a change to simply remove support for the do-set-home mission command for AC3.2.1 so I've moved the larger issue (add proper support) to AC3.3..
## Comment4
### Comment author: rmackay9
### Comment Time: Feb 12, 2015
### Comment Content:
support for the do-set-home command (both as a mission command and as an immediate command from the GCS) are in master now and will go out with AC3.3.