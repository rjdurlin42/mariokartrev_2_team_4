Team 4 – Mario Kart & Ride Replay Simulator

Team Member: Ray Durlin

Detail Design: Main Power Distribution System


Function of the Subsystem: 

The function of the main power distribution system is to supply protected power to the following components: main microcontroller, user interface microcontroller, microcontroller cooling fans, Nintendo Switch, resistance system linear motor, and lastly the display monitor. The input power is to be received from a wall receptable via a cannon plug connection at the rear of the user interface enclosure. The input voltage is to be 120 volts ac, 60 Hz, circuit protected. A circuit breaker, CBM, is to be installed after the 120 VAC input from the receptacle so that the system can be locked out when any enclosure covers are taken off as a safety precaution. After the input power from the receptable enters the user interface enclosure, the power will be directed to a three of AC to DC converters. Converters C1, C2, and C3 listed on the schematic will convert input voltage from 120 VAC to an output voltage 12 VDC, 5 VDC, and 15 VDC, respectively. The output power by the converters C1, C2, and C3 will then enter three individual mini-fuses, F1, F2, and F3 prior to supplying power to any devices downstream for protecting each device. 


Constraints:

Reliability: The power distribution must provide reliable power to all devices while maintaining the specified protection ratings set by the National Electric Code (NEC). The system will maintain overprotection of the simulator devices with a rating of %125 percent of continuous circuit load as specified by the National Electrical Code Article 210.20(A) [1]. The overprotection rating of each circuit breaker will ensure that all devices are properly protected without the risk of opening the circuit unintentionally as circuit load fluctuates. Unintentionally opening a circuit due to inaccurate load calculations results in decreased system reliability. 

Safety: Safety is the most important aspect of this subsystem as there is the potential for electrocution if not designed properly. To mitigate the possibility of electrocution by anyone working inside the user interface. All 120 VAC terminals within the user interface are to have been covered and contain a warning of electrocution on the cover. It is recommended that lock out tag out procedures to be followed when working within the user interface enclosure with any covers off. All wire sizing is to be in accordance with National Electrical Code Article 240.4(B) based on continuous circuit load [1]. 

Buildable schematic:

![image](https://user-images.githubusercontent.com/114370750/203234571-c7df044e-180e-413c-b995-9f830cb3505d.png)

Analysis:

The power distribution subsystem analysis meets all the power distribution specifications and requirements for all devices receiving power from an outside power receptacle and entering the Mario Kart simulator. Table 1 below shows all devices that were considered during the analysis. Table 1 also specifies the maximum current and power based on the datasheet of each device. The wire and circuit protection sizing within the design is based upon maximum circuit load in accordance with National Electrical Code Article 210.20(A) [1]. 

Starting at the main power input, which in this case is an ordinary 120 VAC, 60 Hz, power receptable, a main circuit breaker, shown as CBM on Figure 1, is located on the outside of the power that is rated at 20 A, based on 125% of total maximum load of the system. The wire size is to be 12-gauge 3 strand (12/3 Romex) rated for 20 A. 

Circuit 1 of the subsystem contains the linear actuator motor. The linear motor is the rated at 125% maximum of 4.38 A and 52.5 W. The input voltage for the linear motor is 12 VDC. The linear motor contributes a significant amount of current and power compared to other circuits within the subsystem. Circuit 1 has an AC to DC converter (C1) rated for 5 A and 60 W. Downstream of the C1 is to be a mini blade fuse rated at 5 A for protection of the converter. A circuit breaker was researched for device protection; however, a fast-acting fuse is more effective for cost and performance.

Circuit 2 of the subsystem included two raspberry pi 4 model B microcontrollers and two computer fans, one is the main microcontroller for the simulator, and the other is for the user interface. The input voltage for these devices is 5 VDC. Although the manufacturer datasheet for the raspberry pi 4 model B does not list a maximum current, the manufacturer does state that a 3 A power supply is recommended. Based on the manufacturer’s recommendations and the 125% rating, both the devices are supplied power by an AC to DC converter (C2) rated for 10 A at 50 W. Downstream of the C2 is to be a mini blade fuse rated at 10 A for protection of the converter. 

Circuit 3 of the subsystem includes the power supply for the Nintendo Switch game console. The Nintendo Switch requires an input of 15 VDC. With a 125% current rating of only 2.68, this circuit has an AC to DC converter (C3) rated for 3A at 45 W. Downstream of the C3 is to be a mini blade fuse rated at 5 A for protection of the converter. 

The display monitor for the simulator has an input voltage is 120 VAC with a 125% maximum current rating of 4.25 A. The display monitor is to be protected using the main circuit breaker, which is within the 125% maximum current rating. No converters are required as the power input is the same as the outlet receptacle. 


| Table 1        |                             |             |                         |                 |               |                         |                      |
| -------------- | --------------------------- | ----------- | ----------------------- | --------------- | ------------- | ----------------------- | -------------------- |
| Circuit Number | Device                      | Voltage (V) | Voltage Type (AC or DC) | Max Current (A) | Max Power (W) | 125 % Rated Current (A) | 125% Rated Power (W) |
| 1              | Linear Motor                | 12          | DC                      | 3.5             | 42.00         | 4.38                    | 52.50                |
| 2              | Main Controller             | 5           | DC                      | 3               | 15.00         | 3.75                    | 18.75                |
| 2              | MET System (User interface) | 5           | DC                      | 3               | 15.00         | 3.75                    | 18.75                |
| 2              | Fan 1                       | 5           | DC                      | 0.25            | 1.25          | 0.31                    | 1.56                 |
| 2              | Fan 2                       | 5           | DC                      | 0.25            | 1.25          | 0.31                    | 1.56                 |
| 3              | Nintendo Switch             | 15          | DC                      | 2.1             | 31.50         | 2.63                    | 39.38                |
| 4              | Display Monitor             | 120         | AC                      | 3.4             | 35.00         | 4.25                    | 43.75                |
|                |                             |             |                         |                 | Total         | 19.38                   | 176.25               |


BOM:

| Team 4 - Mario Kart & RRS | Bill of Materials (BOM)   |                                             |
| ------------------------- | ------------------------- | ------------------------------------------- |
|                           |                           |                                             |  |  |  |  |  |  |
|                           |                           |                                             |  |  |  |  |  |  |
| Subsystem Name:           | Power Distribution System |                                             |  |  |  |
| Requested by:             | Ray D                     |                                             |  |  |  |
| Approve by:               |                           |                                             |  |  |  |
| Total Cost:               | $110.81                   |                                             |  |  |  |
|                           |                           |                                             |  |  |  |  |  |  |
|                           |                           |                                             |  |  |  |  |  |  |
| Level                     | Part #                    | Part Name                                   | Supplier | Supplier Part # | Qty | Units | Unit Cost | Cost |
| 1                         | Main Circuit              | Main Power Input Circuit                    |
| 1.1                       | CBM-1                     | Homeline 20 Amp Single-Pole Circuit Breaker | The Home Depot | 576387 | 1 | Each | $5.98 | $5.98 |
| 1.2                       | ROM-12-3                  | 12/3 Romex Wire                             | The Home Depot | 268925 | 1 | Foot | $2.28 | $2.28 |
| 2                         | Circuit 1                 | Linear Motor Circuit                        |
| 2.1                       | CONV-ACDC1-1              | AC to DC Converter 1                        | DigiKey | 102-PSK-60-12-DIN-ND | 1 | Each | $25.69 | $25.69 |
| 2.2                       | FUSEHOL-1                 | 18 AWG Mini Fuse Holder                     | Crimp Supply | 40A12018 | 1 | Each | $3.56 | $3.56 |
| 2.3                       | FUSE5A-1                  | Bussmann 5 Amp ATM Mini Fuse 5 Piece        | Autozone | BP-ATM-5-RP | 1 | Each | $4.99 | $4.99 |
| 3                         | Circuit 2                 | Main Controller & Interface                 |
| 3.1                       | CONV-ACDC1-2              | AC to DC Converter 2                        | DigiKey | 102-PSK-60-5-DIN-ND | 1 | Each | $22.65 | $22.65 |
|                           | FUSEHOL-2                 | In-line 16 AWG Mini Blade ATM Fuse Holder   | Parts Express | 070-676 | 1 | Each | $1.99 | $1.99 |
|                           | FUSE10A-1                 | 10A ATM Mini Blade Fuse 5-Pack              | Parts Express | 071-3610 | 1 | Each | $2.29 | $2.29 |
| 4                         | Circuit 3                 | Nintendo Switch                             |
| 4.1                       | CONV-ACDC1-3              | AC to DC Converter 3                        | DigiKey | 102-PSK-45-15-DIN-ND | 1 | Each | $22.65 | $22.65 |
| 4.2                       | FUSEHOL-1                 | 18 AWG Mini Fuse Holder                     | Crimp Supply | 40A12018 | 1 | Each | $3.56 | $3.56 |
| 4.3                       | FUSE5A-1                  | Bussmann 5 Amp ATM Mini Fuse 5 Piece        | Autozone |  BP-ATM-5-RP | 1 | Each | $4.99 | $4.99 |
| 5                         | WIRE18AWG-1               | (By-the-Foot) 18/3 Brown Solid              | The Home Depot | 278327 | 10 | Foot | $0.37 | $3.70 |
| 6                         | WIRE16AWG-1               | By-the-Foot) 16/3 300-Volt CU Black         | The Home Depot | 562215 | 6 | Foot | $1.08 | $6.48 |
|                           |                           |                                             |  |  |  |  |  | $0.00 |
|                           |                           |                                             |  |  |  |  | Total | $110.81 |
