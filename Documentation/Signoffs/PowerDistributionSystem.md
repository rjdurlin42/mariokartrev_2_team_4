Team 4 – Mario Kart & Ride Replay Simulator

Team Member: Ray Durlin

Detail Design: Main Power Distribution System

<br/><br/>


**Function of the Subsystem:** 

The function of the main power distribution subsystem is to receive an incoming power supply from a 120 Vac, 60 Hz, from a wall receptacle and then 
distribute the power through a protected circuit to multiple devices, which carry varying voltage requirements. The following devices that are to 
receive power from the power distribution subsystem are listed below: 
<br/><br/>
•	5 Vdc

&nbsp;&nbsp;&nbsp;&nbsp; o	Main Controller, MET System (User interface), Fan 1, Fan 2, Arduino 1, and Arduino 2

•	12 Vdc

&nbsp;&nbsp;&nbsp;&nbsp;o	Linear Motor

•	15 Vdc

&nbsp;&nbsp;&nbsp;&nbsp;o	Nintendo Switch

•	120 Vac 

&nbsp;&nbsp;&nbsp;&nbsp;o	Display Monitor

<br/>

The wall receptacle provides power via a ground fault circuit interrupter (GFCI) power cord and then goes through an on/off switch located on the 
distribution enclosure. The power is then routed through a 4-amp circuit breaker. Lastly, the protected 120 Vac power branches to the simulator 
display monitor and three AC/DC power supplies, which feed the 5 Vdc, 12 Vdc, and 15 Vdc devices within the Mario Kart simulation bike. 

The power distribution subsystem is to be enclosed in an aluminum enclosure, which is designed within the power distribution subsystem. The power 
distribution enclosure is to house the user interface screen (HMI), cooling fans, on/off switch, (3) power supplies, and (4) microcontrollers. The 
front panel of the enclosure is to be removable for access and house the HMI display.

<br/><br/><br/><br/>
















**Constraints:** 
<br/><br/>

*Circuit Design:* 

• The system will maintain overprotection of the Mario Kart simulator devices with a rating of %125 percent of maximum continous circuit load as specified by the National 
Electrical Code Article 210.20(A) [1]. 
<br/><br/>
• Design circuit must carry load for all devices without the unintentional opening of any circuits which may result in decreased system reliability or system blackouts.
<br/><br/>

*Safety:* 

•  All 120 Vac terminals within the user interface are to have been covered and contain a warning of electrocution on the cover. 
<br/><br/>
• All wire sizing is to be in accordance with National Electrical Code Article 240.4(B) based on continuous circuit load [1].
<br/><br/>
•  Power subsystem must include a means of de-energizing the system via circuit breaker lockout.
<br/><br/>
• Circuit to include GFCI to ensure that all devices within the Mario Kart simulation are properly protected from ground faults. 
<br/><br/>

*Enclosure:* 

• The power distribution subsystem enclosure is to be constructed to contain all electrical devices powered by the powered within the power 
subsystem, excluding the power cord connecting the 12 Vdc power supply to the linear motor controller. 
<br/><br/>
• The front panel of the enclosure is to housing the HMI is to be removable for access.
<br/><br/>
• The enclosure is to be fully enclosed and free of any openings. 
<br/><br/>
• The enclosure is to be properly grounded for protection to protect equipment and possible electrical shock.


<br/><br/>




**Buildable schematic:**

![image](https://user-images.githubusercontent.com/114370750/216790178-2c7bcd85-f7a7-4abf-8896-d0593683e20f.png)

Figure 1. Power Distribution Wiring Diagram

<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216114599-b0bdc40e-46fc-4784-85f0-373b705f58f3.png)

Figure 2. Power Distribution Model - Right Side
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216115243-82105226-d890-42b9-8bd9-88a3b267310d.png)

Figure 3. Power Distribution Model - Left Side
<br/><br/>

<br/><br/>

**Analysis:**
<br/><br/>


*Circuit Design:*
<br/>
The power distribution subsystem includes many devices requiring power, which include multiple differing voltage requirements. The power distribution 
subsystem identifies each circuit based on their respective voltage requirement. The following power requirements identified in the power distribution 
subsystem are listed below in table 1:
<br/>
Table1:
| Circuit Number | Device                      | Voltage (V) | Voltage Type (AC or DC) | Max Current (A) | Max Power (W) |
|----------------|-----------------------------|-------------|-------------------------|-----------------|---------------|
| 1              | Main Controller             | 5           | DC                      | 3               | 15.00         |
| 1              | MET System (User interface) | 5           | DC                      | 3               | 15.00         |
| 1              | Fan 1                       | 5           | DC                      | 0.25            | 1.25          |
| 1              | Fan 2                       | 5           | DC                      | 0.25            | 1.25          |
| 2              | Linear Motor                | 12          | DC                      | 3.4             | 40.80         |
| 3              | Nintendo Switch             | 15          | DC                      | 2.1             | 31.50         |
| 4              | Display Monitor             | 120         | AC                      | 3.4             | 35.00         |

<br/><br/>

Circuit Breaker and Wire Size Determination:	
The power distribution subsystem analysis meets all the power distribution specifications and requirements for all devices receiving power from an 
outside power receptacle and entering the Mario Kart simulator. Table 1 below shows all devices that were considered during the analysis. Table 1 also 
specifies the maximum current and power based on the datasheet of each device. 
<br/><br/>

Prior to selecting an appropriate system circuit protection device, a simulation is completed to determine the power ratings required for each direct 
current circuit (5 V, 12 V, and 15 V) power supply. Figure 4 represents the Simulink circuit model used to determine the size of each power supply. 
The maximum current rating from each device’s datasheet was used to determine a constant power load model. Figures 2, 3, and 4 represent the power 
consumption of each circuit, respectively.
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216790023-47a8da59-759d-4c3c-a374-9e74fc54447b.png)


Figure 4. Matlab Simulation of DC Power
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216790044-aec9b5b3-b37f-476b-8e6a-ca92ce0ba1bc.png)

<br/>
Figure 5. Power (W) as seen by 5 Vdc Circuit.

<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216117790-06d1b409-3ec6-4631-b832-a70b4c5c7547.png)
<br/><br/>
Figure 6. Power (W) as seen by 12 Vdc Circuit.

<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216117885-f8e1ad18-5d2e-481e-9915-9cb7a214f025.png)

Figure 7. Power (W) as seen by 15 Vdc Circuit.
<br/>
<br/>

Based on the simulation, the 5 Vdc circuit will require at least a 33-Watt power supply. A 40-Watt power supply was selected for the 5 Vdc circuit. 
The 12 Vdc circuit will require at least a 41-Watt power supply. A 54-Watt power supply was selected for the 12 Vdc circuit. The 15 Vdc circuit will 
require at least a 32-Watt power supply. A 45-Watt power supply was selected for the 15 Vdc circuit.
<br/>

The final design component for the power distribution subsystem is the system protection device. A model was created in Simulink using the power 
consumption data gathered from the power supply simulation to determine the maximum current on the 120 Vac side of the system. Figure 5 represents the 
circuit created for the circuit protection analysis. Figure 6 shows the current curve of the entire 120 Vac system.
<br/>

![image](https://user-images.githubusercontent.com/114370750/216118598-fd69d017-384a-44b4-b2ee-8ece32e66463.png)

Figure 8. AC Power Distribution Model

<br/>

Based on the simulation, the maximum current within the 120 Vac system is around 1.678 Amps. Using the %125 rule, the minimum rating of the system 
ground fault circuit interrupter (GFCI) is to be at least 2.1 Amps. As a recommendation from the power supply manufacturer’s data sheet, a protection 
device is to be installed upstream of the power supplies in the form of a 4 amp thermal magnetic circuit breaker.The through the AC side can be seen 
in Figure 9. Based on the analysis, the power distrubution subsystem will use 14 Gauge THHN stranded wire that is rated at 15-amps. The 14 Gauge THHN 
stranded wire selection shall cover both AC and DC requirements while still meeting the NEC %125 rule, as stated in the constraints section.

<br/>

![image](https://user-images.githubusercontent.com/114370750/216790057-4469e05d-12df-4846-8ce1-4de7470a6548.png)

Figure 9. Current as seen by the 120 Vac system.
<br/><br/>

*Safety Designed:*

The power distribution subsystem is to be designed to have a plexiglass covering over all 120 Vac wires or terminals. The safety cover has a hazardous 
warning label located on it due to the risk of electrocution. The warning label is to be printed on campus and will match the danger label seen in Figure 10.
<br/><br/>
![image](https://user-images.githubusercontent.com/114370750/216790706-bd4ed616-d75b-4252-b260-186e9926eda7.png)
<br/>
Figure 10. Danger Sign for 120 AC cover.

Wires are also to be marked with their location and voltage to ensure that individuals can safely troubleshoot or add future circuits, if needed. The system is designed with 
an on/off switch to be de-energized when the front panel is off, as the system is to only have the front panel off when the system is de-energized. A 15A GFCI ac power cord 
is to be connected to the main power cord that will protect the whole power system against any ground shorts. 

<br/><br/>

*Enclosure Design:*

The component’s size within power distribution system the analyzed to determine the dimensions of the enclosure. The primary constraint regarding the 
size of the enclosure is the HMI. The current HMI located on the front of the enclosure is approximately 7” (177.8 mm) by 4.5” (114.3 mm). The 
enclosure design is to be 12” (304.8 mm) by 10” (254 mm). The enclosure is to be 152.4 deep to accommodate the power supply depth, including a 
protective cover over the 120 Vac side of the enclosure. The enclosure is to also have knockout accommodations created for the on/off switch, input 
power cord, and output power cord to the display monitor. Each of the knockouts are to be 0.5” (12.7 mm) in diameter. The enclosure is to be made of 
aluminum to decrease the weight of the enclosure. The enclosure is to have knockouts for the two cooling fans and 0.5” (12.7 mm) knockouts external 
connections such as power input/out. All power knockouts will be secured using a screw type cable clamp to ensure that the cords do not get pulled out 
of the enclosure.






<br/>
<br/>
<br/>
<br/>

**BOM:**
<br/><br/>

| Level | Part #              | Part Name                                                                     | Supplier   | Supplier Part #      | Qty | Units | Unit Cost | Cost    |
|-------|---------------------|-------------------------------------------------------------------------------|------------|----------------------|-----|-------|-----------|---------|
| 1     | Enclosure Assembly  |                                                                               |            |                      |     |       |           |         |
| 1.1   | ALUMANGL            | Aluminum Angle                                                                | Home Depot | 204273950            | 1   | ea.   | $14.47    | $14.47  |
| 1.2   | ALUMSHT             | 6 in. x 18 in. 22-Gauge Aluminum Metal Sheet                                  | Home Depot | 204225785            | 1   | ea.   | $12.93    | $12.93  |
| 1.3   | BOLT100             | 1/4-in x 1/2-in Zinc-Plated Coarse Thread Hex Bolt                            | Lowes      | 61820                | 32  | ea.   | $0.00     | $0.00   |
| 1.4   | WASH100             | 1/4-in Zinc-plated Standard Flat Washer                                       | Lowes      | 63306                | 32  | ea.   | $0.00     | $0.00   |
| 1.5   | NUT100              | Hillman  1/4-in x 20 Zinc-Plated Steel Hex Nut                                | Lowes      | 63301                | 32  | ea.   | $0.00     | $0.00   |
| 1.6   | CBLCLMP-5           | 5-Pack Cable Clamp                                                            | Home Depot | 100186543            | 1   | ea.   | $4.34     | $4.34   |
| 1.7   | PLXGLS              | 20 in. x 32 in. x 0.093 in. Acrylic Sheet                                     | Home Depot | 202038049            | 1   | ea.   | $5.34     | $25.48  |
| 1.8   | DINRAIL             | TS35 Din Rail 35mm x 7.5mm                                                    | DigiKey    | ADR3575-U7874-ND     | 1   | ea.   | $7.06     | $25.48  |
| 2     | Electrical Assembly |                                                                               |            |                      |     |       |           |         |
| 2.1   | PS1                 | 120 VAC / 5 VDC Power Supply                                                  | DigiKey    | 102-PSK-45-5-DIN-ND  | 1   | ea.   | $22.65    | $22.65  |
| 2.2   | PS2                 | 120 VAC/ 12 VDC Power Supply                                                  | DigiKey    | 102-PDRB-60-12-ND    | 1   | ea.   | $26.46    | $26.46  |
| 2.3   | PS3                 | 120 VAC / 15 VDC Power Supply                                                 | DigiKey    | 102-PSK-45-15-DIN-ND | 1   | ea.   | $22.65    | $22.65  |
| 2.4   | SWTCH               | 2 Pos Switch                                                                  | DigiKey    | Z6183-ND             | 1   | ea.   | $4.94     | $15.89  |
| 2.5   | 14GACONN            | 16 - 14 AWG #8 - 10 Stud Size Vinyl-Insulated Spade Terminals, Blue (15-Pack) | Home Depot | 202522889            | 1   | ea.   | $3.63     | $3.63   |
| 2.6   | CBMAIN-1            | CIRCUIT BREAKER 4A                                                            | DigiKey    | 277-17753-ND         | 1   | ea.   | $19.00    | $19.00  |
| 2.7   | 14WIRE              | 25 ft. 14 Black Solid CU THHN Wire                                            | Home Depot | 301210609            | 1   | ea.   | $0.00     | $0.00   |
| 2.8   | GRDBAR              | 4 Terminal Grounding Bar                                                      | Home Depot | 100207842            | 1   | ea.   | $8.31     | $8.31   |
| 2.9   | GFCI-15             | 15 Amp Compact Right Angle Plug-In GFCI, Black                                | Home Depot | 205189963            | 1   | ea.   | $21.99    | $21.99  |
| 2.10  | CONN1               | Linear Motor Control Connector                                                | TME        | XT30U-F              | 1   | ea.   | $0.45     | $0.45   |
| 2.11  | TERMSTP             | 4 Lug Terminal Strip                                                          | DigiKey    | 387206204            | 2   | ea.   | $4.17     | $8.34   |
|       |                     |                                                                               |            |                      |     |       | Total     | $232.07 |

<br/><br/>
