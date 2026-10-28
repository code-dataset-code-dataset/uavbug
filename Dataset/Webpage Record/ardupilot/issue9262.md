# Basic Information:
### Title: increasing SCHED_LOOP_RATE causes mavlink messages to GCS to be sent too often
### Issue status: Closed
### Author: rmackay9
### Issue open time: Aug 23, 2018
# Report
### Report author: rmackay9
### Report Time: Aug 23, 2018
### Report Content:
If the SCHED_LOOP_RATE is increased (or perhaps decreased) from it's default value, this causes the mavlink messages to the GCS to arrive at a faster or slower rate than requested.  
To recreate the issue try doing this:  
- install Rover on a flight controller  
- connect with mission planner and on the Config/Tuning >> Planner page set the "Sensor" drop-down to 1  
- open the mavlink inspector window by going to the Flight Data screen, press Ctrl-F and press the "MAVLink In" button, expand Vehicle1/Comp1 and look for the update rate of the RAW_IMU message  
- increase SCHED_LOOP_RATE to 100 (from the default of 50) and reboot the flight controller  
- reconnect and double check that the Config/Tuning >> Planner page still has sensor set to 1h, if it's changed, change it back to 1  
- re-check the mavlink explorer and note the update rate is now 2hz!  

# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Aug 25, 2018
### Comment Content:
fixed in master and will go out with Rover-3.5