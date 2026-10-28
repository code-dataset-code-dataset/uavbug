# Basic Information:
### Title: Plane: decrement waypoint index when switching away from AUTO during landing
### Issue status: Closed
### Author: magicrub
### Issue open time: May 07, 2015
# Report
### Report author: magicrub
### Report Time: May 07, 2015
### Report Content:
Consider the following scenario:  
- performing autoland  
- abort the landing by switching from AUTO to any other flight mode. Lets say we went to STABILIZE  
- manually gain altitude, switch back to AUTO to land again  
- Plane is now flying auto and:  
- - has heavily constrained roll angle  
- - dropping altitude via glide slope from an unplanned altitude (at wherever you resumed AUTO)  
- - unplanned heading while traveling towards land point while dropping altitude, effectively landing from the wrong direction if we are too low  
new proposed behavior:    
When switching away from AUTO while executing a LAND mission item, decrement the waypoint index so that when AUTO is resumed the proper altitude and position is reached before restarting the glide slope.
# Comment
## Comment1
### Comment author: magicrub
### Comment Time: May 12, 2015
### Comment Content:
is currently a pending PR \\\#2269