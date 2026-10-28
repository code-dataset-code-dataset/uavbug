# Basic Information:
### Title: Copter: Will not disarm in ALTH after autotune
### Issue status: Closed
### Author: sgofferj
### Issue open time: Jun 21, 2014
# Report
### Report author: sgofferj
### Report Time: Jun 21, 2014
### Report Content:
I did a few autotune rounds in the last few days and noticed a reproducible behavior which I would consider a bug.  
I did always the same thing:  
- Wait for "green light"  
- Switch to ALTH  
- Take off  
- Fly over safe area  
- Activate autotune  
- After autotune, return to takeoff position  
- Land  
- Try to disarm  
- After failure to disarm, switch to STAB  
- Disarm  
- Deactivate autotune  
The copter reproducibly did NOT follow the disarm command in ALTH! I had to switch to STAB to get it to disarm. It also wouldn't disarm itself (waited > 20s once before I lost my nerves and switch to STAB and disarmed manually).  
I would consider that a bug - unless it's intended behavior. But IMHO, it should be possible at any time in any mode to disarm a copter which sits on the ground.  
Logs: http://home.gofferje.net/copter/    
Drones-discuss: https://groups.google.com/forum/\\\#!topic/drones-discuss/smXNL_o0eFQ  
Note: That might be related to \\\#1159 . On drones-discuss, David Pawlak commented that he experienced the behavior described in \\\#1159 a few times and couldn't disarm the copter then.
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Jun 25, 2014
### Comment Content:
Thanks for the report.  I think this is because in AC3.2 autotune is a flight mode and we only allow disarming in AltHold, Loiter, Hybrid, Acro and Stabilize.  We probably need to add AutoTune to that list.
## Comment2
### Comment author: rmackay9
### Comment Time: Jul 06, 2014
### Comment Content:
Done by Jonathan, thanks!    
ff1f54b  
Note, this doesn't resolve the request above to allow disarming in any mode if the vehicle is on the ground.