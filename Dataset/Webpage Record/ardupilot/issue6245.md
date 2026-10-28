# Basic Information:
### Title: Crash on Quadplane Simulation
### Issue status: Closed
### Author: RMIShane
### Issue open time: May 15, 2017
# Report
### Report author: RMIShane
### Report Time: May 15, 2017
### Report Content:
Issue details  
I'm using Vagrant SITL to do quadplane simulation.  
Launching with this command:    
sim_vehicle.py -L KSFO -j 2 -v ArduPlane -f quadplane  
then uploading an auto mission:    
wp load ../Tools/autotest/ArduPlane-Missions/KSFO-VTOL.txt  
then:    
arm throttle  
then:    
auto  
At this point the simulation crashes.  
    
```bash     
 auto    
FBWA> APM: Executing nav command ID \\#84    
APM: Resetting previous waypoint    
Got MAVLink msg: COMMAND_ACK {command : 11, result : 0}    
APM: Reset alt target to -12.6    
waypoint 1    
/vagrant/Tools/autotest/run_in_terminal_window.sh: line 54: 27548 Aborted                 (core dumped) $cmd $* &> "$filename" < /dev/null    
```  
Version  
ArduPlane 3.8beta5    
(git Tag ArduPlane-beta)  
Logs  
    
```bash     
 Started model quadplane at 37.619373,-122.376637,5.3,118 at speed 1.0    
Starting sketch 'ArduPlane'    
Starting SITL input    
Using Irlock at port : 9005    
bind port 5760 for 0    
Serial port 0 on TCP port 5760    
Waiting for connection ....    
Loaded defaults from /vagrant/Tools/autotest/default_params/quadplane.parm    
bind port 5762 for 2    
Serial port 2 on TCP port 5762    
bind port 5763 for 3    
Serial port 3 on TCP port 5763    
Smoothing reset at 0.001    
Loaded defaults from /vagrant/Tools/autotest/default_params/quadplane.parm    
ERROR: Floating point exception - aborting    
```
# Comment
## Comment1
### Comment author: peterbarker
### Comment Time: May 16, 2017
### Comment Content:
On Sun, 14 May 2017, RMIShane wrote:    
I'm unable to replicate.  
 ArduPlane 3.8beta5    
 (git Tag ArduPlane-beta)  
Please provide a specific git hash.  
 ERROR: Floating point exception - aborting  
That's very bad.
## Comment2
### Comment author: RMIShane
### Comment Time: May 16, 2017
### Comment Content:
commit 92d5055    
Pulled everything again today and still having the same issue.    
(seams to just crash with quadplane)    
following these steps:    
1. vagrant ssh -c "sim_vehicle.py -L KSFO -j 2 -v ArduPlane -f quadplane    
--console --map"    
2. wp load ../Tools/autotest/ArduPlane-Missions/KSFO-VTOL.txt    
3. arm throttle    
4. AUTO    
[image: Inline image 1]    
On Mon, May 15, 2017 at 11:25 PM, Peter Barker <notifications@github.com>    
wrote:  
…    
 On Sun, 14 May 2017, RMIShane wrote:      
 I'm unable to replicate.      
 > ArduPlane 3.8beta5      
 > (git Tag ArduPlane-beta)      
 Please provide a specific git hash.      
 > ERROR: Floating point exception - aborting      
 That's very bad.      
 —      
 You are receiving this because you authored the thread.      
 Reply to this email directly, view it on GitHub      
 <\\\\#6245 (comment)>,      
 or mute the thread      
 <https://github.com/notifications/unsubscribe-auth/AbXHWsO7nHxOVAknvsLwly1dO6bIOXcgks5r6RcZgaJpZM4NaswV>      
 .      

## Comment3
### Comment author: RMIShane
### Comment Time: May 16, 2017
### Comment Content:
Got MAVLink msg: MISSION_ACK {target_system : 255, target_component : 0,    
type :              0, mission_type : 0}    
APM: Flight plan received    
arm throttle    
FBWA> APM: Throttle armed    
Got MAVLink msg: COMMAND_ACK {command : 400, result : 0}    
ARMED    
auto    
FBWA> APM: Executing nav command ID \\\#84    
APM: Resetting previous waypoint    
Got MAVLink msg: COMMAND_ACK {command : 11, result : 0}    
APM: Reset alt target to 16.8    
waypoint 1    
/vagrant/Tools/autotest/run_in_terminal_window.sh: line 54: 26969 Aborted    
                           (core dumped) $cmd $* &> "$filename" < /dev/null    
FBWA> no link    
link 1 down    
no link    
no link    
no link    
no link  
…    
On Tue, May 16, 2017 at 12:03 AM, Shane Roberts ***@***.***> wrote:      
 commit 92d5055      
 Pulled everything again today and still having the same issue.      
 (seams to just crash with quadplane)      
 following these steps:      
 1. vagrant ssh -c "sim_vehicle.py -L KSFO -j 2 -v ArduPlane -f quadplane      
 --console --map"      
 2. wp load ../Tools/autotest/ArduPlane-Missions/KSFO-VTOL.txt      
 3. arm throttle      
 4. AUTO      
 [image: Inline image 1]      
 On Mon, May 15, 2017 at 11:25 PM, Peter Barker ***@***.***>      
 wrote:      
> On Sun, 14 May 2017, RMIShane wrote:      
>      
> I'm unable to replicate.      
>      
> > ArduPlane 3.8beta5      
> > (git Tag ArduPlane-beta)      
>      
> Please provide a specific git hash.      
>      
> > ERROR: Floating point exception - aborting      
>      
> That's very bad.      
>      
> —      
> You are receiving this because you authored the thread.      
> Reply to this email directly, view it on GitHub      
> <\\\\#6245 (comment)>,      
> or mute the thread      
> <https://github.com/notifications/unsubscribe-auth/AbXHWsO7nHxOVAknvsLwly1dO6bIOXcgks5r6RcZgaJpZM4NaswV>      
> .      
>      

## Comment4
### Comment author: peterbarker
### Comment Time: May 16, 2017
### Comment Content:
On Mon, 15 May 2017, RMIShane wrote:    
 commit 92d5055    
 Pulled everything again today and still having the same issue.    
 (seams to just crash with quadplane)    
 following these steps:    
 1. vagrant ssh -c "sim_vehicle.py -L KSFO -j 2 -v ArduPlane -f quadplane    
 --console --map"    
 2. wp load ../Tools/autotest/ArduPlane-Missions/KSFO-VTOL.txt    
 3. arm throttle    
 4. AUTO  
Replicated, thanks!  Any time someone can replicate something in the    
vagrant VM makes me happy.
## Comment5
### Comment author: peterbarker
### Comment Time: May 16, 2017
### Comment Content:
    
```bash     
 Program received signal SIGFPE, Arithmetic exception.    
__ieee754_expf_sse2 () at ../sysdeps/i386/i686/fpu/multiarch/e_expf-sse2.S:116    
116     ../sysdeps/i386/i686/fpu/multiarch/e_expf-sse2.S: No such file or directory.    
(gdb) bt    
\\#0  __ieee754_expf_sse2 ()    
    at ../sysdeps/i386/i686/fpu/multiarch/e_expf-sse2.S:116    
\\#1  0xb7e145c8 in __GI___expf (x=180.639633)    
    at ../sysdeps/ieee754/flt-32/w_expf.c:26    
\\#2  0x08127eb6 in std::exp (__x=180.639633) at /usr/include/c++/6/cmath:246    
\\#3  0x081283a2 in SITL::Plane::liftCoeff (this=0x820bff0, alpha=3.14159274)    
    at ../../libraries/SITL/SIM_Plane.cpp:77    
\\#4  0x081289d3 in SITL::Plane::getForce (this=0x820bff0,     
    inputAileron=5.66840718e-05, inputElevator=-0.0838166773,     
    inputRudder=0.000192956984) at ../../libraries/SITL/SIM_Plane.cpp:192    
\\#5  0x08129003 in SITL::Plane::calculate_forces (this=0x820bff0, input=...,     
    rot_accel=..., body_accel=...) at ../../libraries/SITL/SIM_Plane.cpp:280    
\\#6  0x081295de in SITL::QuadPlane::update (this=0x820bff0, input=...)    
    at ../../libraries/SITL/SIM_QuadPlane.cpp:102    
\\#7  0x08114a61 in HALSITL::SITL_State::_fdm_input_local (    
    this=0x81d2e60 <sitlState>)    
    at ../../libraries/AP_HAL_SITL/SITL_State.cpp:275    
\\#8  0x0811418e in HALSITL::SITL_State::_fdm_input_step (    
    this=0x81d2e60 <sitlState>)    
    at ../../libraries/AP_HAL_SITL/SITL_State.cpp:137    
\\#9  0x0811452b in HALSITL::SITL_State::wait_clock (this=0x81d2e60 <sitlState>,     
    wait_time_usec=45383771) at ../../libraries/AP_HAL_SITL/SITL_State.cpp:190    
\\#10 0x0811579c in HALSITL::Scheduler::delay_microseconds (    
    this=0x81d53a4 <sitlScheduler>, usec=2764)    
    at ../../libraries/AP_HAL_SITL/Scheduler.cpp:45    
\\#11 0x0811569a in AP_HAL::Scheduler::delay_microseconds_boost (    
    this=0x81d53a4 <sitlScheduler>, us=2764)    
    at ../../libraries/AP_HAL/Scheduler.h:30    
\\#12 0x080a0d37 in AP_InertialSensor::wait_for_sample (    
    this=0x81cf140 <plane+3360>)    
    at ../../libraries/AP_InertialSensor/AP_InertialSensor.cpp:1302    
\\#13 0x0804acf1 in Plane::loop (this=0x81ce420 <plane>)    
    at ../../ArduPlane/ArduPlane.cpp:119    
\\#14 0x081133ed in HAL_SITL::run (this=0x81d56a0 <AP_HAL::get_HAL()::hal>,     
    argc=11, argv=0xbffff454, callbacks=0x81ce420 <plane>)    
    at ../../libraries/AP_HAL_SITL/HAL_SITL_Class.cpp:88    
\\#15 0x0804d59e in main (argc=11, argv=0xbffff454)    
    at ../../ArduPlane/ArduPlane.cpp:1060    
(gdb) print alpha    
No symbol "alpha" in current context.    
(gdb) up    
\\#1  0xb7e145c8 in __GI___expf (x=180.639633)    
    at ../sysdeps/ieee754/flt-32/w_expf.c:26    
26      ../sysdeps/ieee754/flt-32/w_expf.c: No such file or directory.    
(gdb)     
\\#2  0x08127eb6 in std::exp (__x=180.639633) at /usr/include/c++/6/cmath:246    
246       { return __builtin_expf(__x); }    
(gdb)     
\\#3  0x081283a2 in SITL::Plane::liftCoeff (this=0x820bff0, alpha=3.14159274)    
    at ../../libraries/SITL/SIM_Plane.cpp:77    
77              double sigmoid = ( 1+exp(-M*(alpha-alpha0))+exp(M*(alpha+alpha0)) ) / (1+exp(-M*(alpha-alpha0))) / (1+exp(M*(alpha+alpha0)));    
(gdb) print alpha    
$1 = 3.14159274    
```  
That's an interesting value for alpha....
## Comment6
### Comment author: tridge
### Comment Time: May 16, 2017
### Comment Content:
looks like we need a constrain_float() in there
## Comment7
### Comment author: peterbarker
### Comment Time: May 22, 2017
### Comment Content:
@RMIShane If you felt like diving into this one, you can run SITL with --debug --gdb and trace through as I did above.  Did you want to do that?  
A quick workaround would be to change the Vagrant virtual machine to be a 64-bit instance instead of a 32-bit instance.
## Comment8
### Comment author: OXINARF
### Comment Time: Sep 15, 2017
### Comment Content:
This should have been fixed by 85ebe92
## Comment9
### Comment author: RMIShane
### Comment Time: Sep 15, 2017
### Comment Content:
Awesome!    
Thank you!  
…    
On Fri, Sep 15, 2017 at 8:39 AM Francisco Ferreira ***@***.***> wrote:      
 Closed \\\\#6245 <\\\\#6245>.      
 —      
 You are receiving this because you were mentioned.      
 Reply to this email directly, view it on GitHub      
 <\\\\#6245 (comment)>, or mute      
 the thread      
 <https://github.com/notifications/unsubscribe-auth/AbXHWh8BdoZBhTO2CstKxK1A0wqe-YI8ks5sipo1gaJpZM4NaswV>      
 .      
