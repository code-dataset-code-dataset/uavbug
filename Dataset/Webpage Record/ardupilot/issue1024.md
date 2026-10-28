# Basic Information:
### Title: AP_Mount - odd stabilization w/o RC
### Issue status: Closed
### Author: AndKe
### Issue open time: Apr 25, 2014
# Report
### Report author: AndKe
### Report Time: Apr 25, 2014
### Report Content:
I know the title is unclear - so here's how to reproduce:    
1.- Set up pitch stabilization.    
2.- assign channel for manual pitch angle control    
(at this point everything works as expected)    
3.- shutdown tx and autopilot.    
4.- Start Autopilot only /(do not switch on RC)    
Observe that pitch stabilization is very extreme, not working - until RC TX is turned on.    
-now stabilization works as expected, even if radio goes off.
# Comment
## Comment1
### Comment author: Naterater
### Comment Time: Jan 18, 2019
### Comment Content:
Is this still a bug?
## Comment2
### Comment author: rmackay9
### Comment Time: Jan 18, 2019
### Comment Content:
This was recently fixed in Copter-3.6.5.  
Txs for reviewing these issues