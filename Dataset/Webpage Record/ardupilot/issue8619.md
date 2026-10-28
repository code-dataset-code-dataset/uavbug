# Basic Information:
### Title: Rover: ignores DO_CHANGE_SPEED command if before first nav command
### Issue status: Closed
### Author: rmackay9
### Issue open time: Jun 11, 2018
# Report
### Report author: rmackay9
### Report Time: Jun 11, 2018
### Report Content:
To recreate the issue do this in SITL:  
- set WP_SPEED to 5 (m/s)  
- create a mission with at least two commands:    
- first command is DO_CHANGE_SPEED with 2nd column set to 2 (m/s)    
- second command is a waypoint some distance away    
- execute the mission, the vehicle will drive at 5m/s  
As a side note, it appears if the vehicle completes the mission at which point it switches to HOLD mode.  If the vehicle is put back into AUTO it will drive the mission at the specified speed.
# Comment
## Comment1
### Comment author: IamPete1
### Comment Time: Aug 30, 2021
### Comment Content:
closed by \\\#12772