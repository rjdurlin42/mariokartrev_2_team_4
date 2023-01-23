# Mario Kart Rev 2 - Signoff - Mario Kart Bike RRSA
## Team 4 - Tyler Chittum ##

### Function

The function of the ride data acquisition system is to collect the data necessary to replay rides taken by a rider. The system is required to collect the following: speed, altitude, and video footage. The system records this data and transfers it to the ride replay system by Bluetooth when in proximity.

### Constraints

**Measurement accuracy:** it is imperative that the device record the altitude of the rider with a high degree of precision. If the simulated resistance is to be within 10 % of the real-world resistance as previously constrained, the combined inaccuracy of the pressure sensor, the speed sensor, and the resistance system must be below 10 %. Let the error allowance for the determination of the energy expended during exercise be 1 %. For a bike and rider of 91 kg, an altitude gain of 4.67 m results in an energy expenditure of 1 kCal since E = mgh. Accordingly, the required precision to achieve +/- 1 % accuracy at a granularity of 1 kCal is +/- 4.67 cm. The speed must also be sampled at a rate which allows reasonably fast response time. Since the use of single-magnet speed sensing is already proven as common practice for bike computers, and all potential energy calculations can be performed with only the measured altitude over time, the main constraint for speed sensing is one of durability. The reed switch used must nominally tolerate at least 1000 miles of operation.

**Video recording:** the resolution is to be 720p, and the frame rate is to be at least 30 fps. 

**Battery life:** the device must be able to continuously operate for at least 3 hours, and must provide the user with a visual indication of battery charge status. 

**Recording capacity:** the device must be able to capture 3 hours of continuous footage and measurements. Additionally, the storage media must possess the bandwidth to record the video as it is being taken. 

**Usability:** the device must provide an easily used interface, which is also unobtrusive and does not distract the rider. 

**Durability:** the device must be shielded from outside weather conditions, and all component boards must be attached firmly enough to prevent them from being knocked around during riding.

**Mountability:** The device must be readily mountable on any standard mountain bike. Additionally, the angle of the device when mounted must produce a satisfactory filming angle for aquisition of optical data. Also, it must be possible to quickly remove/remount the device from/to the bike without any tools, so that the device can be moved to a different location to be charged or to transfer data without imposing any hassle on the user.

### Schematic:

![RRSA Schematic](https://user-images.githubusercontent.com/118228609/203230366-a49b449b-943c-4f00-ad5b-cdeb976bec66.png)
Figure 1: a schematic for the assembly. Not pictured: the camera, which is to be attached to the camera port on the Raspberry Pi Zero 2W.

![PIC03042](https://user-images.githubusercontent.com/118228609/203231527-3cd93c0c-69ab-4919-86b1-4a5de69bc6ae.JPG)
Figure 2: a drawing illustrating the placement of modules within the project box.

![PIC03041](https://user-images.githubusercontent.com/118228609/203231351-a6e881cc-bc34-441a-97ff-cbec0ddabef7.JPG)
Figure 3: a drawing illustrating the front and back panels. The first item (from left to right) on the front panel is a panel-mount USB-C socket. The second is the power switch, followed by the start/stop switch. The hole in the back panel is for the camera.

### Analysis:

The Raspberry Pi Zero 2W was found to draw 580 mA (2.9 W) when stressed [1]. The Raspberry Pi Camera draws a maximum of 250 mA according to a forum post by the Principle Software Engineer of the Raspberry Pi Foundation [2]. The internal resistance of the Raspberry Pi's internal GPIO pullup resistor ranges from 33-73 kOhms [3], and with a 3.3 V logic level, the maximum possible current draw owing to the closing of the reed switch is 0.1 mA (calculated by dividing 3.3 V by the lowest specified resistance). The DPS310 altitude sensor requires a maximum current of 0.345 mA [4]. The LEDs in the switches are specified to have a current draw of approximately 20 mA each [5]. The power supply unit is specified to have a nominal efficiency of 90 %. The battery used has an energy storage capacity of 24.42 Wh. Accordingly, the effective energy available to the unit is 21.98 Wh. The required power input to the device may be calculated by multiplying the sum of the above currents with 5 V, since the voltage regulation on the Raspberry Pi board is performed using a linear regulator (meaning the current is constant). This yields a maximum power draw of 4.352 W, corresponding to a battery life of 5.050 hours, which meets the prior specification. The specified battery contains built in circuitry which ensures that it can never be over-discharged nor over-charged. Additionally, the power supply module provides a visual indication of the charge status, lighting up green when the battery is fully charged, and a red warning light when the charge is low. It was for this reason that a clear-topped box was selected. No detailed cycling data was given, making it impossible to make a cycling life estimation; however, the discharge rate is reccomneded to be kept at or below 0.25 C, corresponding to a current of 1.32 A. This device is expected to draw ((4.352 W)/0.9)/(3.7 V) A = 1.31 A nominally, which satisfies the battery's specification. Additionally, the battery is rated for a peak current of 3.3 A. The charge current is limited to 1 A by the selected power supply module, which satisfies the battery's charge current specification of 1.5 A or less. 

The utilized pressure sensor is specified to provide a measurement precision of +/- 2 cm, so it satisfies the prior specification. In addition, it provides on-board measurement averaging and low-pass filtering to reduce noise from the measurement. 

Hammlin specifies that their reed switches can last over 200 million actuations under ideal conditions [6]. The rated current for these reed switches is 0.5 A, which is well above what would be required to provide a signal voltage to the computer. Assuming a 200-million-actuation life and a 26" bike tire, the device would last for 257,732 miles, satisfying the aforementioned specification. 

The selected camera is capable of recording video in HD, 60 fps (or below) and thus satisfies the previously mentioned specification. 

To meet the storage requirements, a suitable SD card will be selected. A 128 GB SD card is a choice intended to be a reasonable starting point, as a typical 720p video has a bitrate of around 6.5 MB/s [7]. Accordingly, such an SD card would be able to store 3 hours of video as specified with 57.8 GB left over for the OS, programs, and sensor data. This SD card is compliant with the V10 standard, meaning that it is has sufficient bandwidth to record full HD video. 

The interface is a simple, unobtrusive, two button one with a light integrated into each button. One button turns the unit on or off, and the light for this button lights up when the unit is powered. The other button acts to activate or stop the recording. When this button is pressed, recording begins, and the light lights up. When the button is pressed again, recording stops, and the light turns off when the Raspberry Pi enters low power mode. This light also flashes when data transfer is in progress.

By gluing the boards down inside the case, they can be solidly anchored to the inside of the box. In addition, all holes, except what is necessary to allow airflow to the pressure sensor may be coated with glue to waterproof them.

To meet the mountability constraint, the housing for this device is to be secured to the bike using an already-existing universal bike mounting bracket designed for mounting cell phones and similar objects using a combination of adhesive coupling to the device housing, a mechanical twist-locking mechanism, and a screw-tensioned ring with rubber adaptors to allow use on a multitude of handlebar sizes. The angle of the device is adjustable by the user, ensuring the ability to attain an ideal camera angle. The twist-lock mechanism provided by this bracket provides a means to remove the device very rapidly, and without the use of any tools.
  

**Table 1:** Bill of Materials.
| Subsystem Name: | Ride Data Acquisition System |                                                                         |                      |                 |     |        |           |         |
| --------------- | ---------------------------- | ----------------------------------------------------------------------- | -------------------- | --------------- | --- | ------ | --------- | ------- |
| Requested by:   | Tyler C.                     |                                                                         |                      |                 |     |        |           |         |
| Approve by:     |                              |                                                                         |                      |                 |     |        |           |         |
| Total Cost:     | $160.18                      |                                                                         |                      |                 |     |        |           |         |
|                 |                              |                                                                         |                      |                 |     |        |           |         |
|                 |                              |                                                                         |                      |                 |     |        |           |         |
| Level           | Part #                       | Part Name                                                               | Supplier             | Supplier Part # | Qty | Units  | Unit Cost | Cost    |
| 1               | COMP1                        | Raspberry Pi Zero 2W                                                    | Digikey              | 2648-SC0510-ND  | 1   | Module | $15.00    | $15.00  |
| 1.1             | MEM1                         | 128 GB Micro SD Card                                                    | Newegg               | N82E16820215186 | 1   | Module | $10.49    | $10.49  |
| 2               | PSU1                         | Power Supply                                                            | NONE                 | NONE            | 1   | Assy   |           | $0.00   |
| 2.1             | MD1                          | Adafruit Powerboost 1000                                                | Adafruit             | 2465            | 1   | Module | $19.95    | $19.95  |
| 2.2             | CABLE1                       | AK67421-0.3-VM                                                          | Digikey              | AE11229-ND      | 1   | Piece  | $2.58     | $2.58   |
| 2.3             | CABLE2                       | Panel Mount Cable USB C to Micro B Male                                 | Adafruit             | 4056            | 1   | Piece  | $4.95     | $4.95   |  
| 2.4             | SW1                          | Rugged Metal On/Off Switch with Red LED Ring - 16mm Red On/Off          | Adafruit             | 916             | 1   | Piece  | $4.95     | $4.95   |
| 2.5             | BT1                          | Lithium Ion Battery Pack - 3.7V 6600mAh                                 | Adafruit             | 353             | 1   | Piece  | $24.50    | $24.50  |
| 3               | SENSE1                       | Speed Sensor                                                            | NONE                 | NONE            | 1   | Assy   |           | $0.00   |
| 3.1             | SW2                          | Hamlin SPST - N.O. High Quality Reed Switch                             | Electronics Goldmine | G26522          | 1   | Piece  | $2.49     | $2.49   |
| 3.2             | SW3                          | Rugged Metal Pushbutton with Red LED Ring - 16mm Red Momentary          | Adafruit             | 559             | 1   | Piece  | $4.95     | $4.95   |
| 3.3             | ZT1                          | Amazon Basics Multi-Purpose Cable Ties - 4-Inch/100mm, 200-Piece, White | Amazon               | DS-SZS-002      | 1   | Piece  | $4.62     | $4.62   |
| 3.4             | MAG1                         | Bike Wheel Spoke Computer Magnet                                        | AliExpress           | NONE            | 1   | Piece  | $1.68     | $1.68   |
| 4               | SENSE2                       | Adafruit DPS310 Precision Barometric Pressure / Altitude Sensor         | Adafruit             | 4494            | 1   | Module | $6.95     | $6.95   |
| 5               | MECH1                        | Mechanical Parts                                                        | NONE                 | NONE            | 1   | Assy   |           | $0.00   |
| 5.1             | BOX1                         | Large Plastic Project Enclosure - Weatherproof with Clear Top           | Adafruit             | 905             | 1   | Piece  | $19.95    | $19.95  |
| 5.2             | MNT1                         | Bike Phone Mount,Bicycle CellPhone Holder with Universal Adapter        | Amazon               | NONE            | 1   | Kit    | $19.98    | $19.98  |
| 5.3             | GLU1                         | Gorilla Glue Clear Grip                                                 | Lowes                | 1968296         | 1   | Stick  | $6.58     | $6.58   |
| 6               | CAM1                         | Camera Module for Raspberry Pi Zero                                     | Pimoroni             | CAM003          | 1   | Assy   | $10.56    | $10.56  |
|                 |                              |                                                                         |                      |                 |     |        | Total     | $160.18 |

### References

[1] L. Pounder, “Raspberry Pi Zero 2 W review: The long awaited sequel,” tomshardware.com, 28-Oct-2021. [Online]. Available: https://www.tomshardware.com/reviews/raspberry-pi-zero-2-w-review. [Accessed: 20-Nov-2022].

[2] jamesh, “Re: Raspberry Pi - camera, reducing power consumption,” Raspberry Pi Forums - Index page, 30-Jul-2011. [Online]. Available: https://forums.raspberrypi.com/viewtopic.php?t=152864. [Accessed: 13-Jan-2023].

[3] A. Scheller, K. Rijnieks, and A. Allan, “Alternative Functions,” Raspberry Pi Documentation. [Online]. Available: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#alternative-functions. [Accessed: 13-Jan-2023].

[4] “DPS310,” infineon.com, 15-Oct-2020. [Online]. Available: https://www.infineon.com/dgdl/Infineon-DPS310-DataSheet-v01_02-EN.pdf?fileId=5546d462576f34750157750826c42242. [Accessed: 14-Oct-2023].

[5] “Rugged metal on/off switch with Red Led Ring: Technical Details,” adafruit.com. [Online]. Available: https://www.adafruit.com/product/916#technical-details. [Accessed: 13-Jan-2023].

[6] “Hamlin Reed Switch Catalog,” DigiKey. [Online]. Available: https://www.digikey.com/en/pdf/h/hamlin/hamlin-reed-switch-catalog. [Accessed: 30-Nov-2022].

[7] “A beginner’s guide to bit rate,” adobe.com. [Online]. Available: https://www.adobe.com/creativecloud/video/discover/bit-rate.html. [Accessed: 22-Nov-2022].
