# Mario Kart Rev 2 - Signoff - Mario Kart Bike Wireless Sensors Subsystem 
## Team 4 - Blake Pickett ##

_Function of the Subsystem:_

The function of the newly designed feature is to enable Bluetooth LE (BLE) connectivity between sensors and central Raspberry Pi (RPi). These sensors will gather, convert, and send data via BLE (achieved with usage of Arduino Nano 33 BLEs for each sensor) to the master RPi. The wires that rectify and step down the power for the sensors on the current version of the Mario Kart Bike will be replaced with four AA batteries and a holder. The four AA batteries will provide 6 V and 3500 mAh to the microcontrollers, which will power the sensors for more than 56 hours of constant use.   
<br/><br/>

_Constraints:_ 

**Run Time:**

Batteries must supply the DC voltage and current needed to power the equipment for 2 weeks. The equipment shall be able to with stand a minimum of 4 hours of constant use each day during the 2 weeks.     

**Speed Sensor:** 

The KY-032 Obstacle Avoidance Sensor must have a DC voltage between 3.3 V and 5 V, and a minimum of 20 mA to operate correctly.

The Nano 33 BLE and Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V.    

**Steering Sensor:** 

The Potentiometer voltage must be the same as the analog input, so the voltage for the Potentiometer must be the same as the analog to digital converter (ADC), microcontroller, and Bluetooth module.  

The ADC has a maximum voltage of 5.5 V and a minimum of 0 V.

The Nano Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V. 

**Data Transfer Method:**

Communication between the sensors and main RPi must be wireless. Each sensor must have a corresponding Nano 33 BLE in order to achieve BLE communication.

**Latency:**

Communication latency from data sensors to central microcontroller must be at maximum 40 ms.

<br/><br/>
_Buildable Schematic:_     

The wiring schematics for the speed and steering sensors are provided in **Figures 1** and **2**. The schematics are also uploaded to the Capstone Design documentation folder. 

![image](https://user-images.githubusercontent.com/113309616/220494178-c5e14414-511d-449e-95d0-ec3b243dd7b5.png)

**Figure 1.** Wiring Schematic for the Speed Sensor
<br/><br/>

![image](https://user-images.githubusercontent.com/113309616/220494226-476a8e46-283e-40fd-8b5c-526227e72f9a.png)

**Figure 2.** Wiring Schematic for the Steering Sensor

<br/><br/>
_Analysis:_ 

<br/><br/>
![image](https://user-images.githubusercontent.com/113309616/218646430-f175fa4a-9542-4cb2-b9a1-f2d0cc75ad1e.png)

**Figure 3.** Arduino Nano 33 BLE Power Tree [1]
<br/><br/>

![image](https://user-images.githubusercontent.com/113309616/220494294-73fe94d5-aafb-4356-90a7-1e8f4506c187.png)

**Figure 4.** Table 5.2.1.1 Sleep [2]
<br/><br/>

**Power Supply for Wireless Connectivity:** 
<br/><br/>

_Speed Sensor:_

   * Tachometer = 10 mA

   * Arduino Nano 33 BLE Default Settings = 17 mA

   * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on GPIOTE event) = 0.01737 mA 

   * AA Battery Current = 3500 mAh

   * AA Battery Voltage = 1.5 V
<br/><br/>
        - Current needed (running) = 10 + 17 = 27 mA

        - Total Voltage = 1.5 * 4 = 6 volts 

        - Total Amp-Hours Needed = (27 * 56) + (0.01737 * 280) = 1516.86 mAh  
<br/><br/>

_Speed Sensor Run Time:_

Power can be preserved by turning on and off the tachometer (GPIO Pin 22 is connected to KY-032 enable pin, causing ground connection at low input), power LED, and I2C pull-up resistors when needed (done in software) [3][4]. The Arduino Nano 33 BLE will go into sleep mode after tachometer, power LED, and I2C pull-up resistors are turned off. The Nano can be woken via a GPIO interrupt event.

The speed sensor will use 1517 mAh in 2 weeks of use. Four AA batteries will provide 6 V and 3500 mAh, which is sufficient to run the speed sensor equipment for 2 weeks including the 4 hours of constant use each day. 

<br/><br/>
_Steering Sensor:_

   *	Max Potentiometer = 7 mA

   *	ADS1015 = 0.09091 mA 

   *  Arduino Nano 33 BLE Default Settings = 17 mA

   *  Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on GPIOTE event) = 0.01737 mA  

   *	AA Battery Current = 3500 mAh

   *	AA Battery Voltage = 1.5 V
<br/><br/>
         - Current needed (running) = 7+ 0.09091 + 17 = 24.09091 mA

         - Total Voltage = 1.5 * 4 = 6 volts 

         - Total Amp-Hours Needed = (24.09091 * 56) + (0.01737 * 280) = 1353.95 mAh           
<br/><br/>

_Steering Sensor Run Time:_

Power can be preserved by turning on and off the potentiometer (Nano GPIO Pin 20), ADS1015 (same pin), power LED, and I2C pull-up resistors when needed (done in software)[3][4]. The Arduino Nano 33 BLE will go into sleep mode after the potentiometer, ADS1015, power LED, and I2C pull-up resistors are turned off. The Nano can be woken via a GPIO interrupt event.

The steering sensor will use 1354 mAh in 2 weeks of use. Four AA batteries will provide 6 V and 3500 mAh, which is sufficient to run the steering sensor equipment for 2 weeks including 4 hours of constant use each day. 

Dimensions of the battery holders are 2.248 inches (L) by 2.457 inches (w) by 0.622 inches (h). The holders are small/compact to avoid the trip hazard posed by the long wires. Zip ties will securely mount the battery holder to the bike frame.

<br/><br/>
**Strobing of Receiver:** 

IR light is emitted from the KY-032 at a frequency of 38 kHz [5], so the receiver (HS0038B) must be cycling at 76 kHz (as a minimum) to satisfy the Nyquist sampling rate. This strobe rate can be programmed manually.  The KY-032 sensor will use the enable pin, which should not be active for more than 2 ms at a time due to the receiver quickly saturating when active [5].

By determining the time between any two high readings (two markings) and multiplying this time by the number of individual markings, the time required to perform each revolution of the flywheel can be calculated (this calculation will update between every 2 high readings).  

   - (Time between two highs)*(Number of markings)=Time for 1 revolution

By using the gearing ratio between the flywheel and the bike tire, the current revolutions per second (or minute) at the bike tire can be calculated.  

<br/><br/>
**Bluetooth Connectivity:**

BLE connectivity for the steering sensor’s microcontroller can use the sensor in conjunction with the ADS 1015 and Potentiometer as well as the left and right handlebar buttons on the bike.  

Arduino microcontrollers surpass the 5 V limit while others are at 5 V exactly. The Arduino Nano 33 BLE satisfies the power constraint. The Nano 33 BLE measures 45 mm by 18 mm and will within the space constraints of the Mario Kart Bike’s long metal pipes.  

<br/><br/>
**Latency:**

Latency of communication shall be 40 ms. Network latency can be calculated with the following formula [6]:

   - Latency=(d/v)+(s/r)

where:

d = distance of communication in m

v = speed of transmission medium in m/s

s = packet size in bits

r = data transmission rate in Kbps

In the worst case, the distance equals 2.44 m (central RPi to speed sensor). The transmission speed of Bluetooth LE is 3 * 10^8 m/s (radio waves through air). The maximum transfer unit (MTU) of BLE is 184 bits. Finally, the data transmission rate of the Nano 33 BLE is 270 Kbps. This gives a max transmission latency of 0.68 ms.

<br/><br/>
**Coding:**

Coding of the Bluetooth modules and their respective microcontrollers can be accomplished in the Arduino IDE, which supports the programming languages C++ and C. 

Designation of microcontrollers is important, with the sensor’s microcontrollers being peripheral, strictly sending data. 

The RPi housed in the main component box will be the central microcontroller, or master, primarily receiving data from the peripheral microcontrollers and potentially controlling them if necessary.

<br/><br/>
**Profiles:**

Bluetooth LE uses a concept of profiles as specification for Bluetooth communication by creating rules that allow certain tasks to be accomplished. The sensors will send bit data to a central RPi, so the Serial Port Profile (SPP) will be used. This profile will define how to set up virtual serial ports and connect two Bluetooth LE enabled devices. 

<br/><br/>
_BOM:_ 

The bill of materials (BOM) to accomplish the design illustrated in the schematics is provided in **Table 1**. 

**Table 1.** Bill of Materials
| Brand / Manufacturer       | Part Name                    | Supplier | Part / Model # or ASIN # | Qty | Units  | Unit Cost | Cost   |
| -------------------------- | ---------------------------- | -------- | ------------------------ | --- | ------ | --------- | ------ |
| LAMPVPATH                  | 4 AA Battery Holders         | Amazon   | B07L9M6VZK               | 1   | Pack   | $7.49     | $7.49  |
| Energizer                  | 24 Pack AA Lithium Batteries | Amazon   | B07BMH7RDP               | 1   | Pack   | $65.35    | $65.35 |
| HMROPE                     | 8 Inch Zip Ties              | Amazon   | TXLAC                    | 1   | Pack   | $9.18     | $9.18  |
| Duck                       | Electrical Tape              | Amazon   | 282289                   | 1   | Roll   | $1.48     | $1.48  |
| Arduino                    | Nano 33 BLE                  | Arduino  | ABX00030                 | 2   | Pieces | $26.30    | $52.60 |

<br/><br/>
**References** 

[1] Team, T. A. (n.d.). _Arduino docs: Arduino Documentation._ Arduino Docs | Arduino Documentation. Retrieved February 13, 2023, from https://docs.arduino.cc/ 

[2]	_Arduino._ (n.d.). Retrieved February 21, 2023, from https://content.arduino.cc/assets/Nano_BLE_MCU-nRF52840_PS_v1.1.pdf

[3] _How to reduce power consumption on the nano 33 ble._ (n.d.). Retrieved February 21, 2023, from https://support.arduino.cc/hc/en-us/articles/4402394378770-How-to-reduce-power-consumption-on-the-Nano-33-BLE 

[4]	_Arduino® Nano 33 ble._ (n.d.). Retrieved February 21, 2023, from https://docs.arduino.cc/resources/datasheets/ABX00030-datasheet.pdf 

[5]	_IR sensor for obstacle avoidance KY-032 (AD-032)._ IR Senor Obstacle Avoidance Keyes KY 032. (n.d.). Retrieved February 5, 2023, from http://irsensor.wizecode.com/

[6] _RF Wireless World._ Network Latency Calculator | Network Latency Formula. (n.d.). Retrieved February 13, 2023, from https://www.rfwireless-world.com/calculators/Network-Latency-Calculator.html 
