# Mario Kart Rev 2 - Signoff - Mario Kart Bike RRSA
## Team 4 - Tyler Chittum ##

### Function

The function of the ride data acquisition system is to collect the data necessary to replay rides taken by a rider. The system is required to collect the following: speed, altitude, and video footage. The system records this data and transfers it to the ride replay system by Bluetooth when in proximity.

### Constraints

**C1. Sensor Constraints:** 

The combined inaccuracy of the pressure sensor, the speed sensor, and the resistance system is to be below 10 %.

**C1.1. Pressure Sensor:** The required precision to achieve +/- 1 % accuracy at a granularity of 1 kCal is +/- 4.67 cm. The ride data is to be digitally filtered to attenuate out any ride noise above 1 Hz, so altitude data must be sampled at at least 2 Hz [Nyquist theorem].

**C1.2 Speed Sensor:** The bike wheel speed must be sampled at a frequency of at least 9.6 Hz as the maximum specified bike wheel rotational frequency is 288 RPM, or 4.8 Hz [Nyquist theorem].

**C2. Video Recording:** 

**C2.1. Video Quality:** The resolution is to be 720p with a frame rate of at least 30 fps, and the camera is to be compatible with the Raspberry Pi Zero 2W's camera serial interface. 

**C2.2. Video Data Syncing:** The video footage recorded is to be in sync with the data being measured by sensors.

**C3. Battery life:** The device must be able to continuously operate for at least 3 hours and must provide the user with a visual indication of battery charge status.

**C4. Recording capacity:** The device must be able to capture 3 hours of continuous footage and measurements. 

**C5. Usability:** The device must provide an easily used interface, which is also unobtrusive and does not distract the rider.

**C6. Durability:** The device is to be protected from the outside environment with all electrical components secured to prevent damage while the user is riding.

**C.7 Device Fitment:** The device is to be capable of mounting on any standard mountain bike with no obstructions to the video recording.


### Schematic:

![RRSA Schematic](https://user-images.githubusercontent.com/118228609/203230366-a49b449b-943c-4f00-ad5b-cdeb976bec66.png)
Figure 1: a schematic for the assembly. Not pictured: the camera, which is to be attached to the camera port on the Raspberry Pi Zero 2W.

![Overhead View](https://user-images.githubusercontent.com/118228609/220002131-ab6d1f27-5fda-4ba9-a132-e8f04153594e.png)
Figure 2: a drawing illustrating the placement of modules within the project box. The mounting plate is covered in 2.54 mm width square holes. The battery is to be affixed using zip ties. The camera is to be affixed using glue.

![Front Panel](https://user-images.githubusercontent.com/118228609/220002416-1288c96b-3247-4ce5-85d7-2f7800a0e43c.png)
Figure 3: the front panel. The mounted components (from left to right): USB-C socket, power switch, start/stop switch.

![Camera Hole](https://user-images.githubusercontent.com/118228609/220002534-c0886375-129e-439e-89e0-702ba8e7b94f.png)
Figure 4: the camera hole, which is located on the panel facing away from the rider during use.

![Full RRSA](https://user-images.githubusercontent.com/118228609/220002635-eecbd6a5-5cfe-484a-801a-4ce01f01fc76.png)
Figure 5: the full assembly with annotations.

![Speed Sensor](https://user-images.githubusercontent.com/118228609/220002797-e5f8a9a3-fd77-405e-ae3a-d4b655e1e5df.png)
Figure 6: detail on the speed-sensing portion of the assembly. The reed switch will be secured using two zip ties.

### Analysis:

**A1.1. Pressure Sensor:** 

    Imprecision = 2 cm < 4.67 cm
    Operating range: 300 hPa to 1200 hPa
    Measurement time [high precision] = 105 ms [4]
    Maximum sample rate = 1 ÷ 105 ms = 9.524 Hz > 2 Hz

**A1.2. Speed Sensor:**

    Raspberry Pi GPIO sampling speed = 10 MHz [6] > 9.6 Hz

**A2.1. Video Data Syncing:**

    Raspberry pi time clock rate = 1 MHz
    Time precision = 1 μs
    Max frame desync = 1 μs ÷ (1 ÷ 60 Hz) × 100 % = 0.006 %

**A2.2. Video Quality and Format:**

    Camera recording quality: 720p, 60 fps (or below) [as specified]
    Connection protocol: Rasberry Pi CSI (camera serial interface)
    Formatting capability: MPEG-4 h.264 via ffmpeg

**A4. Recording Capacity:**

    Storage capacity: 128 Gb
    Typical bitrate for as-specified video: 6.5 MB/s [7]
    Video-specific storage = 6.5 MB/s × 60 s/min × 60 min/h × 3 h = 70.2 GB
    Remaining storage = 128 Gb - 70.2 Gb = 57.8 Gb

The remaining storage is the be put to use for sensor data and the operating system.
The SD card used for storage is V10 compliant; rated to record full HD video.

**A3: Battery Life:**

    Raspberry Pi Zero 2W current requirement [stressed] = 580 mA [1]
    Raspberry Pi Camera current requirement [max] = 250 mA [2]
    Raspberry Pi GPIO internal pullup resistor = 33-73 kΩ [3]
    Raspberry Pi logic level = 3.3 V
    Reed switch current draw = 3.3 V / 33 kΩ = 0.1 mA
    DPS310 altitude sensor current draw [max] = 0.345 mA [4]
    Indicator light current draw = 20 mA each [5] = 20 mA × 2 = 40 mA
    Power supply nominal efficiency = 90 %
    Battery energy storage capacity = 24.42 Wh
    Effective battery energy = 24.42 Wh × 90 % = 21.98 Wh
    RRSA power requirement [max] = 5 V × (580 mA + 250 mA + 0.1 mA + 0.345 mA + 40 mA) = 4.352 W
    Projected battery life = 21.98 Wh ÷ 4.352 W = 5.050 hours > 3 hours

Also:

    Recommended constant battery discharge rate = 0.25 C = 1.32 A
    Projected current draw [max] = (4.352 W ÷ 90 %) ÷ 3.7 V = 1.31 A < 1.32 A
    Battery charge rate specification = 1.5 A
    Charge rate limit = 1 A < 1.5 A

**A5. Useability:**

Two button interface; one to turn off and on, the other to start or stop the video recording. The power button has an LED that signifies power on, and the other LED lights when video is being recorded and blinks during data transfer.

**A6. Durability:**

Waterproof box provides protection from weather conditions. Aside from the fasteners shown in figures 2,4,6 [nuts and bolts], glue will be used to seal the entry hole for the speed sensor wires as well as the hole for the camera; zip ties will be used to attach the speed sensing reed switch and the battery.

A7. Device Fitment: The housing attaches to the handlebars using a mechanical twist-locking mechanism and a screw-tensioned ring with rubber adaptors. The bracket requires no tools for removal or installation of the box, and the rubber adapters allow for universal fitment.
  

**Table 1:** Bill of Materials.
| Subsystem Name: | Ride Data Acquisition System |                                                                         |                      |                 |     |        |           |         |
| --------------- | ---------------------------- | ----------------------------------------------------------------------- | -------------------- | --------------- | --- | ------ | --------- | ------- |
| Requested by:   | Tyler C.                     |                                                                         |                      |                 |     |        |           |         |
| Approve by:     |                              |                                                                         |                      |                 |     |        |           |         |
| Total Cost:     | $159.85                      |                                                                         |                      |                 |     |        |           |         |
|                 |                              |                                                                         |                      |                 |     |        |           |         |
|                 |                              |                                                                         |                      |                 |     |        |           |         |
| Level           | Part #                       | Part Name                                                               | Supplier             | Supplier Part # | Qty | Units  | Unit Cost | Cost    |
| 1               | COMP1                        | Raspberry Pi Zero 2W                                                    | Digikey              | 2648-SC0510-ND  | 1   | Module | $15.00    | $15.00  |
| 1.1             | MEM1                         | 128 GB Micro SD Card                                                    | Newegg               | N82E16820215186 | 1   | Module | $10.49    | $10.49  |
| 2               | PSU1                         | Power Supply                                                            | NONE                 | NONE            | 1   | Assy   |           | $0.00   |
| 2.1             | MD1                          | Adafruit Powerboost 1000                                                | Adafruit             | 2465            | 1   | Module | $19.95    | $19.95  |
| 2.2             | CABLE1                       | AK67421-0.3-VM                                                          | Digikey              | AE11229-ND      | 1   | Piece  | $2.58     | $2.58   |
| 2.3             | JACK1                        | USB C Jack to USB A Jack Round Panel Mount Adapter                      | Adafruit             | 4259            | 1   | Piece  | $5.95     | $5.95   |  
| 2.4             | CABLE2                       | USB cable - 6" A/MicroB                                                 | Adafruit             | 898             | 1   | Piece  | $2.95     | $2.95   |
| 2.5             | SW1                          | Rugged Metal On/Off Switch with Green LED Ring - 16mm Green On/Off      | Adafruit             | 482             | 1   | Piece  | $4.95     | $4.95   |
| 2.6             | SW3                          | Rugged Metal Pushbutton with Red LED Ring - 16mm Red Momentary          | Adafruit             | 559             | 1   | Piece  | $4.95     | $4.95   |
| 2.7             | BT1                          | Lithium Ion Battery Pack - 3.7V 6600mAh                                 | Adafruit             | 353             | 1   | Piece  | $24.50    | $24.50  |
| 3               | SENSE1                       | Speed Sensor                                                            | NONE                 | NONE            | 1   | Assy   |           | $0.00   |
| 3.1             | SW2                          | Hamlin SPST - N.O. High Quality Reed Switch                             | Electronics Goldmine | G26522          | 1   | Piece  | $2.49     | $2.49   |
| 3.3             | ZT1                          | Amazon Basics Multi-Purpose Cable Ties - 4-Inch/100mm, 200-Piece, White | Amazon               | DS-SZS-002      | 1   | Piece  | $4.62     | $4.62   |
| 3.4             | MAG1                         | Bike Wheel Spoke Computer Magnet                                        | AliExpress           | NONE            | 1   | Piece  | $1.68     | $1.68   |
| 4               | SENSE2                       | Adafruit DPS310 Precision Barometric Pressure / Altitude Sensor         | Adafruit             | 4494            | 1   | Module | $6.95     | $6.95   |
| 5               | MECH1                        | Mechanical Parts                                                        | NONE                 | NONE            | 1   | Assy   |           | $0.00   |
| 5.1             | BOX1                         | QILIPSU Clear Hinged Cover 220x170x110mm Junction Box                   | Amazon               | B087F9TS25      | 1   | Piece  | $29.99    | $29.99  |
| 5.2             | MNT1                         | Bike Phone Mount, Bicycle Cell Phone Holder with Universal Adapter      | Amazon               | B08R5K29BC      | 1   | Kit    | $19.98    | $19.98  |
| 5.3             | FASTENER1                    | M2.5-0.45 x 10 mm Zinc Plated Steel Machine Screws (25-Pack)            | Home Depot           | 311229794       | 1   | 25-Pk  | $6.04     | $6.04   |
| 5.4             | FASTENER2                    | M2.5-0.45 Zinc-Plated Metric Hex Nut (5-Piece per Bag)                  | Home Depot           | 204836094       | 3   | 5-Pk   | $1.25     | $3.75   |
| 5.5             | FASTENER3                    | Gorilla Max Strength Clear Construction Adhesive                        | Amazon               | B0916KZ598      | 1   | Piece  | $7.96     | $7.96   |
| 6               | CAM1                         | Camera Module for Raspberry Pi Zero                                     | Pimoroni             | CAM003          | 1   | Assy   | $10.56    | $10.56  |
|                 |                              |                                                                         |                      |                 |     |        | Total     | $159.85 |

### References

[1] L. Pounder, “Raspberry Pi Zero 2 W review: The long awaited sequel,” tomshardware.com, 28-Oct-2021. [Online]. Available: https://www.tomshardware.com/reviews/raspberry-pi-zero-2-w-review. [Accessed: 20-Nov-2022].

[2] jamesh, “Re: Raspberry Pi - camera, reducing power consumption,” Raspberry Pi Forums - Index page, 30-Jul-2011. [Online]. Available: https://forums.raspberrypi.com/viewtopic.php?t=152864. [Accessed: 13-Jan-2023].

[3] A. Scheller, K. Rijnieks, and A. Allan, “Alternative Functions,” Raspberry Pi Documentation. [Online]. Available: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#alternative-functions. [Accessed: 13-Jan-2023].

[4] “DPS310,” infineon.com, 15-Oct-2020. [Online]. Available: https://www.infineon.com/dgdl/Infineon-DPS310-DataSheet-v01_02-EN.pdf?fileId=5546d462576f34750157750826c42242. [Accessed: 14-Oct-2023].

[5] “Rugged metal on/off switch with Red Led Ring: Technical Details,” adafruit.com. [Online]. Available: https://www.adafruit.com/product/916#technical-details. [Accessed: 13-Jan-2023].

[6] M4H, "Maximum theoretical GPIO sample speed," Raspberry Pi Forums. [Online]. Available: https://forums.raspberrypi.com/viewtopic.php?t=128387. [Accessed: 5-Feb-2023]

[7] “A beginner’s guide to bit rate,” adobe.com. [Online]. Available: https://www.adobe.com/creativecloud/video/discover/bit-rate.html. [Accessed: 22-Nov-2022].


