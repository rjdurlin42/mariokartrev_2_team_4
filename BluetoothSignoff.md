## Bluetooth Subsystem 
# Function of the Subsystem
The function of this subsystem is the wireless communication between the main RPi microcontroller and two external bike sensors: the speed sensor and the steering sensor. These sensors will gather data, converting it in the bike sensors case, and send this via Bluetooth to the master microcontroller, the RPi. These two sensors will be given their own microcontrollers, the Arduino Nano 33 BLE for the steering sensor and the Arduino Nano 33 BLE Sense for the speed sensor, in order to utilize Bluetooth 5 communication to the central RPi. Coding of the individual microcontrollers and their Bluetooth modules will be accomplished through the use of Arduino IDE text editor.

# Constraints
-	Power: Due to power constraints, the sensor’s microcontrollers shall be limited to an operating voltage of 5V. The microcontroller chosen (the Arduino Nano 33 BLE) is a very power efficient model, using only 3.3V of operating voltage.
-	Data Transfer Method: In order to improve the physical design of the Mario Kart bike and clean up the exposed wiring to create a form that is more like commercial products, communication between the sensors and main RPi shall be wireless.

# Buildable Schematic
![HC05](https://user-images.githubusercontent.com/100988295/203235006-bb78facc-8def-4111-ab6c-089bd7539251.jpg)
![SteeringSchem](https://user-images.githubusercontent.com/100988295/203235130-78f5ef26-e984-4a32-a749-8757b2b3a3db.jpg)
![SpeedSchem](https://user-images.githubusercontent.com/100988295/203235176-6876e46d-63d1-41c2-982d-f652e5ed1a0e.jpg)

# Analysis
Selection of the steering sensor’s microcontroller was the first order of business. The Arduino brand was selected due to their microcontrollers being generally simple, effective, and cheap. From here, the power constraint needed to be focused on, as some Arduino microcontrollers surpass the 5 V limit and others are at 5 V exactly. From here, the Arduino Nano 33 BLE was selected. The 33 BLE is a low power microcontroller that has an integrated Bluetooth module utilizing version Bluetooth Low Energy. BLE is a variation of Bluetooth 4.0, sacrificing range of transmission (100m to 50m) and data throughput (2.1-0.7 Mbps to 0.27 Mbps) in exchange for low power consumption. The loss of range and data throughput are acceptable losses, due to the sensors being within 5m of the master RPi, and the throughput still being more than acceptable for the amount of data that will be transmitted. The Nano 33 BLE satisfies the very important power constraint, while also having little to no drawbacks in function. Another benefit of the 33 BLE is its size, it being Arduino’s smallest board, measuring at 45x18mm. Size is an important aspect due to the location of the microcontrollers being along the metal pipes of the bike. This small microcontroller will be out of the way, and will be very easy to conceal in an effort to improve the design of the Mario Kart Bike. For the speed sensor’s microcontroller, the Nano 33 BLE Sense was chosen. This microcontroller is exactly the same as the standard Nano 33 BLE, with the addition of a few built in sensors. One of these sensors is a light sensor that will be specifically needed when measuring the revolutions of the tire, which leads to speed. An infrared light will be sent between the outer wheel and the axel, hitting the spokes of the bike as the user pedals. With the light sensor from the BLE Sense on the other side of the wheel, we can use the breaks in the light to calculate the speed of the user, instead of the current method that uses tape along the bike. The Sense is also helpful in that the light sensor is built into the microcontroller, meaning that everything needed is housed together and extra wiring is not needed.

Coding of the Bluetooth modules and their respective microcontrollers will be accomplished in the Arduino IDE. This text editing platform is specifically used to program and communicate with Arduino hardware. Code will be written in C++ or C, as this is the language our team has the most experience with. Designation of microcontrollers is important, with the sensor’s microcontrollers being peripheral, strictly sending data; the RPi housed in the main component box will be considered the central microcontroller, or master, mainly receiving data from the peripheral microcontrollers and also potentially controlling them if need be.

Bluetooth also uses a concept of profiles. Profiles are a specification for Bluetooth communication that basically create a set of rules that allow certain tasks to be accomplished. Our sensors will be strictly sending bit data to a central RPi, so we will be using the Serial Port Profile (SPP).  This profile defines how to set up virtual serial ports and connect two Bluetooth enabled devices. As of now, the central RPi doesn’t have a Bluetooth module, so one needed to be purchased for Bluetooth connectivity. The HC-05 module seems to be the best fit, as it works as master or slave (flexible), is compatible with the Arduino Nano 33 BLE and BLE Sense, and also supports the SPP Bluetooth profile.

# BOM
| Component                 | Cost    |
|---------------------------|---------|
| Arduino Nano 33 BLE       | $26.30  |
| Arduino Nano 33 BLE Sense | $40.50  |
| HC-05 Bluetooth module    | $10.39  |


