# Basic Information:
### Title: Compiler Error in Plane master
### Issue status: Closed
### Author: priseborough
### Issue open time: Dec 06, 2016
# Report
### Report author: priseborough
### Report Time: Dec 06, 2016
### Report Content:
Issue details  
Commit 8d87751 appears to be causing a compiler error.  
I used the following build  sequence:  
git fetch origin    
git checkout master    
git reset --hard origin/master    
git submodule update --init --recursive    
./waf clean    
./waf configure --board px4-v2    
./waf --targets bin/arduplane --upload  
And got the following error:  
../../libraries/AP_Landing/AP_Landing.cpp: In member function 'void AP_Landing::setup_landing_glide_slope(const Location&, const Location&, const Location&, int32_t&)':    
../../libraries/AP_Landing/AP_Landing.cpp:190:36: error: qualified-id in declaration before '(' token    
void AP_Landing::init_start_nav_cmd(void)    
^  
Version  
master  
Platform  
[  ] All    
[  ] AntennaTracker    
[  ] Copter    
[x] Plane    
[  ] Rover  
Airframe type  
N/A  
Hardware type  
px4-v2  
Logs  
N/A
# Comment
## Comment1
### Comment author: tridge
### Comment Time: Dec 06, 2016
### Comment Content:
fixed in master by reverting 2 patches
## Comment2
### Comment author: magicrub
### Comment Time: Dec 06, 2016
### Comment Content:
Doh! Thanks for the quick fix, Tridge. Sorry about that everyone!  
…    
On Dec 5, 2016 11:09 PM, "Randy Mackay" ***@***.***> wrote:      
 Closed \\\\#5337 <\\\\#5337>.      
 —      
 You are receiving this because you were assigned.      
 Reply to this email directly, view it on GitHub      
 <\\\\#5337 (comment)>, or mute      
 the thread      
 <https://github.com/notifications/unsubscribe-auth/AEj7G26l98aj0LGTbaGbT8rW-HMznVAxks5rFQojgaJpZM4LFEBl>      
 .      
