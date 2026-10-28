# Basic Information:
### Title: Copter: AC3.5-dev - EKF never resets to GPS position after glitch
### Issue status: Closed
### Author: rmackay9
### Issue open time: Mar 04, 2017
# Report
### Report author: rmackay9
### Report Time: Mar 04, 2017
### Report Content:
During testing of master I've found it's possible to make the EKF maintain an offset after a GPS glitch occurs by doing this in the simulator:  
- map set showgpspos 1  (to make the raw gps position visible as the blue vehicle)  
- param set SIM_GPS_GLITCH_Y 0  
- loiter, arm throttle, rc 3 1800, rc 2 1400 (to get the vehicle gently flying forward)  
- param set SIM_GPS_GLITCH_Y 0.002  
In AC3.4 the blue vehicle would jump to the right and a few seconds later the red vehicle (the EKF estimate) would reset to the GPS position.  In AC3.5 however the reset never happens so the two vehicles appear to be flying next to each other.  
This problem does not occur in AC3.4.5 (the official release) so this only affects developers and beta testers.
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Mar 04, 2017
### Comment Content:
Note: this only affects the horizontal reset, the vertical reset (if using EK2_ALT_SOURCE=2/GPS) works.
## Comment2
### Comment author: WickedShell
### Comment Time: Mar 04, 2017
### Comment Content:
Oh good, was getting really worried about that part actually! Thanks for    
the update!  
…    
On Sat, Mar 4, 2017 at 12:46 AM, Randy Mackay ***@***.***> wrote:      
 Note: this only affects the horizontal reset, the vertical reset (if using      
 EK2_ALT_SOURCE=2/GPS) works.      
 —      
 You are receiving this because you are subscribed to this thread.      
 Reply to this email directly, view it on GitHub      
 <\\\\#5813 (comment)>,      
 or mute the thread      
 <https://github.com/notifications/unsubscribe-auth/AAipiFvnXfAGysW_k6rI7p540i_IqFvIks5riRbGgaJpZM4MTArG>      
 .      

## Comment3
### Comment author: priseborough
### Comment Time: Mar 04, 2017
### Comment Content:
I found it - when the reset logic was reworked to include the range beacon, the unintended result was that a position reset would not occur if GPS velocity observations were still being accepted. This didn't show up with my tests using replay logs because realistic glitches and IMU errors always caused the GPS velocity to be rejected as well as the position.  
The intended result was that without GPS velocity rejection, a reset would occur after 5 seconds or 10 seconds if GPs velocity was being fused.  
Fixed by \\\#5816
## Comment4
### Comment author: rmackay9
### Comment Time: Mar 06, 2017
### Comment Content:
This is fixed in master now.  Thanks @priseborough