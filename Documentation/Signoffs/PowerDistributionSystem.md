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

*Constraints are listed in number for Analysis reference.*
<br/><br/>

*Circuit Design:* 

C1. Each power supply is to be adequately sized to be capable of carrying the maximum power requirement for all the devices within its respective circuit.

C2. All wire sizing is to be in accordance with National Electrical Code Article 210.19(A)(1) based on continuous circuit load [1].

C3. The system will maintain overprotection of the Mario Kart simulator devices with a rating of no less than %125 percent of maximum continuous circuit load as specified by 
the National Electrical Code Article 210.20(A) [1]. 

<br/><br/>

*Safety:* 

C4. All 120 Vac terminals within the user interface are to have been covered and contain a warning of electrocution on the cover. 

C5. Power subsystem must include a means of de-energizing the system via circuit breaker lockout. 

C6. Circuit to include GFCI to ensure that all devices within the Mario Kart simulation are properly protected from ground faults. 

<br/><br/>

*Enclosure:* 

C7.  The enclosure is to be sized to house all devices within the subsystem, excluding incoming and outgoing power cabling.

C8. The front panel containing the HMI is to be removable for access. 

C9. The enclosure is to be fully enclosed and free of any openings. 

C10.  The enclosure is to be properly grounded for protection to protect equipment and possible electrical shock.



<br/><br/>




**Buildable schematic:**

![image](https://user-images.githubusercontent.com/114370750/217871834-31a44fc7-9f8c-444d-a56e-c4a7cdb1d108.png)

Figure 1. Power Distribution Wiring Diagram

<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216114599-b0bdc40e-46fc-4784-85f0-373b705f58f3.png)

Figure 2. Power Distribution Model - Right Side
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/216115243-82105226-d890-42b9-8bd9-88a3b267310d.png)

Figure 3. Power Distribution Model - Left Side
<br/><br/>

<br/><br/>

<br/><br/>

**Analysis:**
<br/><br/>
*Analysis is listed in order of constraint reference.*

<br/><br/>

*Circuit Design:*


Devices to be powered within the subsystem below in table 1: 

<br/>

Table 1:

| Circuit Number | Device                      | Voltage (V) | Voltage Type (AC or DC) | Max Current (A) | Max Power (W) |
|----------------|-----------------------------|-------------|-------------------------|-----------------|---------------|
| 1              | Main Controller             | 5           | DC                      | 3               | 15.00         |
| 1              | MET System (User interface) | 5           | DC                      | 3               | 15.00         |
| 1              | Fan 1                       | 5           | DC                      | 0.25            | 1.25          |
| 1              | Fan 2                       | 5           | DC                      | 0.25            | 1.25          |
| 2              | Linear Motor                | 12          | DC                      | 3.4             | 40.80         |
| 3              | Nintendo Switch             | 15          | DC                      | 2.10            | 31.50         |
| 4              | Display Monitor             | 120         | AC                      | 0.29            | 35.00         |

<br/><br/>

A1. *Power Supply Sizing:* Based on the power consumption of all devices in table 1, the power supplies are 45 Watts for both the 5 Vdc and 15 Vdc circuits, while the 12 
Vdc circuit power supply is rated for 60 Watts.

A2. *Wire sizing:* The highest rated current devices powered within this subsystem are the linear motor actuator, which has a rating of 3.4 Amps. The design is to use 14 
Gauge THHN stranded rated at 15 Amps, which is at least %125 of the continuous load rating specified in National Electrical Code Article 210.19(A).

A3. *Overprotection rating:* The designed 4 Amp overprotection circuit breaker meets the %125 NEC requirements specified in the National Electrical Code Article 210.20(A). as 
total current of system is 1.17 Amps as seen in Figure 4.
<br/><br/>

![image](https://user-images.githubusercontent.com/114370750/217872884-6dff9cb9-35c5-4583-b93e-a5aae57e710e.png)

Figure 4. Total AC Current.
<br/><br/>




*Safety Designed:*

A4. *120 Vac Terminals:* All 120 Vac terminals are covered within the enclosure using plexiglass covering with a hazardous warning sticker visible. The hazardous warning is 
to be similar in design as the label represented below in Figure 5. 

<br/><br/>
![image](https://user-images.githubusercontent.com/114370750/216790706-bd4ed616-d75b-4252-b260-186e9926eda7.png)
<br/>
Figure 5. Danger Sign for 120 AC cover.
<br/><br/>

A5. *Means of De-Energizing:* The 5 Amp overprotection device made by Phoenix Contact provides a means of locking out all the devices using a standard circuit breaker lockout. 

A6. *Ground Fault Protection:* Additional protection was designed regarding safety using a Ground Fault Circuit Interrupter (GFCI) built into the incoming power cord of the 
Mario Kart Simulator. 


<br/><br/>

*Enclosure Design:*

A7. *Enclosure Sizing:* The enclosure is increased from previous design to 12” x 12” x 6” for which to provide a minimum of 2” clearance between all devices and the front panel 
for accessibility. 

A8. *Front Panel Access:* The enclosure includes 4 removeable fasteners to remove the front panel for access. 

A9. *Enclosure Quality:* The enclosure is pre-formed and manufactured by Hammond Manufacturing without any openings and cable clamps are to be used to seal power cable input 
and outputs. EPDM rubber is used to create a seal between HMI and inside of front panel.

A10. *Grounding:* Enclosure to be grounded using grounding bar representing in wiring schematic. 







<br/>
<br/>
<br/>
<br/>

**BOM:**
<br/><br/>

| Level | Part #              | Part Name                                                                     | Supplier   | Supplier Part #      | Qty | Units | Unit Cost | Cost    |
|-------|---------------------|-------------------------------------------------------------------------------|------------|----------------------|-----|-------|-----------|---------|
| 1     | Enclosure Assembly  |                                                                               |            |                      |     |       |           |         |
| 1.1   | ENCL1               | BOX STEEL GRAY 12"L X 12"W                                                    | Digikey    | CS12126              | 1   | ea.   | $39.65    | $39.65  |
| 1.2   | CBLCLMP-5           | 5-Pack Cable Clamp                                                            | Home Depot | 100186543            | 1   | ea.   | $4.34     | $4.34   |
| 1.3   | PLXGLS              | 20 in. x 32 in. x 0.093 in. Acrylic Sheet                                     | Home Depot | 202038049            | 1   | ea.   | $25.48    | $25.48  |
| 1.4   | DINRAIL             | TS35 Din Rail 35mm x 7.5mm                                                    | DigiKey    | ADR3575-U7874-ND     | 1   | ea.   | $7.06     | $7.06   |
| 1.5   | EPDM                | EPDM 1/8 in. x 36 in. x 96 in. Commercial Grade 60A Rubber Sheet              | Home Depot | 303371976            | 1   | ea.   | $0.00     | $0.00   |
| 2     | Electrical Assembly |                                                                               |            |                      |     |       |           |         |
| 2.1   | PS1                 | 120 VAC / 5 VDC Power Supply                                                  | DigiKey    | 102-PSK-45-5-DIN-ND  | 1   | ea.   | $22.65    | $22.65  |
| 2.2   | PS2                 | 120 VAC/ 12 VDC Power Supply                                                  | Mouser     | 490-PSK-60-12-DIN    | 1   | ea.   | $24.93    | $24.93  |
| 2.3   | PS3                 | 120 VAC / 15 VDC Power Supply                                                 | DigiKey    | 102-PSK-45-15-DIN-ND | 1   | ea.   | $22.65    | $22.65  |
| 2.4   | SWTCH               | 2 Pos Switch                                                                  | DigiKey    | Z6183-ND             | 1   | ea.   | $4.94     | $15.89  |
| 2.5   | 14GACONN            | 16 - 14 AWG #8 - 10 Stud Size Vinyl-Insulated Spade Terminals, Blue (15-Pack) | Home Depot | 202522889            | 1   | ea.   | $3.63     | $3.63   |
| 2.6   | CBMAIN-1            | CIRCUIT BREAKER 4A                                                            | DigiKey    | 277-17753-ND         | 1   | ea.   | $19.00    | $19.00  |
| 2.7   | 14WIRE              | 25 ft. 14 Black Solid CU THHN Wire                                            | Home Depot | 301210609            | 1   | ea.   | $0.00     | $0.00   |
| 2.8   | GRDBAR              | 4 Terminal Grounding Bar                                                      | Home Depot | 100207842            | 1   | ea.   | $8.31     | $8.31   |
| 2.9   | GFCI-15             | 15 Amp Compact Right Angle Plug-In GFCI, Black                                | Home Depot | 205189963            | 1   | ea.   | $21.99    | $21.99  |
| 2.10  | WARNLAB             | 120 VAC Warning Label                                                         | None       | None                 | 1   | ea.   | $0.00     | $0.00   |
| 2.11  | TRMBLK              | Terminal Block                                                                | DigiKey    | 277-2026-ND          | 8   | ea.   | $1.53     | $12.24  |
| 2.12  | TRMJMP              | 3 Pos - Terminal Block Jumper                                                 | DigiKey    | 277-3230-ND          | 3   | ea.   | $1.80     | $5.40   |
| 2.13  | CONN1               | Linear Motor Control Connector                                                | TME        | XT30U-F              | 1   | ea.   | $0.45     | $0.45   |
| 2.14  | TERMSTP4            | 4 Lug Terminal Strip                                                          | DigiKey    | A98505-ND            | 4   | ea.   | $2.94     | $11.76  |
|       |                     |                                                                               |            |                      |     |       | Total     | $245.43 |

<br/><br/>


**References**
REFERENCES

[1]    NFPA Link®. [Online]. Available: https://link.nfpa.org/free-access/publications/70/2023. [Accessed: 19-Nov-2022].

<br/><br/>
