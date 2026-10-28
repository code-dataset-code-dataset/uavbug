# Basic Information:
### Title: MISSION_CLEAR_ALL fails if last command in mission is RTL
### Issue status: Closed
### Author: DonLakeFlyer
### Issue open time: May 26, 2017
# Report
### Report author: DonLakeFlyer
### Report Time: May 26, 2017
### Report Content:
Issue details  
This was tested using latest ArduCopter RC and QGC daily build.  
- Create a mission which has a RETURN_TO_LAUNCH at the end of it. (You can do this from Mission Settings in QGC)  
- Fly the mission  
- Wait for the copter to come back, land and disarm  
- Now send a MISSION_CLEAR_ALL command to clear the mission from the vehicle (QGC will automatically prompt you for this)  
The MISSION_CLEAR_ALL fails with a MAV_MISSION_ERROR. The problem is in this code:  
    
```bash     
 bool AP_Mission::clear()    
{    
    // do not allow clearing the mission while it is running    
    if (_flags.state == MISSION_RUNNING) {    
        return false;    
    }    
```  
Even though the vehicle is on the ground and disarmed _flags.state == MISSION_RUNNING which seems wrong.
# Comment