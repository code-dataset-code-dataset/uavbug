# Basic Information:
### Title: Plane: Crash detected and plane disarmed on GPS loss while flying
### Issue status: Closed
### Author: Raviu8
### Issue open time: Sep 03, 2018
# Report
### Report author: Raviu8
### Report Time: Sep 03, 2018
### Report Content:
Bug report  
Issue details    
Hi,    
I had a bad crash Today where the plane got a GPS "no fix" for few moments and it suddenly got disarmed while still flying in air in Auto mission.    
I've reviewed telemetry logs and found that the plane sent "crash detected" when disarmed.  
Version    
3.9.1  
Platform    
[  ] All    
[  ] AntennaTracker    
[  ] Copter    
[x] Plane    
[  ] Rover    
[  ] Submarine  
Airframe type    
Fixed wing  
Hardware type    
Pixhawk1  
I could reproduce the bug many times using plane sitl and sitl with x-plane;  
Steps are so easily and reproducible for me every time.    
Steps to reproduce  
1. Start sitl whether normally or with xplane.  
2. enable crash_detect = 1  
3. Give the plane a mission, arm, then start Auto mode.    
-- I've modified the ins_ params to avoid the 3d accelerometer calibration needed not to disable arming checks.  
4. Allow it to takeoff and fly for a little then go to SIM_GPS_BYTELOSS and set it to 5  
5. Go back to Flight Data, it would show GPS no fix. In messages within few moments you'll get "crash detected" and the plane is throttle disarmed.  

# Comment
## Comment1
### Comment author: Raviu8
### Comment Time: Sep 03, 2018
### Comment Content:
I've tracked this down to line 26 in is_flying where airspeed_movement is always returned as false when GPS is lost.    
My plane had no airspeed sensor, so I've set arspd_type to 0.    
But on sitl I could reproduce the same buggy behavior with arspd_type is either 0 or 2.
## Comment2
### Comment author: magicrub
### Comment Time: Sep 04, 2018
### Comment Content:
Thanks for tracking this down!
## Comment3
### Comment author: tridge
### Comment Time: Sep 04, 2018
### Comment Content:
I have a PR to fix this here: \\\#9358
## Comment4
### Comment author: Raviu8
### Comment Time: Sep 05, 2018
### Comment Content:
@tridge Using your PR; I could reproduce another false "crash detected" but no "disarm" - actually I don't know why it doesn't disarm?? -;    
Steps to reproduce  
1.     
Start sitl whether normally or with xplane.    
2.     
enable crash_detect = 1    
3.     
Give the plane a mission, arm, then start Auto mode.    
4.     
Allow it to takeoff and fly for a little then go to SIM_GPS_BYTELOSS and set it to 4 - almost 80% loss -      
Then allow it to fly a little then set SIM_GPS_BYTELOSS to 50 - complete loss -    
5.     
Go back to Flight Data -> messages within few moments you'll get "crash detected" but "no disarm ?"    
6.     
Actually if you set the SIM_GPS_BYTELOSS back to 0 it would accomplish the mission as if nothing happened.    

## Comment5
### Comment author: Raviu8
### Comment Time: Sep 05, 2018
### Comment Content:
I found that the "no disarm" was related to using arming_require = 0. I think this behavior was changed recently on master? As I recall well it was disarming on crash detection with "arming_require = 0".    
So when set to 1 , it disarms. I think it should always disarm in crash detection whatever the arming_require is.
## Comment6
### Comment author: tridge
### Comment Time: Sep 05, 2018
### Comment Content:
@magicrub what do you think? I'm tempted to just disable crash detection if we don't have GPS lock and also don't have working airspeed. Really at that point we have no reliable way to know if we've crashed or not.
## Comment7
### Comment author: tridge
### Comment Time: Sep 05, 2018
### Comment Content:
I've added a patch to implement the "no crash if no GPS and no airspeed" approach
## Comment8
### Comment author: Raviu8
### Comment Time: Sep 06, 2018
### Comment Content:
In simulator it seems fine now, with and without airspeed sensor.    
But what about the "no disarm" with "arming_require = 0" when crash is detected?
## Comment9
### Comment author: Raviu8
### Comment Time: Sep 07, 2018
### Comment Content:
I've done two real flight tests Today using PR \\\#9366 .. To test both crash detection and dead reckoning.    
It was too windy that helped find another crash detection bug.    
I've activated a GPS disable switch, also added a switch for a video transmitter which is proved to work like a GPS jammer. I've tested the later before flight and number of SATs drops from 16 to less than 7 with random movements that prevents arming.    
No air speed was used, and arspd_type was 0.  
Here are the results;  
1. Dead reckoning works fine, I think. Much better with GPS disabled, less effective with GPS jamming activated.    
Tested with Auto and RTL. RTL was astonishing for me as the plane almost flew back to home by side due to relatively powerful wind.  
2. Another false crash detection occurred when the plane was flying into wind with good estimated AS as displayed in MissionPlanner, but very low GS. Then I turned on the disable-GPS switch, and instantly it showed "no fix", detected a crash and disarmed displaying AS of 0 and GS was too much lower than stall speed as mentioned.  
By the way, in my previous attempts to debug the crash detector issue, I've tried some different conditions like the one you added in commit a536760 and it usually crashed, maybe the GPS status is not updated quickly enough here. Also if GPS regained a good fix for few milliseconds the condition is usually bypassed too and it detected a crash.
## Comment10
### Comment author: tridge
### Comment Time: Sep 07, 2018
### Comment Content:
@Raviu8 do you have a log of the false crash detection cases you just found?
## Comment11
### Comment author: Raviu8
### Comment Time: Sep 08, 2018
### Comment Content:
@tridge I could reproduce the same buggy behavior using sitl multiple times;  
1. Draw a mission that goes from East to West for a distance of 7 km at 600m rel. alt. for example.  
2. Set fbw min to 15 m/s, set arspd_type = 0, crash_detect = 1  
3. Set sim_wind_speed to 11.5 m/s and sim_wind_dir to 260 degrees - so as the plane is flying into wind.  
4. Arm, start Auto, and allow plane to achieve required alt., It should have ground speed around 4 to 5 m/s  
5. Set SIM_GPS_BYTELOSS to 5 within few seconds you'd get a crash detect and it'll disarm.  
I'm using your PR \\\#9366 and cherry-picked commit a536760 into it.
## Comment12
### Comment author: Raviu8
### Comment Time: Sep 09, 2018
### Comment Content:
Here are SITL logs showing "crash detected" bug mentioned in latest comment;    
https://mega.nz/\\\#F!LPpAXCwI!TNeBMv_gBE8kHfkMPZLJsQ  
Also folder includes a bin log for a Floating Exception Error that caused SITL crash too.
## Comment13
### Comment author: Raviu8
### Comment Time: Sep 09, 2018
### Comment Content:
@tridge I think I've found something;    
I've made a small change on top on your PR; added a debouncer in case of GPS "no fix".    
I've gradually increased the debounce times, trying each time to reproduce the bug, actually I could reproduce it up to almost 14 times (2 seconds) so I've set it finally to 21 (almost 3 seconds) when I finally could not see a "crash detected" any more on GPS loss.  
I do not know if this patch is a real solution, but I hope it points to one.  
gps_crash_debounce.patch.txt  
    
```bash     
 diff --git a/ArduPlane/is_flying.cpp b/ArduPlane/is_flying.cpp    
index 8e7121375..d86e9db38 100644    
--- a/ArduPlane/is_flying.cpp    
+++ b/ArduPlane/is_flying.cpp    
@@ -207,6 +207,7 @@ void Plane::crash_detection_update(void)    
     bool crashed = false;    
     bool been_auto_flying = (auto_state.started_flying_in_auto_ms > 0) &&    
                             (now_ms - auto_state.started_flying_in_auto_ms >= 2500);    
+    static int8_t gps_fix_debounce;    
     
     if (!is_flying() && arming.is_armed())    
     {    
@@ -278,9 +279,15 @@ void Plane::crash_detection_update(void)    
         crash_state.checkedHardLanding = false;    
     }    
     
+    if (gps_fix_debounce > 0){    
+        gps_fix_debounce--;    
+        crashed = false;    
+    }    
+    
     // if we have no GPS lock and we don't have a functional airspeed    
     // sensor then don't do crash detection    
     if (gps.status() < AP_GPS::GPS_OK_FIX_3D && (!airspeed.use() || !airspeed.healthy())) {    
+        if (gps_fix_debounce < 21) {gps_fix_debounce = 21;}    
         crashed = false;    
     }    
     
```
## Comment14
### Comment author: amilcarlucas
### Comment Time: Sep 10, 2018
### Comment Content:
21 seams to be a magic number. Does it have to do with 5Hz GPS? What happens with a 10Hz GPS ?
## Comment15
### Comment author: Raviu8
### Comment Time: Sep 10, 2018
### Comment Content:
Actually, 21 means 4.2 seconds. As crash_detection_update is called update_is_flying_5Hz , so it's 5Hz, I thought it was 7Hz.    
It's 5Hz on SITL as GPS_RATE_MS is 200 by default.
## Comment16
### Comment author: amilcarlucas
### Comment Time: Sep 10, 2018
### Comment Content:
I fly with a Septentrio AsteRX GPS at GPS_RATE_MS 100. Other people do that as well.    
IMHO you should replace 21 with (4.2*1000/GPS_RATE_MS)  
or, if it is coupled with update_is_flying then (4.2*update_is_flying_rate)
## Comment17
### Comment author: Raviu8
### Comment Time: Sep 10, 2018
### Comment Content:
@amilcarlucas    
is_flying update rate is constant so 21 is always 4.2 seconds.    
But GPS update is not well synchronized. I'll change GPS rate to 100 ms and do more testing.
## Comment18
### Comment author: Raviu8
### Comment Time: Sep 10, 2018
### Comment Content:
I've done some more testing, I think a value of 16 is fine with both 5Hz and 10Hz GPS.    
So it's up to @tridge now to make decision.
## Comment19
### Comment author: Raviu8
### Comment Time: Sep 10, 2018
### Comment Content:
I've also simulated a case using xplane - with my patch at 16 bounces - where I got the plane to physically crash on ground while GPS was disabled then re-enabled it after it actually crashed, within few seconds - less than 4 seconds after enabling GPS, it detected a crash and disarmed - as required.  
Also tested the same with arspd_type = 2 and then with also arspd_use = 1.    
Setting arspd_use =1 allowed good crash detection without GPS.  
So the idea is working fine, I think.
## Comment20
### Comment author: WickedShell
### Comment Time: Sep 10, 2018
### Comment Content:
    
I fly with a Septentrio AsteRX GPS at GPS_RATE_MS 100    
GPS_RATE_MS has no effect on a Septentrio GPS, and the code cannot make any assumptions that it corresponds to what the GPS is providing. That is strictly a u-blox parameter at this time, and any usage outside of the u-blox driver is wrong.
## Comment21
### Comment author: magicrub
### Comment Time: Sep 11, 2018
### Comment Content:
Hey guys, I'll take a look at this soon
## Comment22
### Comment author: amilcarlucas
### Comment Time: Sep 11, 2018
### Comment Content:
@WickedShell thanks for clarifying that. That info should be added to the wiki. (or to the parameter description)
## Comment23
### Comment author: Raviu8
### Comment Time: Sep 17, 2018
### Comment Content:
Any updates on this?    
I've done real flight tests with my patch and it seems working as expected.
## Comment24
### Comment author: Raviu8
### Comment Time: Oct 26, 2018
### Comment Content:
@tridge @magicrub Long time no updates?
## Comment25
### Comment author: tridge
### Comment Time: Nov 28, 2018
### Comment Content:
we believe this is all fixed now (thanks Tom!)    
please re-test though