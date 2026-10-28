# Basic Information:
### Title: Copter: Sonar Enabled/Disable is not refreshed upon start/reset of APM
### Issue status: Closed
### Author: TimGFoley
### Issue open time: Aug 14, 2013
# Report
### Report author: TimGFoley
### Report Time: Aug 14, 2013
### Report Content:
Testing Sonar with an XL-MB1240, conditions.  Found that the APM upon power up is not refreshing the Sonar enable/disable param if a radio channel is used to control it.  
Steps to reproduce:  
1. Sonar enable/disable parameter set to 1 (Enable)  
2. Assign channel (CH8) to turn Sonar off and on  
3. Leave Radio Switch in Disable position (Sonar Off)  
4. Power up APM  
5. Read Params, will see that Sonar is 1 (Enabled) where it should be disabled.  
6. Toggle Ch8 back and forth on radio, refresh params and it will now properly follow the CH8 setting.  

# Comment
## Comment1
### Comment author: rmackay9
### Comment Time: Aug 28, 2013
### Comment Content:
This is fixed in master, so it will go out with AC3.1.  Feel free to double check the release candidate when it goes out which should be within 1 week.