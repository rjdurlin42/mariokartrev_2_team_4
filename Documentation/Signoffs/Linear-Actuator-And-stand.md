Team 4 – Mario Kart & Ride Replay Simulator

Team Member: Ray Durlin, Blake Pickett, Tyler Chittum, Benjamin Reed, and Sage Mooneyhamm

Detail Design: Linear Actuator and Stand

<br/><br/>


**Function of the Subsystem:** 
<br/><br/>
The function of the linear actuator stand subsystem is to provide a base for the linear actuator during Mario Kart gameplay and ride replay simulations. The linear actuator 
stand will also house the linear actuator controller. The function of the linear actuator stand is to provide a base for the linear actuator during Mario Kart simulations. 
The linear actuator stand also houses the linear actuator controller. The linear motor’s function is to receive input from the motor control subsystem and provide a feedback 
system to the control.
<br/><br/>

**Constraints:**

*Constraints are listed in number for Analysis reference.*
<br/><br/>
C1. The linear actuator is secured in a manner that the actuator and stand are anchored.

C2. The case of the linear actuator is to be properly grounded.

C3. The linear actuator stand is to be sized for the motor controller to be stored inside of the stand.

C4. The linear actuator stand has two openings for the power and control wires from the controller to the actuator. 

C5. The linear motor stand is to be constructed of materials that will not shield wireless communications of the motor controller. 

<br/><br/>
**Buildable schematic:**
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/217995188-5d1c0067-906f-411a-a265-f294c78b5b1d.png)
<br/>
Figure 1. Right View of 3D model for the Linear Actuator Stand Subsystem
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/217995255-50885073-0629-46af-8559-3bf2e2b51c98.png)
<br/>
Figure 2. Rear View of 3D model for the Linear Actuator Stand Subsystem
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/217995309-3e02fbd0-04e8-4437-88ea-1fe92e44c0eb.png)
<br/>
Figure 3. Full View of 3D model for the Linear Actuator Stand Subsystem

<br/><br/>
<br/><br/>

**Analysis:**

Analysis is listed in order of constraint reference.
<br/><br/>

A1. *Anchoring:* The linear actuator is mounted to the stand, which is anchored to the bike stand frame using clamps, and is represented in Figures 1, 2, and 3.

A2. *Grounding:*  The linear actuator case is grounded to the bike stand frame using 14 Gauge THHN stranded wire, rated for 15 Amps. Paint is to be removed from bike stand 
frame and is represented in Figure 2. 

A3. *Sizing:* The linear actuator stand modeled to be 5.6” x 5.8” x 6.3”, which is capable of containing the controller board that is approximately 3.5” x 2”, while 
maintaining the height required for the resistance subsystem.

A4. *Openings:* Figure 2 shows 2 holes, one circular for power input, and the other a slit opening for the actuator to controller communication/power.

A5. *Constructions:* The linear actuator stand is constructed using 0.5” thick plexi-glass material that will not block communication from the linear actuator controller to 
the main controller.





<br/><br/>
<br/><br/>
**BOM:**
<br/><br/>
The bill of materials (BOM) to accomplish the design illustrated in the schematics is provided in Table 1. 
<br/><br/>
Table 1.

| Level | Part #      | Part Name                                                                     | Supplier      | Supplier Part # | Qty | Units | Unit Cost | Cost    |
|-------|-------------|-------------------------------------------------------------------------------|---------------|-----------------|-----|-------|-----------|---------|
| 1     | LINMOTOR100 | Linear Motor                                                                  | Pololu        | 4953            | 1   | ea.   | $183.95   | $183.95 |
| 2     | SCR3        | #3 x 1/2 in. Phillips Head Brass Wood Screw (6-Pack)                          | Home Dept     | 204587520       | 1   | bag   | $1.38     | $1.38   |
| 3     | PLXGLS      | 20 in. x 32 in. x 0.093 in. Acrylic Sheet                                     | Home Dept     | 202038049       | 1   | ea.   | $25.48    | $25.48  |
| 4     | CBLCLMP1    | CBL CLAMP P-TYPE BLACK FASTENER                                               | DIGIKEY       | N-32B-BK        | 2   | ea.   | $1.20     | $2.40   |
| 5     | 14WIRE      | 25 ft. 14 Black Solid CU THHN Wire                                            | Home Depot    | 301210609       | 1   | ea.   | $0.00     | $0.00   |
| 6     | 14GACONN    | 16 - 14 AWG #8 - 10 Stud Size Vinyl-Insulated Spade Terminals, Blue (15-Pack) | Home Depot    | 202522889       | 1   | ea.   | $3.63     | $3.63   |
| 7     | SCR2        | #2 x 1/4 in. Phillips Flat Head Zinc Plated Wood Screw (8-Pack)               | Home Dept     | 204587381       | 4   | bag   | $1.38     | $5.52   |
| 8     | LNMTCLP     | Routing Clamp                                                                 | McMaster Carr | 3039T16         | 3   | ea.   | $2.92     | $8.76   |
| 9     | BRKPLT      | 12 in. x 12 in. 22-Gauge Weldable Sheet                                       | Home Dept     | 100237896       | 1   | ea.   | $13.57    | $13.57  |
| 10    | AXLMNT      | 10mm Universal Aluminum Mounting Hubs for Shaft – 18009                       | OzRobitics    | 18009           | 1   | ea.   | $9.40     | $9.40   |
|       |             |                                                                               |               |                 |     |       | Total     | $254.09 |
