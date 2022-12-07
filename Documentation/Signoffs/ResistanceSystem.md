Team 4 – Mario Kart & Ride Replay Simulator

Team Members: Ray Durlin, Blake Pickett, Tyler Chittum, Benjamin Reed, and Sage Mooneyham

## Detail Design: Resistance System ##


### Function of the Subsystem:

The function of the resistance system is to control and vary the resistance felt by the user of the Mario Kart Bike, hereafter referred to as the bike.  

- The monitors the linear actuator feedback voltage to determine its current position with 10-bit precision, which corresponds to the distance of the magnet array from the flywheel. 

- An external digital input (via the Bluetooth module) is received from the ride replay subsystem to determine the calculated set point which the actuator should extend to. This recieved value corresponds to a resistance state, of which there are 1024, since the limiting factor is the 10-bit precision of the controller.

- The controller supplies either a positive or negative voltage to the linear actuator to control the direction of the actuator's motion. 

- The actuator is to vary the array of magnets perpendicular to the simulator’s rear conductive flywheel (not the current flywheel on the bike, a new flywheel with dimensions that fit our design more effectively) to generate eddy currents using the primary magnetic induction formed at the conductor [1], which result in the generation of braking torque opposed onto the flywheel. 

- The braking torque will transfer from the flywheel to the rear bike tire, and then from the rear bike tire to the rider’s pedals, which will act to resist the pedaling of the rider. 



### Constraints:

#### Magnet Distance Range: 

- A distance range of 2-25mm from magnet to flywheel was selected, as these distances matched up well with the torque values that we want the resistance system to apply. 

 

#### Minimum Tire Speed: 

- The minimum speed of the bike tire shall be considered 116.35 rpm. This value is based on the American Council on Exercise's recommendation for the minimum wheel speed recommended for moderate exercise on a bike [2]. This correlates to 2501.52 rpm in the flywheel (conversion is explained in later sections). At speeds less than 116.35 rpm, the torque placed on the rider will not be specified to reach any minimum value, and the resolution of the resistance changes within this operating region is not specified.

 

#### Maximum Tire Speed: 

- The maximum speed of the bike tire shall be considered 288 rpm, a value that comes from the average pedaling rpm (118 rpm) of an elite level cyclist [3] (Wheel to pedal gear ratio = 2.444, so wheel speed = 2.444*pedal speed). This correlates to 6192 rpm in the flywheel due to the the rotational velocity ratio of 43:2 between the flywheel and the wheel. If the user passes this speed, no additional torque will be applied to avoid injury to rider. 

 

#### Maximum Torque at Minimum Speed: 

- Using the value for tire minimum speed (116.35 rpm), we know that the maximum torque at this speed will be produced when the magnets are closest (2mm). From here, you can find magnetic field felt at the flywheel using equation 2. These values can be plugged into equation 1 to give the torque at the flywheel, which can then be converted to torque at the bike wheel/pedals using the gearing ratios between the components (this is explained in more detail later in the document). Using this logic, we find that the max torque at the minimum speed is 49.23 Nm. 

#### Minimum Torque at Minimum Speed: 

- Using the above logic while setting magnet distance to the furthest value (20mm) and wheel speed to the minimum value, we find the minimum torque at minimum speed is 0.002 Nm. 

  

#### Maximum Torque at Maximum Speed: 

- Using the above logic while setting magnet distance to the closest value and wheel speed to the maximum value (288 rpm), we find the maximum torque at maximum speed is 121.85 Nm. Safety always being a concern, this force is much lower than what is needed to break any leg bone in the average person. [4] [6]. 

  

#### Minimum Torque at Maximum Speed: 

- Using the above logic while setting magnet distance to the furthest value and wheel speed to the maximum value, we find the minimum torque at maximum speed is 0.004 N•m. 

#### Resistance Resolution: 

- The resistance system will have a resolution of at least 85 states. 

- The controller will allow for 10-bit resolution or 1024 unique states. 

The linear actuator used has a length of 1.97". In practical usage, we would use 49.96 % of this range, yielding an effective number of states of 511.

Note: The minimum and maximum speeds referenced within this section have been converted to bike tire rpm, so the units of measure are consistent throughout the report. The pedaling speed sourced from the reference was multiplied by the gear ratio from the front to rear sprocket, which was 2.44. The speed of the bike is referred to in the units of bike tire revolutions per minute (rpm). 




### Buildable Schematic:

![image](https://user-images.githubusercontent.com/114370750/205554450-37b7aedf-20ad-4403-ab97-4d81d6decbce.png)

Figure 1. Resistance System Full View

![image](https://user-images.githubusercontent.com/114370750/205554492-89368243-436b-4ada-a5b3-ee7d10c3539f.png)

Figure 2. Close Up of Linear Actuator, Flywheel, Magnet Holder

![image](https://user-images.githubusercontent.com/114370750/205554527-ea166ccf-6503-40b6-9993-45dad74d8431.png)

Figure 3. Close Up of Linear Actuator, Flywheel, Magnet Holder with Different Viewpoint



### Aluminum Flywheel:

•	An aluminum circle with a radius of 101.6 mm (4”) will be cut from a sheet of aluminum material. 

•	A hole will be drilled in the center of the aluminum flywheel. 

•	The steel flywheel on the UNISKY bike stand will be replaced with the new aluminum flywheel. 

&ensp;&thinsp; &ensp;&thinsp; •The bolt holding the steel flywheel will be unscrewed.
   
&ensp;&thinsp; &ensp;&thinsp; •The steel flywheel will be replaced with the aluminum flywheel.
   
&ensp;&thinsp; &ensp;&thinsp; •The bolt will be screwed back into place on the bike stand.
   
•	The drive wheel at the back of the UNISKY bike stand will be screwed into the rear wheel of the bike.

&ensp;&thinsp; &ensp;&thinsp; •	This will ensure maximum transfer of energy when the magnetic breaking occurs to the flywheel. 
   
•	The UNISKY bike stand will come with a magnetic brake which will be removed. 


*Bracket:*

•	For the magnetic portion of the resistance system, two mounting brackets will be welded to a metal block stand.

&ensp;&thinsp; &ensp;&thinsp; • The two mounting brackets will be separated by 246 mm to allow for proper mounting of the linear actuator. 

•	The linear actuator will be hooked to the two mounting brackets. 

•	A 14 mm square bracket will be welded to the circular steel bracket.

•	Two magnets will be attached to the opposite side of the circular bracket using the ferromagnetic properties of the steel to hold the magnets in place.

•	The linear actuator will be attached to the square bracket. 





### Analysis:

#### Method of Data Analysis for Calculating Torque: 
The resistance system is centered on the electromagnetic topic of eddy currents and Lenz’s Law. An equation found in a publication for the Centre for Intelligent Machines that models the function of an eddy current braking system was utilized to determine the attributes of the resistance system components [1]. Specifically, the torque achieved depends on angular speed, as well as magnet distance from the flywheel. The function is shown below. 

 ![image](https://user-images.githubusercontent.com/100988295/205823414-769b3940-8802-42f7-8f2f-d8c696565979.png)
</br> where, 

σ = Conductivity of flywheel material  (Ω−1m−1) </br>
D=magnet diameter (meters) </br>
d = disc (flywheel) thickness (meters) </br>
B = magnet field strength (Tesla) </br>
R = dist from flywheel center to magnet (m) </br> 
θ = angular velocity (rads/s) </br>

This equation was used to determine the torque produced in the flywheel at varying magnet distances and angular speeds. This torque can then be used to find the torque felt in the bike tire, as well as pedals, by applying the flywheel to tire gear ratio (43:2) or tire to pedal gear ratio (43:18), respectively. The following values were determined from the onset. 

- The bicycle’s wheel radius is a known constant of 0.33 m.  

- The flywheel’s radius is a known constant of 0.1016 m. 

- The flywheel’s thickness is a known constant of 0.0127 m. 

- The magnet’s diameter is a known constant of 0.0508 m. 

- The material for the flywheel is aluminum because aluminum has the highest conductivity for the cost, allowing the resistance system to reach the necessary torque values. Therefore, this value is 3.77*107 (Ωm)-1. 

- The axis-to-pole value was set to be approximately 0.305 m. This distance was determined by the flywheel’s radius minus the maximum radius of the magnet options available. Torque is maximized when the magnets are at the edge of the flywheel. 


#### Method of Data Analysis for Calculating Distance between Magnet and Flywheel (Air Gap):

The magnetic field and angular speed can be considered the varying components in torque calculation.  The angular speed will determine the magnet distance (field strength at the flywheel) needed to produce certain torque states. The resistance system will vary the distance between 2 mm and 25 mm. 


The linear motor will increase or decrease the distance from the aluminum flywheel to the magnet (air gap), resulting in an increase or decrease in the magnetic field the flywheel experiences. The distance to magnetic field relationship can be modeled using Equation 2 below, which was found within the magnet suppliers’ website [5].

![image](https://user-images.githubusercontent.com/114370750/205557403-c2894074-2403-4ebe-b96b-c4b6a4af9e1e.png)

where,

μ_o=magnetic permeability in a vaccum (Tm/A)

m = magnetic moment (Am^2 )

r=dist. from magnet to flywheel (m)

Because the x-component of the point of measurement on the flywheel is zero, the total magnetic field at the flywheel is equal to the y-component of the magnetic field. 

Magnetic moment of the magnet can be found using Equation 3 found within the magnet suppliers’ website [5].

![image](https://user-images.githubusercontent.com/114370750/205557488-ab291188-2b77-40df-9f27-09e2d75a0c27.png)

where, 

B_(r )= residual field (Gauss)

V = magnet volume (m^3 )

The disk magnets utilized in the analysis are 2 inches in diameter and 0.125 inches in thickness. The supplier part number for K & J Magnetics is DY04-N52 [5]. The magnet used in the analysis was determined based on the supplier’s documented shape and field strength. The optimal shape of the magnet for this analysis is a disk shape. The disk shape allowed the team to apply Lenz’s formula without further adaptation. The DY04-N52 magnets have a surface field of 1795 Gauss, which is the ideal field strength to the torque generated by the eddy currents within the resistance system based on the analysis gathered within this report.

*DY04-N52 Magnet Characteristics:*

•	Residual field provided by the magnet suppliers is14,800 Gauss

•	Volume is calculated to be 1.287E-5 m^3

•	Calculated magnetic moment of 15.158 Am^2 

Note: The calculated distance between the magnets and the flywheel required to control the resistance felt by the user will be calculated by the Ride Simulation System (RSS) processing subsystem and is an external input to the resistance subsystem.

#### Minimum Speed Analysis: 

Objective: To prove that the resistance system can provide and vary torque while the rider is traveling at a minimum speed of 116.35 rpm.  

The plots in Figures 6 and 7 are a representation of provided torque, based on the magnetic field between the magnet and flywheel using Equation 1. 

![image](https://user-images.githubusercontent.com/114370750/205557898-94cd16c9-e4c5-4ce1-b1ab-4bc68f78ec05.png)

Figure 4. Torque on Rider at Minimum Speed.

![image](https://user-images.githubusercontent.com/114370750/205557970-689677c3-70c4-4309-b379-6b12a88d00ad.png)

Figure 5. Torque Generated at Flywheel at Minimum Speed.

The analysis validates that the resistance system can provide and vary torque braking torque while operating at the minimum speed of 116.35 rpm, with a distance range of 2-25mm between magnet and flywheel. For the minimum speed analysis, the flywheel speed was calculated at 2501.6. To calculate the flywheel speed, the bike tire rpm was multiplied by 21.5. The value of 21.5 is the gear ratio between the bike tire and the flywheel.  


#### Maximum Speed/Maximum Torque Analysis:

Objective: To prove that the resistance system can provide and vary torque while the rider is traveling at a maximum speed of 288 rpm.


![image](https://user-images.githubusercontent.com/114370750/205558420-97cdf8b7-f5d1-453d-b502-f23db541e869.png)

Figure 6. Torque on Rider at Maximum Speed.

![image](https://user-images.githubusercontent.com/114370750/205558480-a69e9015-321e-4a08-9546-30432f8b18a8.png)

Figure 7. Torque Generated at Flywheel at Maximum Speed.




Figures 8 and 9 show the torque generated by the resistance system while the rider is at the maximum speed of 288 rpm. The maximum torque that the resistance system can generate will occur at the maximum speed of the bike, with the closest distance between magnet and flywheel. We can see in Figure 8 that the maximum achieved torque is equal to 121.845 Nm. The increased torque generated is the result of an increase in eddy currents, which is represented in Equation 1 in the form of angular velocity (Rad/s). Analysis validates that the maximum torque that the resistance will provide to the rider is 121.845 N•m 

#### Resistance Resolution Analysis:

•	The torque values were calculated by determining incline angle, denoted α, increases that resulted in 10 % increases – give or take 3-4 % – in resistance, given by sin(α), for a range of 0° to 40°. This was done in accordance with the previous specifications proposed for this project.

•	The torque values were determined by scaling the resistance values by that of the 85th state, then multiplying all values by 28.9 Nm to find fractions of our maximum torque.

•	This process was completed using a MATLAB script, which are in the project folder under the name state_test.m. The torque values, in Nm, are shown in Table 1. 


|     Table 1.   Torque Values in Nm    |               |               |               |               |               |               |               |               |
|---------------------------------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
|     0.0643                            |     0.0693    |     0.0742    |     0.0841    |     0.0940    |     0.1039    |     0.1138    |     0.1237    |     0.1336    |
|     0.1435                            |     0.1583    |     0.1732    |     0.1880    |     0.2029    |     0.2177    |     0.2375    |     0.2573    |     0.2771    |
|     0.2969                            |     0.3216    |     0.3463    |     0.3711    |     0.4008    |     0.4305    |     0.4651    |     0.4997    |     0.5393    |
|     0.5789                            |     0.6234    |     0.6679    |     0.7174    |     0.7718    |     0.8262    |     0.8856    |     0.9499    |     1.0192    |
|     1.0934                            |     1.1725    |     1.2566    |     1.3456    |     1.4445    |     1.5484    |     1.6572    |     1.7759    |     1.9044    |
|     2.0379                            |     2.1813    |     2.3345    |     2.5025    |     2.6804    |     2.8681    |     3.0706    |     3.2879    |     3.5198    |
|     3.7666                            |     4.0329    |     4.3189    |     4.6244    |     4.9494    |     5.2988    |     5.6725    |     6.0704    |     6.4974    |
|     6.9533                            |     7.4428    |     7.9657    |     8.5268    |     9.1256    |     9.7667    |     10.454    |     11.188    |     11.972    |
|     12.811                            |     13.712    |     14.674    |     15.705    |     16.808    |     17.989    |     19.249    |     20.599    |     22.041    |
|     23.586                            |     25.239    |     27.007    |     28.901    |               |               |               |               |               |

In order to find the minimum change in torque required for the design, the values of torque up to the maximum torque attainable at the minimum speed was calculated via the prior algorithm. The smallest change in torque present within the resulting list was 0.0084 N•m, which corresponds to the very first two states in the list. The difference in torque corresponding to the difference in distance between the furthest two possible positions which the controller can set the actuator in a range extending from 2 mm to 25 mm is 0.141 micro N•m.

*Control Circuit Components Analysis:*

An analysis of selected control circuit components and the resultant relevant design considerations are provided in Table 2.

|     Table 2: Analysis of Selected Control Circuit Components   and Design Considerations    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     Component(s)                                                                            |     Design   Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     Switching Transistors (Q1, Q2, Q3, Q4)                                                  |     Q1 and Q2 are rated to handle continuous current up to 24   A, while Q3 and Q4 are rated to handle continuous current up to 45 A; both   are well above the expected current requirement. Q1 and Q2 only need to   switch when the actuator changes direction, and a delay can be   programmatically implemented to ensure no current flows during the switching   of these transistors. However, Q3 and Q4 must be able to switch fast enough   to handle Pulse Width Modulation (PWM). These FETs have rise and fall times in   the order of tens of nanoseconds. As such, they should be easily capable of   handling a PWM signal in the kHz range.    |
|     Back-EMF Protection Diodes (D1, D2, D3, D4)                                             |     These diodes are Schottky diodes with fast switching time   and very low forward voltage. Compared to the body diodes of the utilized   transistors (Vf ~ 1 V), these diodes provide a forward voltage of   equal to or less than 0.5 V, effectively bypassing the transistors during   reverse-conduction. These diodes are specified for use in free-wheeling   applications in the datasheet and are well-suited to handle the large   momentary current spikes produced by back-EMF, given that they are rated to   handle 100 A peak current.                                                                                                         |
|     Resistors (All)                                                                         |     All resistors in this circuit were subject to only very   small power dissipations: less than a milliwatt in all cases. As such, small,   common ¼ W resistors were selected. Gate resistors were selected to be   surface mount chip-resistors to minimize space usage. The gate driver   resistors for the P-Ch FETs are larger than those for the N-Ch FETs, as   switching speed is not a priority for the P-Ch FETs. The PWM will be done on   the N-Ch FETs, and it is vital that the voltage drop across the gate driver IC   be minimized to ensure complete biasing at steady-state.                                                              |
|     Pre-Biased Dual NPN IC (U1)                                                             |     This component is used to bias the gates of the P-Ch FETs,   as turning these transistors off will require a voltage of 12 V – a voltage   not achievable by using the microcontroller alone. This component was   selected because it combines the utility of four resistors and two BJTs into a   single package.                                                                                                                                                                                                                                                                                                                                        |
|     Arduino Nano (A1)                                                                       |     This microcontroller module was selected because it is   already in our stock. It provides an on-board voltage regulator capable of   regulating to 3.3 V and to 5 V. The 3.3 V supply is ideal for powering the   selected wireless module, while the 5 V supply is ideal for providing a   logic-voltage reference to the linear actuator feedback.                                                                                                                                                                                                                                                                                                      |
|     Bluetooth Module                                                                        |     The HC06 module is an incredibly cheap Bluetooth module.   It should be capable of providing the required range, as it has a maximum   range of about 10 m. In addition to being inexpensive, this module also has   the benefit of being very easily connected; it requires only four pins to be   connected to the external circuit.                                                                                                                                                                                                                                                                                                                     |
|     Power Connector                                                                         |     The component handles the power input to the circuit,   which is then fed into the linear actuator. As such, it must be rated to   handle several amperes of current. An XT30 connector was selected, as this   type is rated for 15 A which is well over the expected current demand; it   does not allow the user to connect the polarity incorrectly. In addition, the   mating connector is commonly available in a form that lends itself to the   easy fabrication of cables of a custom length without any special equipment.                                                                                                                       |


*Abbreviation Definitions:*

•	3D: three dimensional

•	RPM: revolutions per minute

•	FET: field effect transistor

•	P-Ch: P-channel

•	N-Ch: N-channel

•	PWM: Pulse-width modulation

•	EMF: electromotive force; a potential difference

•	IC: integrated circuit

•	BJT: bipolar junction transistor

### BOM:

| Team 4 - Mario Kart & RRS |                 | Bill of Materials   (BOM)                         |               |                  |     |        |           |         |
|:-------------------------:|:---------------:|---------------------------------------------------|---------------|------------------|-----|--------|-----------|---------|
|                           |                 |                                                   |               |                  |     |        |           |         |
|                           |                 |                                                   |               |                  |     |        |           |         |
| Subsystem Name:           |                 |                 Resistance System                 |               |                  |     |        |           |         |
| Requested by:             |                 | Ray D, Blake P, Tyler C,   Benjamin R, and Sage M |               |                  |     |        |           |         |
| Approve by:               |                 |                                                   |               |                  |     |        |           |         |
| Total Cost:               |                 |                      $427.48                      |               |                  |     |        |           |         |
|                           |                 |                                                   |               |                  |     |        |           |         |
|                           |                 |                                                   |               |                  |     |        |           |         |
|           Level           |      Part #     |                     Part Name                     |    Supplier   |  Supplier Part # | Qty |  Units | Unit Cost |   Cost  |
| 1                         |      RS100      |                      Assembly                     |      None     |       None       |  1  |  Assy  |   $0.00   |  $0.00  |
|            1.1            |   ALUMPLATE100  |          Aluminum Plate   10" X10"X 0.5"          | Online Metals |       4535       |  1  |  Sheet |   $70.32  |  $70.32 |
| 2                         |    HBRIDGE100   |                      Assembly                     |      None     |       None       |  1  |  Assy  |   $0.00   |  $0.00  |
|            2.1            |     SOCK100     |                 DC Connector -Male                |      TME      |     XT30PW-M     |  1  |  Piece |   $0.63   |  $0.63  |
|            2.2            |    MOSFET100    |                       MOSFET                      |    DIGIKEY    |      G26P04K     |  2  |  Piece |   $0.78   |  $1.56  |
|            2.3            |    MOSFET101    |                       MOSFET                      |    DIGIKEY    |      AOD424      |  2  |  Piece |   $0.98   |  $1.96  |
|            2.4            |    WIFIREC100   |                Bluetooth Receiveer                |   ALIEXPRESS  |       HC-06      |  1  |  Piece |   $2.24   |  $2.24  |
|            2.5            |     DIODE100    |                       Diode                       |    DIGIKEY    |     B320-13-F    |  4  |  Piece |   $0.48   |  $1.92  |
|            2.6            |      BJT100     |                        BJT                        |    DIGIKEY    |   DDC114YU-7-F   |  1  |  Piece |   $0.43   |  $0.43  |
|            2.7            |   CHRESIST100   |                   Chip Resistor                   |    DIGIKEY    | CRCW120610K0JNEA |  2  |  Piece |   $0.10   |  $0.20  |
|            2.8            |   CHRESIST101   |                   Chip Resistor                   |    DIGIKEY    |   ERJ-8GEYJ102V  |  2  |  Piece |   $0.14   |  $0.28  |
|            2.9            |  CARBRESIST100  |                    1k Resistor                    |    DIGIKEY    |  CFR-25JB-52-1K  |  3  |  Piece |   $0.01   |  $0.03  |
|            2.10           |  CARBRESIST101  |                   2.2k Resistor                   |    DIGIKEY    |  CFR-25JR-52-2K2 |  1  |  Piece |   $0.01   |  $0.01  |
|            2.11           |    ARDNANO100   |                    Arduino Nano                   |    Arduino    |      A000005     |  1  |  Piece |   $24.90  |  $24.90 |
| 3                         |  LINMOTORBRK100 |                      Assembly                     |      None     |       None       |  1  |  Assy  |   $0.00   |  $0.00  |
|            3.1            |     STLSH100    |              12" X 18"   Steel sheet              |     Lowes     |       44487      |  1  |  Stick |   $9.48   |  $9.48  |
|            3.2            |    STLROD100    |                3/8"X3' Steel   Rod                |     Lowes     |       44079      |  1  |  Stick |   $7.48   |  $7.48  |
|            3.3            |     BOLT100     |                        Bolt                       |     Lowes     |       61820      |  8  |  Piece |   $0.15   |  $1.20  |
|            3.4            |     WASH100     |                       Washer                      |     Lowes     |       63306      |  8  |  Piece |   $0.15   |  $1.20  |
|            3.5            |      NUT100     |                        Nut                        |     Lowes     |       63301      |  8  |  Piece |   $0.10   |  $0.80  |
| 4                         | LINMOTORASSY100 |                      Assembly                     |      None     |       None       |  1  |  Assy  |   $0.00   |  $0.00  |
|            4.1            |   LINMOTOR100   |                    Linear Motor                   |     Pololu    | GF23-120502-3-65 |  1  |  Piece |  $183.95  | $183.95 |
|            4.2            |      MG100      |           Magnet - 2" by 0.125" Thickness         |  kjmagnetics  |     DY04-N52     |  2  |  Piece |   $28.44  |  $56.88 |
|            4.3            |      ADH100     |                      Adhesive                     |     Lowes     |       50112      |  1  | Bottle |   $7.98   |  $7.98  |
|            4.4            |   STLFLTBAR100  |                  Flat Bar - Steel                 |     Lowes     |      216190      |  1  |  Stick |   $12.98  |  $12.98 |
|            4.5            |     BOLT100     |                        Bolt                       |     Lowes     |       61820      |  4  |  Piece |   $0.15   |  $0.60  |
|            4.6            |     WASH100     |                       Washer                      |     Lowes     |       63306      |  4  |  Piece |   $0.15   |  $0.60  |
|            4.7            |      NUT100     |                        Nut                        |     Lowes     |       63301      |  4  |  Piece |   $0.10   |  $0.40  |
| 4.8                       |   LINMTRMNT100  |                 Linear Motor Mount                |     Pololu    |       2328       |  1  |   Set  |   $39.45  |  $39.45 |
|                           |                 |                                                   |               |                  |     |        |           |  $0.00  |
|                           |                 |                                                   |               |                  |     |        |           |  $0.00  |
|                           |                 |                                                   |               |                  |     |        |   Total   | $427.48 |




### References:

[1]	A. H. C. Gosline and V. Hayward, "Eddy Current Brakes for Haptic Interfaces: Design, 	Identification, and Control," in IEEE/ASME Transactions on Mechatronics, vol. 13, no. 	6, pp. 669-677, Dec. 2008, doi: 10.1109/TMECH.2008.2004623.

[2]	“How to Start an Exercise Program,” American Council on Exercise, vol. FF, 2013. 

[3]	R. Gregor and L. Childers, “4,” in Neuromechanics of the Cycling Task, Blackwell 	Publishing Ltd, 2011, pp. 52–77.

[4]	RC;, H. (1989, March). Contact pressures in the patellofemoral joint during impact loading on the human flexed knee. Journal of orthopaedic research: official publication of the Orthopaedic Research Society. Retrieved November 19, 2022, from https://pubmed.ncbi.nlm.nih.gov/2918426/

[5]	Magnetic Dipole Moment. [Online]. Available: https://www.kjmagnetics.cm/blog.asp?p=dipole. 






