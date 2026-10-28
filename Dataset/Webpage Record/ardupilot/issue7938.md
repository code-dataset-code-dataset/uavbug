# Basic Information:
### Title: Copter-3.6-dev: RTL within Auto gets stuck if command's altitude is non-zero
### Issue status: Closed
### Author: rmackay9
### Issue open time: Mar 16, 2018
# Report
### Report author: rmackay9
### Report Time: Mar 16, 2018
### Report Content:
Copter (using latest/master/3.6-dev) and can get stuck in the initial climb stage of RTL if this is done:  
- create a mission with an RTL at the end with an altitude of 100  
- run the mission  
- the vehicle will climb to 100m (which I think is non-standard behaviour actually, I think it should ignore the lat/lon/alt of the command) and remain there forever.  

# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Mar 16, 2018
### Comment Content:
sorry, user error!  i was using mavproxy waypoint editor and somehow I set the last command as a waypoint instead of return-to-launch