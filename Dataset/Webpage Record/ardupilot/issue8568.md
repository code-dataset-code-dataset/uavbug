# Basic Information:
### Title: Rover: do-reverse persists when mission is restarted
### Issue status: Closed
### Author: rmackay9
### Issue open time: Jun 03, 2018
# Report
### Report author: rmackay9
### Report Time: Jun 03, 2018
### Report Content:
If the previous mission ended with the vehicle moving in reverse (because of a DO_SET_REVERSE mission command) then the next time the mission is run, it will begin in reverse.  
To reproduce the issue:  
- create a rover mission with a do-set-reverse (with 1 as the first field) command in it.  
- run the mission  
- remove to do-set-reverse from the mission  
- run the mission again, it will run in reverse (which is incorrect).  
The cause of the issue is the mode.h file's ModeAuto::_reversed parameter is not reset to false.  The simplest solution is probably just to add a call to set_reversed(false) in mode_auto.cpp's enter() method.  The only downside of this simple solution is that if the mission is restarted without leaving auto, which is possible using a mavlink command I think, the reverse setting will remain.  
This issue was reported in this Rover discussion.
# Comment
## Comment1
### Comment author: WickedShell
### Comment Time: Jun 03, 2018
### Comment Content:
You also might resume a mission while you were in a reversed segment, and automatically setting reversed to false is probably not good for that situation either, as now the vehicle is very much off the mission profile.
## Comment2
### Comment author: WickedShell
### Comment Time: Jun 03, 2018
### Comment Content:
Also worth noting this class of issues applies to all the vehicles for any of the do set speed commands and similar.
## Comment3
### Comment author: rmackay9
### Comment Time: Aug 22, 2018
### Comment Content:
This is resolved in master and will go out with Rover-3.5.