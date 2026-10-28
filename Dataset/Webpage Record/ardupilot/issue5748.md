# Basic Information:
### Title: Unable to connect to SITL with virtual gimbal on Windows
### Issue status: Closed
### Author: kshahar
### Issue open time: Feb 17, 2017
# Report
### Report author: kshahar
### Report Time: Feb 17, 2017
### Report Content:
Issue details  
When starting SITL on Windows (Cygwin) with the --gimbal option, the application does not accept connections on TCP port 5760.  
To reproduce on Windows simply run the following and try some commands in MAVProxy:    
$ sim_vehicle.py --model quad --mavlink-gimbal  
netstat output:  
    
```bash     
 C:\> netstat -an | find "576"    
  TCP    0.0.0.0:5760           0.0.0.0:0              LISTENING    
  TCP    127.0.0.1:5760         127.0.0.1:62869        ESTABLISHED    
  TCP    127.0.0.1:62869        127.0.0.1:5760         ESTABLISHED    
  TCP    127.0.0.1:62870        127.0.0.1:5762         SYN_SENT    
```  
Also, the following piece of code (taken from SIM_ADSB.cpp) seems to resolve this issue:  
    
```bash     
 void Gimbal::send_report(void)    
{    
    if (AP_HAL::millis() < 10000) {    
        // simulated aircraft don't appear until 10s after startup. This avoids a windows    
        // threading issue with non-blocking sockets and the initial wait on uartA    
        return;    
    }    
```  
Version  
Tested with Copter 3.4.4 on Windows 10 / Cygwin.  
    
```bash     
 $ uname -srv    
CYGWIN_NT-10.0-WOW 2.6.1(0.305/5/3) 2016-12-16 11:50    
```  
Platform  
[  ] All    
[  ] AntennaTracker    
[*] Copter    
[  ] Plane    
[  ] Rover  
Logs  
ArduCopter.log:  
    
```bash     
 Started model quad at -35.363261,149.165230,584,353 at speed 1.0    
Starting sketch 'ArduCopter'    
Starting SITL input    
bind port 5760 for 0    
Serial port 0 on TCP port 5760    
Waiting for connection ....    
Smoothing reset at 0.001    
```
# Comment
## Comment1
### Comment author: OXINARF
### Comment Time: Feb 18, 2017
### Comment Content:
Since you already figured out what is needed to fix it, it don't you want to open a PR with it? In any case, thank you for the report!
## Comment2
### Comment author: OXINARF
### Comment Time: Mar 17, 2017
### Comment Content:
Fixed with \\\#5879