# Mario Kart Bike V2

## Executive Summary

The Capstone Design Project Team 4 collaborated to further enhance the riding experience offered by the existing Mario Kart Bike design. Team 4’s design adds a variable of resistance for two modes of operation: the Mario Kart Game Simulation and a Ride Replay Simulation (RRS).  

Improvements to the previous iteration of the Mario Kart Bike offer new dimensions of realism by adding a more dynamic resistance system, while the RRS enables users to record an actual bike ride and then replay it later indoors. Using data gathered from various sensors and an internal physics engine, the RRS processing subsystem calculates whether to speed up or slow down video playback based on the speed the user is pedaling, and it determines the appropriate resistance to apply.

The streamlined resistance system design replaced the cumbersome motor with a linear motor attached to an array of magnets, located perpendicular to a conductive flywheel to generate eddy currents. Opposing magnetic fields generate braking torque in the flywheel, which is transferred to the real bike wheel. This braking torque functions as the resistance felt by the user. The magnetic resistance system utilizes 85 states to create a smooth and realistic replay. The new resistance system also works in the original Mario Kart Bike Mode. 

Team 4 believes the Mario Kart Bike will have a significant impact on the general health of society when the commercialized version is used by Mario Kart enthusiasts and other gamers to participate in physical activity. We also believe our research to achieve a dynamic resistance system can be leveraged for other engineering applications.  


## Capabilities

The Dynamic Resistance System works as designed, providing resistance in the form of braking torque. At a minimum of 411 RPM of the flywheel, the maximum achievable braking torque is 19.432 Nm, and the minimum achievable braking torque is 0.097 Nm. At a maximum of 2,258 RPM of the flywheel, the maximum achievable braking torque is 38.865 Nm, and the minimum achievable braking torque is 0.972 Nm. The bike can be used to play Mario Kart levels, as well as dynamically apply resistance in the Mushroom Cup, via serial commands to the linear actuator. An HDMI switcher button and a play time popup were also implemented. Ride replay data gathering was a success. The Steering Sensor Subsystem is wireless and work as designed. The Speed Sensor Subsystem is hardwired and works as designed. The battery pack power supply for the Steering and Speed Sensor Subsystems is adequate for 2 weeks of run time while in constant use for 4 hours a day. Power distribution and protection comply with the design requirements. 


## Salient Outcomes

##### Dynamic Resistance System
- Resistance felt by the user is applied comparable an exercising spin bike
- Eddy currents are created by moving two magnets closer to a rotating aluminum disk
- Mode of operation: Mario Kart Gaming Simulation 
- Resistance system control
  - PID controller (Arduino Nano, PID_v1 library, maintains 25% duty cycle)
  - MOSFET H-Bridge with discrete components

##### Ride Replay Module (RRSA)
- Data collection (video, elevation, and speed)
- Data storage (removeable 128 GB SD card)
- Data processing (Raspberry Pi Zero W2 specified; Raspberry Pi B2 used due to supply shortage)
- Sensors 
  - Speed (utilizes a magnetic switch (reed switch) and a magnet mounted on bike wheel spoke)
  - Elevation (utilizes a pressure sensor)
- Automatic shutdown on low battery
- Battery life indicator LEDs on power supply

##### Steering and Speed Sensor Subsystems 
- Replaced Speed controller with an Arduino Nano 33 BLE to transfer data by Bluetooth communication
- Added Arduino Nano 33 BLE to the Steering Subsystem to enable the transfer of data by Bluetooth communication
- Designed system to power the Sensor Subsystems using battery packs with 4 lithium AA batteries
- MOSFET was added in the Speed Sensor circuit to save power

##### Steering Sensor Mount Enhancement
- Strengthened and stabilized steering sensor mount 
- Replaced existing plastic 3D printed L-Bracket with metal L-Bracket for enhanced strength
- Attached L-Bracket to bike with conduit hanger for stability 

##### Power Distribution
- Provides device and system protection
- Installation of over protection and Ground Fault Interruption (GFI) protection
- Complete replacement of 120 VAC power supply

## Project Demonstration & Images

We plan on posting a link to a video showcasing the Mario Kart Bike, as well as images of the project when production is completed.

## About Us

### Team

Team 4 is a 5-person Capstone Design Project Team at Tennessee Technological University, who began Revision 2 of the Mario Kart Simulation Project during the Fall 2022 semester. Team members are Blake Pickett, Ray Durlin, Tyler Chittum, Benjamin Reed, and Sage Mooneyham. All members worked on the Resistance System.
<br />

![samooneyha43](https://user-images.githubusercontent.com/118228609/204955069-5617f7d6-c4db-4fd1-b2a3-732c5af7caee.jpeg)
##### Sage Mooneyham
- Computer Engineering Major
- Software/Coding
- Bluetooth Communication
<br />

![bcpickett42](https://user-images.githubusercontent.com/118228609/204954952-6079d263-4d1e-48e7-8d34-d9937e9ed811.png)
##### Blake Pickett
- Electrical Engineering Major
- Hardware
- Sensor System
- Steering System
<br />

![bdreed43](https://user-images.githubusercontent.com/118228609/204954921-bbedaad3-1c52-4cc3-909e-dcdc8ed76ba5.png)
##### Benjamin Reed
- Computer Engineering Major
- Software/Coding
- HDMI Switching System
<br />

![thchittum42](https://user-images.githubusercontent.com/118228609/204954827-8bc5f440-cad9-4cd9-8ab2-526fa8b15040.jpg)
##### Tyler Chittum
- Electrical Engineering Major
- Hardware
- Ride Replay Simulation Acquisition (RRSA) System
<br />

![rjdurlin42](https://user-images.githubusercontent.com/118228609/204953756-6faef26e-8d7b-40a0-a6fc-cdfcfbd8a586.png)
##### Ray Durlin
- Electrical Engineering Major
- Hardware
- Power Distribution System


### Faculty Supervisor

The faculty advisor for this project is Jesse Roberts.

### Stakeholders

The main customer for this project is Jesse Roberts, however a commercialized version of this product would likely garner attention from people who enjoy playing Mario Kart, fitness, and/or cycling.

### Recognition

We would like to recognize the work of Reed Hester, Chase Griffin, and Leah Faulkner, the engineers who designed the first iteration of the Mario Kart Bike.


## Repo Organization


### [Reports](https://github.com/rjdurlin42/mariokartrev_2_team_4/tree/main/Reports)

Completed reports can be found in the Reports folder, or by clicking the link above.

### [Documentation](https://github.com/rjdurlin42/mariokartrev_2_team_4/tree/main/Documentation)

Project documentation can be found in the Reports folder, or by clicking the link above.

### [Software](https://github.com/rjdurlin42/mariokartrev_2_team_4/tree/main/Software)

Written software can be found in the Reports folder, or by clicking the link above.
