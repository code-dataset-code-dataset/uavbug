# Basic Information:
### Title: mission index should reset on mission update
### Issue status: Closed
### Author: magicrub
### Issue open time: Jun 23, 2015
# Report
### Report author: magicrub
### Report Time: Jun 23, 2015
### Report Content:
When uploading a new mission while in auto the current mission cmd stays in RAM and continues to execute. With MISSION_RESTART=0, if you switch to manual then back to auto you will continue executing the RAM mission, not the new mission in flash. To execute the new mission you must reset mission index to 1.  
This may seem obvious but consider this scenario:  
- boot /w some unknown previously uploaded mission.  
- switch to auto  
- switch back to manual  
- upload new mission  
- switch to auto and launch.  
You had stayed on mission cmd index=1 the whole time. You will launch with the old mission cmd 1 instead of your new mission cmd 1.  
On a mission upload, reset index to 1 will solve this problem
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Jun 23, 2015
### Comment Content:
Sounds like we have a bit of a problem.    
I guess we need to be careful that when we fix this that the uploading of partial missions still works ok.  So for example if the user uploads waypoints that haven't been run yet.. we wouldn't want to interrupt the mission.
## Comment2
### Comment author: magicrub
### Comment Time: Jun 23, 2015
### Comment Content:
I already do detection of full mission updates when I dump the new mission    
to DF, the same mechanism could trigger a mission restart.  
I had done a half-fix to test this by adding logic in the reset-or-resume    
function to reset if the current index was 1. That fixes my particular    
problem but it is not a very good general solution. The above solution is    
better.    
On Jun 22, 2015 7:54 PM, "Randy Mackay" notifications@github.com wrote:  
    
Sounds like we have a bit of a problem.      
I guess we need to be careful that when we fix this that the uploading of      
partial missions still works ok. So for example if the user uploads      
waypoints that haven't been run yet.. we wouldn't want to interrupt the      
mission.    
—      
Reply to this email directly or view it on GitHub      
\\\\#2445 (comment)      
.    

## Comment3
### Comment author: magicrub
### Comment Time: Jun 23, 2015
### Comment Content:
After talking it over with @tridge , @rmackay9  we think a reset of the current mission item if ok only when not currently executing it. That is, when switching from non-AUTO to AUTO you should always clear the cached copy and update it with the mission item in flash memory.
## Comment4
### Comment author: magicrub
### Comment Time: Jun 23, 2015
### Comment Content:
fixed via \\\#2448