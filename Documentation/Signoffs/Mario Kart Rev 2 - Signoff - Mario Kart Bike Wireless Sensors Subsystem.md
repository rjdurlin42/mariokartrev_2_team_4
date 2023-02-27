# Mario Kart Rev 2 - Signoff - Mario Kart Bike Wireless Sensors Subsystem 
## Team 4 - Blake Pickett and Sage Mooneyham ##
<br/><br/>
### _Function of the Subsystem:_ ###

The function of the newly designed feature is to enable Bluetooth LE (BLE) connectivity between sensors and central Raspberry Pi (RPi). These sensors will gather, convert, and send data via BLE (achieved with usage of Arduino Nano 33 BLEs for each sensor) to the master RPi. The wires that rectify and step down the power for the sensors on the current version of the Mario Kart Bike will be replaced with batteries and a holder. The 4 AA batteries will provide 6 V and 3500 mAh to the microcontroller, which will power the speed sensor for more than 2 weeks. The 4 AAA batteries will provide 6 V and 1300 mAh to the microcontroller, which will power the speed sensor for more than 2 weeks.    
<br/><br/>

### _Constraints:_ ###

* **Run Time:**
  * Batteries must supply the DC voltage and current needed to power the equipment for 2 weeks. The equipment shall be able to with stand a minimum of 4 hours of constant use each day during the 2 weeks.     

* **Speed Sensor:** 
  * The KY-032 Obstacle Avoidance Sensor must have a DC voltage between 3.3 V and 5 V, and a minimum of 10 mA to operate correctly.
  * The Nano 33 BLE and Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V.     

* **Steering Sensor:** 
  * The Potentiometer voltage must be the same as the analog input, so the voltage for the Potentiometer must be the same as the analog to digital converter (ADC), microcontroller, and Bluetooth module.   
  * The ADC has a maximum voltage of 5.5 V and a minimum of 0 V.
  * The Nano Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V.  

* **Data Transfer Method:**
  * Communication between the sensors and main RPi must be wireless. Each sensor must have a corresponding Nano 33 BLE in order to achieve BLE communication.

* **Latency:**
  * Communication latency from data sensors to central microcontroller must be at maximum 40 ms.

<br/><br/>
### _Buildable Schematic:_  ###   

The wiring schematics for the speed and steering sensors are provided in **Figures 1** and **2**. The schematics are also uploaded to the Capstone Design documentation folder. 

![image](https://user-images.githubusercontent.com/113309616/221471146-13a9a91d-449d-4cfe-84f9-6e5308a85983.png)

**Figure 1.** Wiring Schematic for the Speed Sensor
<br/><br/>

![image](https://user-images.githubusercontent.com/113309616/221471197-902003cb-8d6e-47b9-b3a4-122cded22a2a.png)

**Figure 2.** Wiring Schematic for the Steering Sensor

<br/><br/>
### _Analysis:_ ### 

<br/><br/>
![image](https://user-images.githubusercontent.com/113309616/218646430-f175fa4a-9542-4cb2-b9a1-f2d0cc75ad1e.png)

**Figure 3.** Arduino Nano 33 BLE Power Tree [1]
<br/><br/>

![image](https://user-images.githubusercontent.com/113309616/221471259-f36d58d3-a2b8-4779-a43e-4b6c99f4a270.png)

**Figure 4.** Arduino Nano 33 BLE Sleep Mode Current Draws[2]
<br/><br/>
<br/><br/>

* **Power Supply for the Speed Sensor:** 
<br/><br/>

  * **_Speed Sensor Batteries:_**
  
      * AA Battery Current = 3500 mAh
      * AA Battery Voltage = 1.5 V
      * Total AA Batteries Voltage = 1.5 * 4 = 6 V
      * Total AA Batteries Wattage = 6 * 3500 = 21000 mWh

  * **_Speed Sensor Current:_**
    
      * Tachometer = 10 mA
      * Arduino Nano 33 BLE Default Settings = 17 mA
      * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on RTC event) = 0.00316 mA  
      * Current Leakage on IO pins (sleep) = 0.01 mA
    <br/><br/>
         * Current needed (running) = 10 + 17 = 27 mA
         * Current needed (Sleeping) = 0.01 + 0.00316 = 0.01316 mA
          * Total Amp-Hours Needed = (27 * 56) + (0.01316  * 280) = 1515.685 mAh   
        
    The speed sensor will use 1516 mAh in 2 weeks of use, which is less than the 3500 mAh that the battery can supply.    
<br/><br/>

  * **_Speed Sensor Voltage:_**
<br/><br/>
    ![image](https://user-images.githubusercontent.com/113309616/221472032-5c0c6b44-f4f6-4835-9229-a8cb58c2fd84.png)

    **Figure 5.** Discharge of the Ultimate Lithium Energizer AA Battery [3]

    From **Figure 5**, the voltage from of a battery discharging 10 mA or 100 mA drops from 1.5 V to 1.3 V. 

     * Total Voltage Before Discharging =  1.5 * 4 = 6 V 
     * Total Voltage After Discharging =  1.3 * 4 = 5.2 V 

    Therefore, the voltage will stay above the 5 V cutoff voltage of the Arduino Nano 33 BLE even when the batteries have dissipated the full 3500 mAh.

    The input voltage will be regulated by the voltage regulator on the Arduino Nano 33 BLE to 3.3 V. 
    <br/><br/>

  * **_Speed Sensor Power:_**

    * Tachometer = 10 * 3.3 = 33 mW
    * Arduino Nano 33 BLE Default Settings = 17 * 6 = 102 mW
    * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on RTC event) = 0.00316  * 6 = 0.01896 mW 
    * Current Leakage on IO pins (sleep) = 0.01 * 3.3 = 0.033 mW
    <br/><br/>
       - Watts needed (running) = 33 + 102 = 135 mW  
       - Watts needed (sleeping) = 0.033 + 0.01896 = 0.05196 mW
       - Total Watt-Hours Needed = (135 * 56) + (0.05196 * 280) = 7574.5488 mWh  

    The speed sensor will use 7575 mWh in 2 weeks of use. Four AA batteries will provide 21000 mWh, which is sufficient to run the speed sensor equipment for 2 weeks including the 4 hours of constant use each day.
    <br/><br/>

  * **_Speed Sensor Run Time:_**

    Power can be preserved by turning on and off the tachometer (GPIO Pin 22 is connected to KY-032 enable pin, causing ground connection at low input), power LED, and I2C pull-up resistors when needed (done in software) [4][5]. To control the state of the sensor, remove the jumper and use the EN pin, a HIGH signal will enable the sensor and a LOW signal will disable it [6]. The Arduino Nano 33 BLE will go into sleep mode after tachometer, power LED, and I2C pull-up resistors are turned off. This sleep mode is awoken by event using the RTC timer on the nRF52840 processor. Every 10 (this number is chosen to connect in a timely fashion if user wants to activate the controller, while keeping Nano in sleep a majority of the time) seconds, the Nano used for speed data communication will check to see if the central RPi is looking for connection (this means user is attempting to use device). If central RPi is not broadcasting for connection, the Nano will reenter sleep mode (RTC counter).

    Dimensions of the battery holders are 2.248 inches (L) by 2.457 inches (w) by 0.622 inches (h). The holders are small/compact to avoid the trip hazard posed by the long wires. Zip ties will securely mount the battery holder to the bike frame. 
    <br/><br/>
    <br/><br/>
    
* **Power Supply for the Steering Sensor:**
    <br/><br/>
    * **_Steering Sensor Batteries:_**

      * AAA Battery Current = 1300 mAh
      * AAA Battery Voltage = 1.5 V
      * Total AAA Batteries Voltage = 1.5 * 4 = 6 V
      * Total AAA Batteries Wattage = 6 * 1300 = 7800 mWh

    * **_Steering Sensor Current:_**
    
      * Max Potentiometer = 10k ohms = 3.3/10000 = 0.33 mA
      * ADS1015 = 0.3 / 3.3 = 0.09091 mA 
      * Arduino Nano 33 BLE Default Settings = 17 mA
      * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on GPIOTE event) = 0.01737 mA    
      * Current Leakage on IO pins (sleep) = 0.01 mA
        <br/><br/>
         - Current needed (running) = 0.33 + 0.09091 + 17 = 17.421 mA
         - Current needed (Sleeping) = 0.01 + 0.01737  = 0.02737 mA
         - Total Amp-Hours Needed = (17.421 * 56) + (0.02737 * 280) = 983.2396 mAh   

      The steering sensor will use 984 mAh in 2 weeks of use, which is less than the 1300 mAh that the battery can supply.  
      <br/><br/>

    * **_Steering Sensor Voltage:_**

      ![image](https://user-images.githubusercontent.com/113309616/221475245-cdd4e366-64b1-4f36-ba3c-69a6f3054803.png)

      **Figure 7.** Discharge of the Ultimate Lithium Energizer AAA Battery [7]

      From **Figure 7**, the voltage from of a battery discharging 10 mA or 100 mA drops from 1.5 V to 1.3 V. 

         * Total Voltage Before Discharging =  1.5 * 4 = 6 V 
         * Total Voltage After Discharging =  1.3 * 4 = 5.2 V 

      Therefore, the voltage will stay above the 5 V cutoff voltage of the Arduino Nano 33 BLE even when the batteries have dissipated the full 1300 mAh.

      The input voltage will be regulated by the voltage regulator on the Arduino Nano 33 BLE to 3.3 V. 
      <br/><br/>

    * **_Steering Sensor Power:_**

        * Max Potentiometer = 0.33 * 3.3 = 1.089 mW
        * ADS1015 = 0.3 mW
        * Arduino Nano 33 BLE Default Settings = 17 * 6 = 102 mW
        * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on GPIOTE event) = 0.01737 * 5 = 0.08685 mW 
        * Current Leakage on IO pins (sleep) = 0.01 * 3.3 = 0.033 mW
        <br/><br/>
            - Watts needed (running) = 1.089 + 0.3 + 102 = 103.389 mW
            - Watts needed (sleeping) = 0.033 + 0.08685 = 0.11985 mW
            - Total Watt-Hours Needed = (103.389 * 56) + (0.11985 * 280) = 5823.342 mWh

        The speed sensor will use 5824 mWh in 2 weeks of use. Four AA batteries will provide 7800 mWh, which is sufficient to run the speed sensor equipment for 2 weeks including the 4 hours of constant use each day.
        <br/><br/>

    * **Steering Sensor Run Time:**

      Power can be preserved by turning on and off the potentiometer (Nano GPIO Pin 20), ADS1015 (same pin), power LED, and I2C pull-up resistors when needed (done in software)[4][5]. The Arduino Nano 33 BLE will go into sleep mode after the potentiometer, ADS1015, power LED, and I2C pull-up resistors are turned off. The Nano can be woken via a GPIO interrupt event. The GPIO interrupt event that will awaken the switch will be on pin 25 as well as 26 (left and right handlebar button). When the user presses either/both of these, the Nano will wake from sleep, and connect to the central RPi. 

      Dimensions of the battery holders are 2.441 inches (L) by 1.909 inches (w) by 0.626 inches (h). The holders are small/compact to avoid the trip hazard posed by the long wires. Zip ties will securely mount the battery holder to the bike frame.
      <br/><br/>

  * **Strobing of Receiver:** 

    IR light is emitted from the KY-032 at a frequency of 38 kHz [8], so the receiver (HS0038B) must be cycling at 76 kHz (as a minimum) to satisfy the Nyquist sampling rate. This strobe rate can be programmed manually.  The KY-032 sensor will use the enable pin, which should not be active for more than 2 ms at a time due to the receiver quickly saturating when active [8].

    By determining the time between any two high readings (two markings) and multiplying this time by the number of individual markings, the time required to perform each revolution of the flywheel can be calculated (this calculation will update between every 2 high readings).   

      - (Time between two highs)*(Number of markings)=Time for 1 revolution

    By using the gearing ratio between the flywheel and the bike tire, the current revolutions per second (or minute) at the bike tire can be calculated.   
    <br/><br/>

  * **Bluetooth Connectivity:**

    BLE connectivity for the steering sensor’s microcontroller can use the sensor in conjunction with the ADS 1015 and Potentiometer as well as the left and right handlebar buttons on the bike.   

    Arduino microcontrollers surpass the 5 V limit while others are at 5 V exactly. The Arduino Nano 33 BLE satisfies the power constraint. The Nano 33 BLE measures 45 mm by 18 mm and will within the space constraints of the Mario Kart Bike’s long metal pipes.   
    <br/><br/>

 * **Latency:**

    Latency of communication shall be 40 ms. Network latency can be calculated with the following formula [9]:

      - Latency=(d/v)+(s/r)

    where:

    d = distance of communication in m

    v = speed of transmission medium in m/s

    s = packet size in bits

    r = data transmission rate in Kbps

    In the worst case, the distance equals 2.44 m (central RPi to speed sensor). The transmission speed of Bluetooth LE is 3 * 10^8 m/s (radio waves through air). The maximum transfer unit (MTU) of BLE is 184 bits. Finally, the data transmission rate of the Nano 33 BLE is 270 Kbps. This gives a max transmission latency of 0.68 ms.
    <br/><br/>

 * **Coding:**

    Coding of the Bluetooth modules and their respective microcontrollers can be accomplished in the Arduino IDE, which supports the programming languages C++ and C.  

    Designation of microcontrollers is important, with the sensor’s microcontrollers being peripheral, strictly sending data.  

    The RPi housed in the main component box will be the central microcontroller, or master, primarily receiving data from the peripheral microcontrollers and potentially controlling them if necessary.
    <br/><br/>

  * **Profiles:**

    Bluetooth LE uses a concept of profiles as specification for Bluetooth communication by creating rules that allow certain tasks to be accomplished. The sensors will send bit data to a central RPi, so the Serial Port Profile (SPP) will be used. This profile will define how to set up virtual serial ports and connect two Bluetooth LE enabled devices. 

<br/><br/>
### _BOM:_ ### 

The bill of materials (BOM) to accomplish the design illustrated in the schematics is provided in **Table 1**. 

**Table 1.** Bill of Materials
| Brand / Manufacturer       | Part Name                    | Supplier | Part / Model # or ASIN # | Qty | Units  | Unit Cost | Cost   |
| -------------------------- | ---------------------------- | -------- | ------------------------ | --- | ------ | --------- | ------ |
| LAMPVPATH                  | 4 AA Battery Holders         | Amazon   | B07L9M6VZK               | 1   | Pack   | $7.49     | $7.49  |
| Energizer                  | 12 Pack AA Lithium Batteries | Amazon   | B0044P3J2I               | 1   | Pack   | $37.49    | $37.49 |
| LAMPVPATH                  | 4 AAA Battery Holders        | Amazon   | B076HRBFG7               | 1   | Pack   | $8.99     | $8.99  |
| Energizer                  | 12 Pack AAA Lithium Batteries| Amazon   | B06ZYWKBRB               | 1   | Pack   | $26.99    | $26.99 |
| HMROPE                     | 8 Inch Zip Ties              | Amazon   | TXLAC                    | 1   | Pack   | $9.18     | $9.18  |
| Duck                       | Electrical Tape              | Amazon   | 282289                   | 1   | Roll   | $1.48     | $1.48  |
| Arduino                    | Nano 33 BLE                  | Arduino  | ABX00030                 | 2   | Pieces | $26.30    | $52.60 |

<br/><br/>
**References** 

[1] Team, T. A. (n.d.). _Arduino docs: Arduino Documentation._ Arduino Docs | Arduino Documentation. Retrieved February 13, 2023, from https://docs.arduino.cc/ 

[2]	_Arduino._ (n.d.). Retrieved February 21, 2023, from https://content.arduino.cc/assets/Nano_BLE_MCU-nRF52840_PS_v1.1.pdf 

[3]	_Energizer L91 specifications ultimate lithium._ (n.d.). Retrieved February 24, 2023, from https://data.energizer.com/pdfs/l91.pdf 

[4] _How to reduce power consumption on the nano 33 ble._ (n.d.). Retrieved February 21, 2023, from https://support.arduino.cc/hc/en-us/articles/4402394378770-How-to-reduce-power-consumption-on-the-Nano-33-BLE 

[5]	_Arduino® Nano 33 ble._ (n.d.). Retrieved February 21, 2023, from https://docs.arduino.cc/resources/datasheets/ABX00030-datasheet.pdf

[6]	ArduinoModules, Olawale, I., Ryerson, B., & Chavan, S. (2023, February 15). _KY-032 infrared obstacle avoidance sensor module._ ArduinoModulesInfo. Retrieved February 24, 2023, from https://arduinomodules.info/ky-032-infrared-obstacle-avoidance-sensor-module/ 

[7]	_Energizer L92 specifications ultimate lithium._ (n.d.). Retrieved February 24, 2023, from https://data.energizer.com/pdfs/l92.pdf 

[8]	_IR sensor for obstacle avoidance KY-032 (AD-032)._ IR Senor Obstacle Avoidance Keyes KY 032. (n.d.). Retrieved February 5, 2023, from http://irsensor.wizecode.com/

[9] _RF Wireless World._ Network Latency Calculator | Network Latency Formula. (n.d.). Retrieved February 13, 2023, from https://www.rfwireless-world.com/calculators/Network-Latency-Calculator.html 








