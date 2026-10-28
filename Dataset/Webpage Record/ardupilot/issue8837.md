# Basic Information:
### Title: Rover: check/fix Vectored Thrust steering direction with reverse throttle
### Issue status: Closed
### Author: rmackay9
### Issue open time: Jul 06, 2018
# Report
### Report author: rmackay9
### Report Time: Jul 06, 2018
### Report Content:
The Vectored Thrust feature (wiki) scales the steering output based on the throttle.  I.e. steering is reduced as throttle is increased.  
In Rover-3.4.1 the steering direction may be backwards however when reversing so we should confirm there is a bug and then fix the problem.  
We could test the issue in a real vehicle or in the simulator:  
- arm the vehicle and switch to ACRO mode  
- face the vehicle downstream in a strong current  
- monitor the vehicle's output throttle, it should go negative in order to try and maintain a zero velocity  
- if there is a bug the vehicle's heading will change wildly, it may even turn around and point upstream.  
The implementation of Vectored Thrust can be found here in the AP_MotorsUGV library.  I think we do have a bug and it can be fixed by adding the lines below to the, "if (have_vectored_thrust()) {" section:  
    
```bash     
 // reverse steering direction when backing up    
if (is_negative(throttle)) {    
    steering *= -1.0f;    
 }    
```  
The discussion that prompted this issue is at the bottom of this discussion.  In particular at one point in the mission the vehicle did a small loop.  The other possible cause of the little loop is the steering controller thought the throttle was in reverse but the vehicle doesn't actually support reversing the motors so we may instead need to create an issue to add better support for vehicles that cannot reverse.
# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Jul 14, 2021
### Comment Content:
In 4.1 we've reworked the vectored thrust support and I think we've resolved any issues that were there before.