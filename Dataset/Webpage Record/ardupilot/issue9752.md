# Basic Information:
### Title: 80% MAVLink Packet loss when connected to Mission Planner or other GCSs
### Issue status: Closed
### Author: jmachuca77
### Issue open time: Nov 10, 2018
# Report
### Report author: jmachuca77
### Report Time: Nov 10, 2018
### Report Content:
Bug report  
There is about an 80% packet loss being reported by MAVProxy, when mission planner or Solex are connected to telemetry over UDP. Not sure where the loss is occurring, it could be from the pixhawk to the CC, or in MAVlink_router.  
To reproduce, use APsync CC to connect to a pixhawk. Run MAVproxy locally to monitor packet loss. When no GCS is connected, packet loss reported is 0 or 0.2% max. As soon as a GCS is connected packet loss jumps to almost 80%. When the GCS is disconnected packet loss returns to normal. This behavior is seen with Mission planner and Solex, but not with QGC.  
Version    
Multiple versions only tested on Rover. Copter does show this behavior.  
Platform    
[ X ] Rover  
MAVProxy Output (running locally on CC)    
OLD> link 1 OK (2978 packets, 0.00s delay, 5 lost, 0.2% loss)    
link    
HOLD> link 1 OK (3065 packets, 0.00s delay, 5 lost, 0.2% loss)    
link    
HOLD> link 1 OK (3896 packets, 0.00s delay, 5 lost, 0.1% loss)    
link    
HOLD> link 1 OK (3967 packets, 0.00s delay, 5 lost, 0.1% loss)    
link    
HOLD> link 1 OK (4055 packets, 0.00s delay, 5 lost, 0.1% loss)    
link    
HOLD> link 1 OK (4113 packets, 0.00s delay, 5 lost, 0.1% loss)    
link    
HOLD> link 1 OK (4159 packets, 0.00s delay, 32 lost, 0.8% loss)    
linkAPM: Mission Planner 1.0.0.0  
HOLD> link 1 OK (4220 packets, 0.00s delay, 32 lost, 0.8% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4259 packets, 0.00s delay, 287 lost, 6.3% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4301 packets, 0.00s delay, 543 lost, 11.2% loss, (no-signing-secret))    
APM: ArduRover V3.4.2 (318a941)    
APM: PX4: b535f974 NuttX: 1472b16c    
APM: PX4v3 00490024 33375111 37353832    
link    
HOLD> link 1 OK (4359 packets, 0.00s delay, 543 lost, 11.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4399 packets, 0.00s delay, 799 lost, 15.4% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4442 packets, 0.00s delay, 1034 lost, 18.9% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4498 packets, 0.00s delay, 1054 lost, 19.0% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4545 packets, 0.00s delay, 1309 lost, 22.4% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (4602 packets, 0.00s delay, 1564 lost, 25.4% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (5066 packets, 0.00s delay, 3094 lost, 37.9% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (5126 packets, 0.00s delay, 3094 lost, 37.6% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (5177 packets, 0.00s delay, 3349 lost, 39.3% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (5207 packets, 0.00s delay, 3583 lost, 40.8% loss, (no-signing-secret))    
HOLD> link    
HOLD> link 1 OK (37878 packets, 0.00s delay, 76870 lost, 67.0% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (37922 packets, 0.00s delay, 77124 lost, 67.0% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (37957 packets, 0.00s delay, 77124 lost, 67.0% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38029 packets, 0.00s delay, 77379 lost, 67.0% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38069 packets, 0.00s delay, 77634 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38100 packets, 0.00s delay, 77634 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38123 packets, 0.00s delay, 77634 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38138 packets, 0.00s delay, 77889 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38158 packets, 0.00s delay, 77889 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38173 packets, 0.00s delay, 77889 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38204 packets, 0.00s delay, 77889 lost, 67.1% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38212 packets, 0.00s delay, 78144 lost, 67.2% loss, (no-signing-secret))    
link    
HOLD> link 1 OK (38242 packets, 0.00s delay, 78144 lost, 67.1% loss, (no-signing-secret))
# Comment
## Comment1
### Comment author: Pedals2Paddles
### Comment Time: Nov 10, 2018
### Comment Content:
The same happens on the solo with it's UDP telem. Very annoying.
## Comment2
### Comment author: jmachuca77
### Comment Time: Nov 10, 2018
### Comment Content:
@Pedals2Paddles to what degree? Kelly has checked it on Solo and he mentioned it is not this bad. And I tested Copter and it does not happen.
## Comment3
### Comment author: Pedals2Paddles
### Comment Time: Nov 11, 2018
### Comment Content:
If you use the "link stats" in mission planner, it will show 80-95% packet loss.  That's the only place I've looked.
## Comment4
### Comment author: jmachuca77
### Comment Time: Nov 11, 2018
### Comment Content:
Solo on Master? Or Solo firmware?
## Comment5
### Comment author: jmachuca77
### Comment Time: Nov 11, 2018
### Comment Content:
Tridge/Randy, any ideas?
## Comment6
### Comment author: jmachuca77
### Comment Time: Nov 11, 2018
### Comment Content:
These are the tlogs from Mission Planner    
Packetloss_logs.zip
## Comment7
### Comment author: tridge
### Comment Time: Nov 11, 2018
### Comment Content:
you'd need to work out if the packet loss is real. MAVProxy gets packet loss by looking at the sequence numbers. This can be fooled in many ways:  
- if a duplicate packet is sent, then this is seen as a loss of 255 packets  
- if two packets arrive out of order then this is seen as loss of 254 packets  
to look into this you need to examine the log a lot more closely
## Comment8
### Comment author: Pedals2Paddles
### Comment Time: Nov 11, 2018
### Comment Content:
There doesn't seem to be any actual degredation of the telemetry. So I think it is likely as Tridge described.
## Comment9
### Comment author: peterbarker
### Comment Time: Nov 12, 2018
### Comment Content:
On Sat, 10 Nov 2018, Jaime Machuca wrote:    
 There is about an 80% packet loss being reported by MAVProxy, when mission    
 planner or Solex are connected to telemetry over UDP. Not sure where the    
 loss is occurring, it could be from the pixhawk to the CC, or in    
 MAVlink_router.  
What system IDs are you using for each of the GCSs involved?
## Comment10
### Comment author: rmackay9
### Comment Time: Nov 13, 2018
### Comment Content:
@jmachuca77, above it says, "Copter does show this behavior" but it should say, "Copter does not show this behavior" right?
## Comment11
### Comment author: jmachuca77
### Comment Time: Nov 13, 2018
### Comment Content:
@rmackay9 right, it's a typo I'll correct it in the morning
## Comment12
### Comment author: Professor77
### Comment Time: May 19, 2019
### Comment Content:
My qgc Mavlink setting shows an 85% loss but there's no problem connecting to the vehicle and getting the telemetry.  
Mission planner says 100%... no losses!  
I'm using clone pixhawk 2.4.8 with latest apm firmware, sik 433mhz telemetry set that came in the package.  
Aborted my maiden flight today because of a plan upload error... caused by me trying to manually set home position not knowing it automatically sets upon arming.  
Internet digging revealed plan upload errors can be caused by bad telemetry link, that's how I found the qgc mavlink setting.  
Anyway I uploaded a plan fine from qgc pc, and the set plan downloaded from vehicle to my android tablet qgc so data is being transferred successfully.  
Good to read about miscounted packet loss on this thread... I'm a total noob!
## Comment13
### Comment author: OXINARF
### Comment Time: Jun 11, 2019
### Comment Content:
@jmachuca77 Is this still relevant?
## Comment14
### Comment author: mnumanuyar
### Comment Time: Aug 06, 2020
### Comment Content:
fyi this is also relevant for QGC. I observed it in a costumized v4.0.8 build with mocklink . the loss calculation is like below :  
    
```bash     
             uint8_t expectedSeq = lastSeq + 1;    
            .    
            .    
            .    
            if (_message.seq != expectedSeq)    
            {    
                //foo = 1;    
                int lostMessages = 0;    
                //-- Account for overflow during packet loss    
                if(_message.seq < expectedSeq) {    
                    lostMessages = (_message.seq + 255) - expectedSeq;   // this causes loss misscount    
                } else {    
                    lostMessages = _message.seq - expectedSeq;    
                }    
                // Log how many were lost    
                totalLossCounter[mavlinkChannel] += static_cast<uint64_t>(lostMessages);    
            }    
```
## Comment15
### Comment author: jmachuca77
### Comment Time: Aug 07, 2020
### Comment Content:
This ended up being as Tridge mentioned above a problem with the way the packet loss is measured. Latest releases for Rover dont show this behavior.
## Comment16
### Comment author: shivam2813
### Comment Time: Apr 16, 2025
### Comment Content:
For me I am using a telemetry module and whenever I connect to it using udp I get more packet loss than packet count and when I use rfd connection it shows right value on mavproxy but not through udp telemetry and mission planner just shows me 100%