# Mario Kart Rev 2 - Signoff - Mario Kart Bike Wireless Sensors Subsystem 
## Team 4 - Blake Pickett ##

_Function of the Subsystem:_

The function of the newly designed feature is to convert the speed and steering sensors, the right and left handle bar buttons, and the microcontrollers on the Mario Kart Bike to be wireless. These sensors will gather data, convert it, and send it via Bluetooth to the master microcontroller, the Raspberry Pi (RPi). Each sensor will be given its own microcontroller, an Arduino Nano 33 BLE for both the steering and speed sensor in order to utilize Bluetooth 5 communication to the central RPi. Coding of the individual microcontrollers and their Bluetooth modules will be accomplished through the use of Arduino IDE text editor. This new feature will mitigate safety risks to the Mario Kart Bike riders by eliminating the long wires running down the bike and around the bike stand as well as improve the aesthetic form of the product. These long wires are a safety hazard for future customers. The wires that rectify and step down the power for the sensors on the current version of the Mario Kart Bike will be replaced with a fourth-D-battery holder, complete with four D batteries that will produce 6 V and 6.25 A current to the sensors and microcontrollers. The four D batteries will power the microcontroller, which will power the sensors, for six hours of constant use. 

_Constraints:_ 

The wireless capability provided by the new design requires the removal of the long wires along the bike. Although eliminating the long wires mitigates a safety risk to Mario Kart Bike riders, the equipment must still have power to work properly. Therefore, the long wires will be replaced with batteries. Multiple batteries will supply the DC voltage and current needed to power the equipment for six hours of constant use.   

**Speed Sensor:** The KY-032 Obstacle Avoidance Sensor must have a DC voltage between 3.3 V and 5 V to operate correctly. Likewise, the KY-032 Obstacle Avoidance Sensor must have a minimum of 20 mA of current to operate correctly. The Nano 33 BLE and Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V.  

**Steering Sensor:** The Potentiometer voltage must be the same as the analog input, so the voltage for the Potentiometer must be the same as the analog to digital converter (ADC), microcontroller, and Bluetooth module. The ADC has a maximum voltage of 5.5 V and a minimum of 0 V. The Nano Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V. During the fabrication of the new design, analysis will be performed to ensure that safety risks have been mitigated. Although the long wires will be replaced to mitigate the risk resulting from the potential trip hazard, analysis will be performed to ensure that the batteries are not inducing an unacceptable level of voltage or current onto the Mario Kart Bike frame, posing a potential safety risk to the rider.   

**Data Transfer Method:** To improve the physical design of the Mario Kart bike and clean up the exposed wiring to create a form that is more like commercial products, communication between the sensors and main RPi shall be wireless.

**Latency:** Communication latency from data sensors to central microcontroller must be at maximum 40 ms.

_Buildable Schematic:_     

The wiring schematics for the speed and steering sensors are provided in **Figures 1** and **2**. The schematics are also uploaded to the Capstone Design documentation folder. 

![image](https://user-images.githubusercontent.com/113309616/216878265-85b9dd64-0cbd-4305-849b-ddae6a2e561f.png)

**Figure 1.** Wiring Schematic for the Speed Sensor

 ![image](https://user-images.githubusercontent.com/113309616/216878290-5532345e-a4e5-4ac4-8371-c4b1a3d5df2e.png)

**Figure 2.** Wiring Schematic for the Steering Sensor

_Analysis:_ 

An analysis verified that the existing steering and speed sensors installed on the Mario Kart Bike perform to specification, meeting both the technical requirements and ethical constraints for user safety. The results of the analysis indicate that the sensors are adequate to meet the intended performance, including the enhanced resistance and trail ride features. After verifying the adequacy of the speed and steering sensors, a design adds the convenience of wireless connectivity.   

**Power Supply for Wireless Connectivity:** To assist in the verification of wireless capability for the speed and steering sensors, schematics provide illustrations for visual analysis of the design, including a satisfactory, functional means of mounting the batteries needed to achieve the required voltage. Additionally, the use of mathematical calculations enabled the verification of the quantity of batteries needed to provide the required voltage range. Since a single D battery provides 1.5 V and 6.25 A, four batteries will provide 6 V and 6.25 A, which is sufficient voltage within the required range and the required current. Based on the datasheet, the maximum current used by the microcontroller, which powers the sensors, is 1 Ah. Therefore, four D batteries provide sufficient current to power each microcontroller using 1 Ah for six hours of constant use. The dimensions of the battery holders, measuring 5.5 inches (L) by 2.8 inches (w) by 1.2 inches (h), are small and compact, avoiding the trip hazard posed by the long wires installed on the previous version of the Mario Kart Bike. Additionally, zip ties will neatly and securely mount the battery holder to the Mario Kart bike frame, further promoting the safety of the Mario Kart Bike user. 

**Bluetooth Connectivity:** Investigation determined that Bluetooth LE connectivity for the steering sensor’s microcontroller can use the sensor in conjunction with the ADS 1015 and Potentiometer as well as the left and right handlebar buttons on the bike. Analysis also determined that power constraint must also be addressed, as an investigation revealed that some Arduino microcontrollers surpass the 5 V limit while others are at 5 V exactly. The Arduino Nano 33 BLE, a low power microcontroller with an integrated Bluetooth module, was selected. The Nano 33 BLE satisfies the power constraint, although it is Arduino’s smallest board, measuring at 45 mm by 18 mm. Size is an important aspect due to the location of the microcontrollers being along the metal pipes of the bike. 

**Latency:** Communication between the sensors and the central RPi must satisfy the latency constraint of 40 ms. Bluetooth LE has a range of transmission of about 50 m, and a data throughput of 0.27 Mbps. To calculate expected max latency, we look at the worst case scenario. Network latency can be calculated with the following formula [2]:

Latency=(d/v)+(s/r)

where:

d = distance of communication in m

v = speed of transmission medium in m/s

s = packet size in bits

r = data transmission rate in Kbps

In the worst case, the maximum distance equals the distance from the central RPi to the speed sensor, which is about 2.44 m. The transmission of Bluetooth LE is equivalent to radio waves through air, which has a speed of 3 * 10^8 m/s. The MTU (maximum transfer unit) of BLE is 184 bits. Finally, the data transmission rate of the Nano 33 BLE is 270 Kbps. This gives a max transmission latency of 0.68 ms.

**Speed Sensor Microcontroller:** Analysis determined that another Nano 33 BLE will be appropriate for the speed sensor’s microcontroller, which will be used in conjunction with the KY-032 infrared sensor in order to accurately measure the speed of the rear wheel. Our investigation also determined that the KY-032 sensor can be properly used by using the enable pin, which should not be active for more than 2 ms at a time due to the receiver quickly saturating when active [1].  

**Strobing of Receiver:** Investigation revealed that strobing of the receiver can be programmed. Because the IR light is emitted at a frequency of 38 kHz [1], the receiver (HS0038B) must be cycling at 76 kHz (as a minimum) to satisfy the Nyquist sampling rate. As stated before, this strobe rate can be programmed manually. By determining the time between any two high readings (two markings) and multiplying this time by the number of individual markings, the time required to perform each revolution of the flywheel can be calculated. 

(Time between two highs)*(Number of markings)=Time for 1 revolution

This number can be converted to revolutions per second (or minute) in the flywheel. By using the gearing ratio between the flywheel and the bike tire, the current revolutions per second (or minute) at the bike tire can be calculated. This calculation will constantly update, taking place between each individual marking, in order to be as precise as possible. This calculated number will be transmitted via Bluetooth LE to the main RPi for other functions.

**Coding:** Investigation determined that Coding of the Bluetooth modules and their respective microcontrollers can be accomplished in the Arduino IDE. Arduino IDE supports the programming languages C++ and C. Designation of microcontrollers is important, with the sensor’s microcontrollers being peripheral, strictly sending data. The RPi housed in the main component box will be the central microcontroller, or master, primarily receiving data from the peripheral microcontrollers and potentially controlling them if necessary.

**Profiles:** Investigation confirmed that Bluetooth LE uses a concept of profiles as specification for Bluetooth communication by creating rules that allow certain tasks to be accomplished. The sensors will be strictly sending bit data to a central RPi, so the Serial Port Profile (SPP) will be used. Based on an analysis, this profile will define how to set up virtual serial ports and connect two Bluetooth LE enabled devices. 

Based on analysis and investigation of the design using the schematic and mathematical calculations, the materials needed to implement the new design of the speed and steering sensors were priced. The most economical option for purchasing the batteries was selected to ensure adequate quantities for the initial testing, standard use, and spares. The price for these materials was reviewed against the proposed budget and determined to be within range. 

_BOM:_ 

The bill of materials (BOM) to accomplish the design illustrated in the schematics is provided in **Table 1**. 

**Table 1.** Bill of Materials
| Brand / Manufacturer       | Part Name              | Supplier | Part / Model # or ASIN # | Qty | Units  | Unit Cost | Cost   |
| -------------------------- | ---------------------- | -------- | ------------------------ | --- | ------ | --------- | ------ |
| SDTC Tech                  | 4 D Battery Holders    | Amazon   | B08594HCR5               | 2   | Pieces | $4.45     | $8.90  |
| Duracell                   | 8 Pack D Battery       | Amazon   | B00164H4AI               | 3   | Pack   | $15.87    | $47.61 |
| HMROPE                     | 8 Inch Zip Ties        | Amazon   | TXLAC                    | 1   | Pack   | $9.18     | $9.18  |
| Duck                       | Electrical Tape        | Amazon   | 282289                   | 1   | Roll   | $1.48     | $1.48  |
| Arduino                    | Nano 33 BLE            | Arduino  | ABX00030                 | 2   | Pieces | $26.30    | $52.60 |

**References**

[1]	_IR sensor for obstacle avoidance KY-032 (AD-032)_. IR Senor Obstacle Avoidance Keyes KY 032. (n.d.). Retrieved February 5, 2023, from http://irsensor.wizecode.com/ 

[2] _“RF Wireless World,” Network Latency Calculator | Network Latency Formula._ [Online].   Available: https://www.rfwireless-world.com/calculators/Network-Latency-Calculator.html. [Accessed: 08-Feb-2023]. 
