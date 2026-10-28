# Basic Information:
### Title: Rover/EKF: floating point exception if RNGFND_GNDCLEAR 0
### Issue status: Closed
### Author: rmackay9
### Issue open time: Feb 14, 2017
# Report
### Report author: rmackay9
### Report Time: Feb 14, 2017
### Report Content:
In rover we get a floating point exception in the EKF2 (or EKF3 I think) if the RNGFND_GNDCLEAR parameter is set to zero.  
To recreate the issue:  
- start APMRover2 in SITL.  ../Tools/autotest/sim_vehicle.py -D -G --map --console  
- param set RNGFND_GNDCLEAR 0  
- restart SITL  
- arm throttle  
- rc 3 1800  
After a few seconds this will appear.  It looks like the heightAboveGndEst is zero.  
    
Program received signal SIGFPE, Arithmetic exception.      
NavEKF2_core::EstimateTerrainOffset (this=0x77e320)      
at ../../libraries/AP_NavEKF2/AP_NavEKF2_OptFlowFusion.cpp:91      
91          float losRateSq = velHorizSq / sq(heightAboveGndEst);    

# Comment