# Mario Kart Rev 2 - Signoff - Mario Kart Bike Wireless Sensors Subsystem 
## Team 4 - Blake Pickett and Sage Mooneyham ##
<br/><br/>
### _Function of the Subsystem:_ ###

The function of the newly designed feature is to enable Bluetooth LE (BLE) connectivity between sensors and central Raspberry Pi (RPi). These sensors will gather, convert, and send data via BLE (achieved with usage of Arduino Nano 33 BLEs for each sensor) to the master RPi. The wires that rectify and step down the power for the sensors on the current version of the Mario Kart Bike will be replaced with 4 AA batteries and a holder. The 4 AA batteries will provide 6 V and 3500 mAh to the microcontrollers, which will power the sensors for more than 2 weeks.    
<br/><br/>

### _Constraints:_ ###

* **Run Time:**
  * Batteries must supply the DC voltage and current needed to power the equipment for 2 weeks. The equipment shall be able to with stand a minimum of 4 hours of constant use each day during the 2 weeks.     

* **Speed Sensor:** 
  * The KY-032 Obstacle Avoidance Sensor (tachometer) must have a DC voltage between 3.3 V and 5 V, and a minimum of 20 mA to operate correctly. [1]
  * The MIC94053 P-Channel MOSFET must have an input voltage from 1.8 V to 5.5 V. [2] 
  * The MIC94053 P-Channel MOSFET must allow a drain current of 20 mA.  
  * The Nano 33 BLE must have a DC voltage between 5 V and 21 V. [3]
  * The current through the 3.3 pin on the Nano 33 BLE must be less than 100 mA. [4]     

* **Steering Sensor:** 
  * The Potentiometer voltage must be the same as the analog to digital converter (ADS1015).    
  * The ADS1015 must have a DC voltage between 0 V and 5.5 V. [5] 
  * The Nano 33 BLE must have a DC voltage between 5 V and 21 V. [3]
  * The current through the GPIO pins on the Nano 33 BLE must be less than 15 mA. [3]

* **Data Transfer Method:**
  * Communication between the sensors and main RPi must be wireless. Each sensor must have a corresponding Nano 33 BLE in order to achieve BLE communication.

* **Latency:**
  * Communication latency from data sensors to central microcontroller shall be at maximum 40 ms.

<br/><br/>
### _Buildable Schematic:_  ###   

The wiring schematics for the speed and steering sensors are provided in **Figures 1** and **2**.  

![image](https://user-images.githubusercontent.com/113309616/222093348-172a01bc-0b0a-4d13-abbd-737224e1fa5a.png)

**Figure 1.** Wiring Schematic for the Speed Sensor
<br/><br/>

![image](https://user-images.githubusercontent.com/113309616/222106145-a69c4e9f-3974-4ed4-a7cf-127cb6c76b75.png)

**Figure 2.** Wiring Schematic for the Steering Sensor

<br/><br/>
### _Analysis:_ ### 
<br/><br/>

* **Power Supply for the Speed Sensor:** 
<br/><br/>

  * **_Speed Sensor Batteries:_**
  
      * AA Battery Current = 3500 mAh [6]
      * AA Battery Voltage = 1.5 V [6]
      * Total AA Batteries Voltage = 1.5 * 4 = 6 V
      * Total AA Batteries Wattage = 6 * 3500 = 21000 mWh

  * **_Speed Sensor Current:_**
    
      * Tachometer (running) = 20 mA [1]
      * Tachometer (sleeping)  = 0 mA 
         * The MOSFET is in the cut-off region when Vgs > - Vth. The Vgs = 3.3 – 3.3 = 0  V. The Vth minimum value is - 0.5 V and the maximum value is -1.2 V [2]. Since Vgs = 0 V > Vth = -0.5 V, the drain current Id = 0 A. The tachometer sleeping current is equal to the drain current. 
      * MIC94053 P-Channel MOSFET Current = 0.005 mA [2] 
      * Arduino Nano 33 BLE Default Run Settings = 17 mA [7]  
      * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on RTC event) = 0.00316 mA [8]
    <br/><br/>
         * Max current going through 3.3 pin  =  20 mA
         * Current needed (running) = 20 + 17 + 0.005 = 37.005 mA
         * Current needed (Sleeping) = 0 + 0.00316 + 0.005 = 0.00816  mA
         * Total Amp-Hours Needed = (37.005 * 56) + (0.00816  * 280) = 2074.56 mAh    
        
    The speed sensor will use 2075 mAh in 2 weeks of use, which is less than the 3500 mAh that the battery can supply. 
    
    The max current going through the 3.3 pin is 20 mA which is less than 100 mA that the 3.3 pin can with stand. 
    
    The tachometer will be supplied 20 mA when running and 0 mA when sleeping. 
    
    The MIC94053 P-Channel MOSFET will allow a drain current of 20 mA through the MOSFET because the drain current is less than 1.4 amps [2]. The tolerance for the drain current is 1.4 amps [2].
<br/><br/>

  * **_Speed Sensor Voltage:_**
<br/><br/>
    ![image](https://user-images.githubusercontent.com/113309616/222095045-b4764fad-d99c-4626-ae0d-39a660decc9e.png)

    **Figure 3.** Discharge of the Ultimate Lithium Energizer AA Battery [6]

    From **Figure 3**, the voltage from of a battery discharging 10 mA or 100 mA drops from 1.5 V to 1.3 V. 

     * Total Voltage Before Discharging =  1.5 * 4 = 6 V 
     * Total Voltage After Discharging =  1.3 * 4 = 5.2 V 

    Therefore, the voltage will stay above the 5 V cutoff voltage of the Arduino Nano 33 BLE even when the batteries have dissipated the full 3500 mAh.

    The input voltage will be regulated by the voltage regulator on the Arduino Nano 33 BLE to 3.3 V. 
    
    The tachometer will be supplied 3.3 V when running and 0 V when sleeping. 
    
    The MIC94053 P-Channel MOSFET will receive 3.3 V for the input voltage which is between 1.8 V and 5.5 V. 
    <br/><br/>

  * **_Speed Sensor Power:_**

    * Tachometer (running) = 20 * 3.3 = 66 mW
    * Tachometer (sleeping) = 0 V * 0 A = 0 mW
    * MIC94053 P-Channel MOSFET Power Dissipation = (Id )^2 * Rds = (20*10^-3)^2 * 76 * 10 ^-3 = 0.0304 mW  
       * Id = tachometer (running) = 20 mA
       * Rds = 76 m ohms [2]
    * Arduino Nano 33 BLE Default Settings = 17 * 6 = 102 mW 
    * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on RTC event) = 0.00316* 6 = 0.01896 mW
    <br/><br/>
       - Watts needed (running) = 66 + 102 + 0.0304 = 168.0304 mW  
       - Watts needed (sleeping) =  0 + 0.01896 + 0.0304 = 0.4936 mW
       - Total Watt-Hours Needed = (168.0304  * 56) + (0.4936  * 280) = 9423.5232 mWh  

    The speed sensor will use 9424 mWh in 2 weeks of use. Four AA batteries will provide 21000 mWh, which is sufficient to run the speed sensor equipment for 2 weeks including the 4 hours of constant use each day.
    <br/><br/>

  * **_Speed Sensor Run Time:_**

    Power can be preserved by turning on and off the tachometer (GPIO Pin 22 will be connected to the gate of the MIC94053 P-Channel MOSFET), power LED, and I2C pull-up resistors when needed (done in software) [9][10]. 
    
    A low signal will be asserted to Pin 22 to turn on the tachometer. This will complete voltage connection from the Nano voltage pin (pin 2) to the Tachometer voltage pin( Vcc) allowing current to flow through the tachometer.
    
    A high signal will be asserted to Pin 22 to turn off the tachometer. This will break the voltage connection from the Nano voltage pin (pin 2) to the Tachometer voltage pin( Vcc), creating an open circuit, allowing no current to flow through the tachometer.
    
    This Nano is awoken by event using the RTC timer on the nRF52840 processor. Every 10 seconds (this number is chosen so as to connect in a timely fashion if user wants to activate the controller, while still keeping Nano in sleep a majority of the time), the Nano used for speed data communication will check to see if the central RPi is looking for connection (this means user is attempting to use device). If so, Tachometer is turned back on and actions made before sleeping are reverted. If central RPi is not broadcasting for connection, the Nano will reenter sleep mode (RTC counter).
    
    Dimensions of the battery holders are 2.248 inches (L) by 2.457 inches (w) by 0.622 inches (h). The holders are small/compact to avoid the trip hazard posed by the long wires. Zip ties will securely mount the battery holder to the bike frame. 
    <br/><br/>
    <br/><br/>
    
* **Power Supply for the Steering Sensor:**
    <br/><br/>
    * **_Steering Sensor Batteries:_**

      * AA Battery Current = 3500 mAh [6]
      * AA Battery Voltage = 1.5 V [6]
      * Total AA Batteries Voltage = 1.5 * 4 = 6 V
      * Total AA Batteries Wattage = 6 * 3500 = 21000 mWh

    * **_Steering Sensor Current:_**
    
      * Potentiometer  (running) = 10k ohms [11] = 3.3/10000 = 0.33 mA
      * Potentiometer (sleeping) = 0 / 10000 = 0 mA
      * ADS1015 = 0.3 / 3.3 = 0.09091 mA 
      * Arduino Nano 33 BLE Default Settings = 17 mA [7]    
      * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on GPIOTE event) = 0.01737 mA [8]
        <br/><br/>
         - Max current going through IO pins = 0.33 mA
         - Current needed (running) = 0.33 + 0.09091 + 17 = 17.421 mA
         - Current needed (sleeping) = 0 + 0.09091+ 0.01737 = 0.10828 mA
         - Total Amp-Hours Needed = (17.421 * 56) + (0.10828 * 280) = 1981.47 mAh 

      The steering sensor will use 1982 mAh in 2 weeks of use, which is less than the 3500 mAh that the battery can supply.  
      
      The max current going through the GPIO pins is 0.33 mA which is less than 15 mA that the GPIO pins can with stand. 
      <br/><br/>

    * **_Steering Sensor Voltage:_**
    
      From **Figure 3**, the voltage from of a battery discharging 10 mA or 100 mA drops from 1.5 V to 1.3 V.  

         * Total Voltage Before Discharging =  1.5 * 4 = 6 V 
         * Total Voltage After Discharging =  1.3 * 4 = 5.2 V 

      Therefore, the voltage will stay above the 5 V cutoff voltage of the Arduino Nano 33 BLE even when the batteries have dissipated the full 3500 mAh. 

      The input voltage will be regulated by the voltage regulator on the Arduino Nano 33 BLE to 3.3 V.
      
      The GPIO pins will output 3.3 V when given a high signal and 0 V when given a low signal.
      
      The potentiometer and the ADS1015 will be supplied with 3.3 V when their IO pins are given a high signal. Therefore, the voltage on the potentiometer and the ADS1015 will be the same. 
      <br/><br/>

    * **_Steering Sensor Power:_**

        * Potentiometer (running)= 0.33 * 3.3 = 1.089 mW
        * Potentiometer (sleeping) = 0 A * 0 V = 0 mW
        * ADS1015 = 0.3 mW [5]
        * Arduino Nano 33 BLE Default Settings = 17 * 6 = 102 mW 
        * Arduino Nano 33 BLE Sleep Mode (Ram Retention, wake on GPIOTE event) = 0.01737 * 5 = 0.10422 mW
        <br/><br/>
            - Watts needed (running) =  1.089 + 0.3 + 102 = 103.389 mW
            - Watts needed (sleeping) = 0 + 0.3 + 0.10422 = 0.40422 mW
            - Total Watt-Hours Needed = (103.389 * 56) + (0.40422 * 280) = 5902.97 mWh

        The speed sensor will use 5903 mWh in 2 weeks of use. Four AA batteries will provide 21000 mWh, which is sufficient to run the speed sensor equipment for 2 weeks including the 4 hours of constant use each day.
        <br/><br/>

    * **Steering Sensor Run Time:**

      Power can be preserved by turning on and off the potentiometer (Nano GPIO Pin 20), power LED, and I2C pull-up resistors when needed (done in software)[9][10]. 
      
      A high signal will be asserted to pin 20 to turn on the potentiometer. 
      
      A low signal will be asserted to pin 20 to turn on the potentiometer. 
      
      The Arduino Nano 33 BLE will go into sleep mode after the potentiometer, power LED, and I2C pull-up resistors are turned off. Before sleeping, Nano will use the endTransmission Arduino function to end I2C communication. 
      
      The Nano can be woken via a GPIO interrupt event. The GPIO interrupt event that will awaken the switch will be on pin 25 as well as 26 (left and right handlebar button). When the user presses either/both of these, the Nano will wake from sleep, and connect to the central RPi, as well as revert previous actions before it slept.

      Dimensions of the battery holders are 2.248 inches (L) by 2.457 inches (w) by 0.622 inches (h). The holders are small/compact to avoid the trip hazard posed by the long wires. Zip ties will securely mount the battery holder to the bike frame.
      <br/><br/>

 * **Strobing of Receiver:** 

    IR light is emitted from the KY-032 at a frequency of 38 kHz [12], so the receiver (HS0038B) must be cycling at 76 kHz (as a minimum) to satisfy the Nyquist sampling rate. This strobe rate can be programmed manually.  The KY-032 sensor will use the enable pin, which should not be active for more than 2 ms at a time due to the receiver quickly saturating when active [12].

    By determining the time between any two high readings (two markings) and multiplying this time by the number of individual markings, the time required to perform each revolution of the flywheel can be calculated (this calculation will update between every 2 high readings).    

      - (Time between two highs) * (Number of markings) = Time for 1 revolution

    By using the gearing ratio between the flywheel and the bike tire, the current revolutions per second (or minute) at the bike tire can be calculated.    
    <br/><br/>

 * **Bluetooth Connectivity:**

    BLE connectivity for the steering sensor’s microcontroller can use the sensor in conjunction with the ADS 1015 and Potentiometer as well as the left and right handlebar buttons on the bike.    

    Arduino microcontrollers surpass the 5 V limit while others are at 5 V exactly. The Arduino Nano 33 BLE satisfies the power constraint. The Nano 33 BLE measures 45 mm by 18 mm and will within the space constraints of the Mario Kart Bike’s long metal pipes.     
    <br/><br/>

 * **Latency:**

    Latency of communication shall be 40 ms. Network latency can be calculated with the following formula [13]:

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
| Energizer                  | 24 Pack AA Lithium Batteries | Amazon   | B07BMH7RDP               | 1   | Pack   | $65.35    | $65.35 |
| Microchip Technology       | MIC94053YC6-TR               | Digi-key | MIC94053YC6-TR           | 1   | Piece  | $0.74     | $0.74  |
| HMROPE                     | 8 Inch Zip Ties              | Amazon   | TXLAC                    | 1   | Pack   | $9.18     | $9.18  |
| Duck                       | Electrical Tape              | Amazon   | 282289                   | 1   | Roll   | $1.48     | $1.48  |
| Arduino                    | Nano 33 BLE                  | Arduino  | ABX00030                 | 2   | Pieces | $26.30    | $52.60 |

<br/><br/>
**References** 

[1]	ArduinoModules, Olawale, I., Ryerson, B., & Chavan, S. (2023, February 15). KY-032 infrared obstacle avoidance sensor module. ArduinoModulesInfo. Retrieved February 24, 2023, from https://arduinomodules.info/ky-032-infrared-obstacle-avoidance-sensor-module/ 

[2] 84mΩ p-channel MOSFET in SC-70-6 - Microchip Technology. (n.d.). Retrieved March 1, 2023, from https://ww1.microchip.com/downloads/en/DeviceDoc/mic94052-53.pdf 

[3] Store.arduino.cc/Nano-33-BLE. (n.d.). Retrieved March 1, 2023, from https://docs.arduino.cc/static/0877c2bf863b3473e961b0b72c8e68ec/ABX00030-full-pinout.pdf 

[4] How to power your arduino? Vin, 5V, and 3.3V pins. How to Power Your Arduino? Vin, 5V, and 3.3V Pins. - Circuit Journal. (n.d.). Retrieved March 1, 2023, from https://circuitjournal.com/arduino-power-pins#:~:text=3.3V%20Pin%20as%20a%20Power%20Output.%20You%20can,can%20supply%20about%20100%20to%20150mA%20of%20current. 

[5] ADS1015. ADS1015 data sheet, product information and support | TI.com. (n.d.). Retrieved March 1, 2023, from https://www.ti.com/product/ADS1015 

[6]	Energizer L91 specifications ultimate lithium. (n.d.). Retrieved February 24, 2023, from https://data.energizer.com/pdfs/l91.pdf 

[7] Team, T. A. (n.d.). Arduino docs: Arduino Documentation. Arduino Docs | Arduino Documentation. Retrieved February 13, 2023, from https://docs.arduino.cc/ 

[8] Arduino. (n.d.). Retrieved February 21, 2023, from https://content.arduino.cc/assets/Nano_BLE_MCU-nRF52840_PS_v1.1.pdf

[9]	How to reduce power consumption on the nano 33 ble. (n.d.). Retrieved February 21, 2023, from https://support.arduino.cc/hc/en-us/articles/4402394378770-How-to-reduce-power-consumption-on-the-Nano-33-BLE 

[10]	Arduino® Nano 33 ble. (n.d.). Retrieved February 21, 2023, from https://docs.arduino.cc/resources/datasheets/ABX00030-datasheet.pdf

[11] Industries, A. (n.d.). Stemma wired potentiometer breakout board - 10K ohm linear. adafruit industries blog RSS. Retrieved March 1, 2023, from https://www.adafruit.com/product/4493#description 

[12]	IR sensor for obstacle avoidance KY-032 (AD-032). IR Senor Obstacle Avoidance Keyes KY 032. (n.d.). Retrieved February 5, 2023, from http://irsensor.wizecode.com/

[13] RF Wireless World. Network Latency Calculator | Network Latency Formula. (n.d.). Retrieved February 13, 2023, from https://www.rfwireless-world.com/calculators/Network-Latency-Calculator.html 



