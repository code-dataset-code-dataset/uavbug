# Basic Information:
### Title: Copter-3.6.0: skips 1st spline waypoint in SITL
### Issue status: Closed
### Author: rmackay9
### Issue open time: Oct 30, 2018
# Report
### Report author: rmackay9
### Report Time: Oct 30, 2018
### Report Content:
in SITL at least (and perhaps in a real vehicle although this hasn't been seen yet), the first Spline waypoint in a mission may be skipped.  To recreate the problem:  
1. start master or Copter-3.6 branch in SITL  
2. create a mission like below with a takeoff, a spline waypoint and a return-to-launch command    
3. type LOITER to switch to Loiter mode  
4. arm throttle (to arm the vehicle)  
5. rc 3 1100 (to raise throttle slightly)  
you should see that the vehicle climbs to takeoff altitude, the first spline waypoint command completes immediately and the vehicle begins the 2nd spline command.  
This issue does not happen in Copter-3.5.7.  
The issue appears related to this commit.
# Comment
## Comment1
### Comment author: arjun7965
### Comment Time: Oct 30, 2018
### Comment Content:
This seems to happen wherever the first Spline is(Skipped wp5). Just recreated this in SITL with:    

## Comment2
### Comment author: SwiftGust
### Comment Time: Nov 06, 2018
### Comment Content:
I think not just the commit the link @rmackay9 pointed, also spline time got issue too.    
This is SITL - Gazebo result with spline waypoint, it's not only skipping WP 2, also determines very earlier before reaching other WPs ( It turns out to be problem with fast_waypoint feature)    
Note WP6 is just straight WP, other WPs are spline    

## Comment3
### Comment author: SwiftGust
### Comment Time: Nov 06, 2018
### Comment Content:
@rmackay9 I made PR  \\\#9710 for the possible solution of this issue
## Comment4
### Comment author: rmackay9
### Comment Time: Mar 01, 2019
### Comment Content:
This is fixed in master and released with Copter-3.6.6.