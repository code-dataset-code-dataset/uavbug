# Basic Information:
### Title: Rover: skid-steering in reverse bug
### Issue status: Closed
### Author: khancyr
### Issue open time: Jan 30, 2017
# Report
### Report author: khancyr
### Report Time: Jan 30, 2017
### Report Content:
Issue details  
See http://discuss.ardupilot.org/t/skid-steering-in-reverse/14112/9  
Resume : in skid steering mod the rover can get stuck when use do_reverse  
Version  
To reproduce the bug on sitl, make a line of way point, put a do_reverse between to waypoint, launch the mission. The rover will get stuck on spot after the rotation. It also rightfully trigger a fs_crash !  
Platform  
[  ] All    
[  ] AntennaTracker    
[  ] Copter    
[  ] Plane    
[  ] Rover
# Comment
## Comment1
### Comment author: gmorph
### Comment Time: Feb 09, 2017
### Comment Content:
Confirmed this is broken in current master - not just the 3.1.1 release.
## Comment2
### Comment author: gmorph
### Comment Time: Nov 29, 2017
### Comment Content:
Is this still a bug?  The new master changes should of fixed this?
## Comment3
### Comment author: rmackay9
### Comment Time: Nov 29, 2017
### Comment Content:
It's better than before but I've still seen it get stuck.
## Comment4
### Comment author: rmackay9
### Comment Time: May 06, 2018
### Comment Content:
I think this is fixed in master so closing.