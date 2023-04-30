# Lessons Learned and Acquired Skills

## Tyler Chittum
### Lessons
1. Limitations of mechanical durability: the mounting bracket for the RRSA subsystem unexpectedly broke rather easily during testing by riding off a curb. This occured because the mounting bracket was too weak, the mounting location was not at the center of gravity, and the bike used lacked any form of damping on the suspension. In addition, the glue used to attempt to repair it did not hold, and in fact failed to harden normally. The five-minute epoxy we used seems to have been a bad batch. A sturdier mounting bracket or more centered mounting location may have averted this issue.
2. Limitations of Raspberry Pi video recording: the Raspberry Pi used in the RRSA subsystem unexpectedly drops frames during recordings. This results in desync with the data which cannot be resolved by simply shifting or clipping the data.
3. Pressure sensing requires airflow to the sensor.
4. It is important to use ESD protection to avoid damaging components. A failure to adequitely protect against ESD unexpectedly resulted in the failure of two key components (ADC and Arduino Nano).
6. Limitations of Raspberry Pi video playback: the Raspberry Pi has some rather shoddy video playback, and the one in use as the main controller in this project is all the less capable given that it is running a desktop operating system.
7. Always get permission before touching other people's work.
8. The manufacturer-provided PID coefficients for the utilized actuator did not provide stable operation using our controller, which meant that we had to manually tune the device.
9. As per Mr. Roberts advice: linear actuator duty cycle is not a valid rating on a very minute timescale, which is to say that PWM duty cycle is not a valid means to meet such a specification as was done for the RRS control subsystem.
10. In terms of management, we found having no leader to work fine, but I feel that teamwork was much more effective when decisions regarding who would do what were made at meetings rather than left up to whoever decided to take action.
11. Communication was most effective when going through only one channel.
12. If you feel stuck, it is a good idea to ask others for help, and you should always be willing to help as well.
13. The pin socket header used to connect the wireless module on the RRS controller subsystem is too short, and does not do a good job of holding the wireless module or normal wire pins, particularly when the enclosure vibrates. The lesson here is that deeper pin sockets are better.
### Acquired Skills
1. 3D modeling for signoffs.
2. Teamwork, particularly getting a feel for when it is or isn't beneficial to try to help.
3. Presenting, which was required several times throughout the process.
4. Time management; particularly knowing when to give up/ignore things when not doing so would result in worse overall consequences due to eating into time needed for more important tasks.

## Ray Durlin
### Lessons learned
1. It is important to be as detailed as possible in the design phase of a project to ensure that the implementation is better efficient
2. Project outcome identification and analyzing measure of success
3. Better understanding of how to meet deadlines and expectations 
4. Importance of teamwork in a group setting
5. Presenting work to different types of audiences
6. Effectively communicating with others
7. How to be a better problem solver
8. Value of overcoming obstacles
9. Do not be afraid to ask for help
10. Allows look for better ways to improve, countinous improvement will lead to a desireable outcome
11. When in doubt, look at the manufacturers datasheet, or call the manufacture to ask questions - Use all the resources available

### Skills Acquired
1. AutoCAD 
2. Project Design
3. Detailed knowledge of GFCI and Overprotection
4. Fabricating components
5. Hands on system implementation
6. Analysis and Experimentation
7. Theoretical Modeling
8. MATLAB – Simulink
9. Electrical troubleshooting

## Blake Pickett
### Lessons
1. Impact of Logistics on project success
2. Effective collaboration and communication are critical
3. Clear, concise, and up-to-date documentation is critical
4. Better understanding of Eddy Currents and Magnetic Fields
5. Better understanding of Bluetooth Communication and how Arduinos work
6. Better understanding of how a Potentiometer works
7. Better understanding of Battery Power Supply
8. Better understanding of the impacts of Procurement process
9. Backup plan is necessary for Risk Mitigation (e.g., technical performance, parts/supplies delivery, etc.)

### Skills Acquired
1. Power estimation and supply for Electronics
2. Arduino installation
3. AutoCAD
4. Design implementation and fabrication (e.g., L-Bracket, Flywheel, Magnet Bracket, Actuator Bracket)
5. Testing, analysis and experimentation
6. Troubleshooting
7. Improved Soldering skills for Electronics application
8. Improved Technical Writing skills (e.g., proposal, reports)
9. Electronic subsystem removal and documentation 
10. Integration of new Subsystem components with existing components 

## Sage Mooneyham
### Lessons
1.	Some hardware can be unexpectedly fragile
2.	Software libraries are very helpful
3.	RPi’s are quite finnicky
4.	It’s important to constantly have backups (plans, files, etc.)
5.	When picking up another teams work, it’s beneficial to have contact with the previous team
6.	Reading data sheets is important

### Skills Acquired
1.	Bluetooth programming
2.	Python programming
3.	Design Implementation
4.	Debugging
5.	Command terminal navigation
6.	Arduino Nano programming
7.	Incorporating someone else’s work in your own
8.	Serial communication
9.	Time management
10.	Presenting
11.	Working in a team

## Benjamin Reed
### Lessons
1. When inheriting a project from another team, it is imperative that determination of how the hardware and software works occur very early in the development process. 
2. Adequate documentation is necessary to allow future teams to be able to improve the design properly. 
3. If utilizing any video, ensure that the hardware you are using, specifically the graphics card, is capable of handling the video you intend to use. 
4. Software development needs to begin very early. Even as early as the conceptual design. 
5. Go ahead and have a basic idea of how you could run experiments on hardware during the design phase to have a head start. 
6. If a software component is imperative for the function of your design, then checking if that component can be used should be considered part of that design. 
7. It is important to understand the schedules of your teammates and to plan the project accordingly to those schedules. 
8. In addition to the importance of documentation, it is as important to document while designing, researching, and building for the project. 
9. If you have a plan, there is a very good chance that plan does not come to fruition. It is, however, better than having no plan and, therefore, no direction. 
10. I cannot stress enough the importance of documentation. Nobody is going to think the way you do, so every detail needs to be discussed and conveyed in a digestible manner. 
11. It is important to state everything explicitly. Even if information can be assumed, such as hardware having the appropriate specifications according to their datasheets, the fact that it has room to be assumed introduces an unnecessary possibility of error. 

### Skills Acquired
1. Reverse-engineering the work of a previous design. 
2. Hardware design and datasheet analysis. 
3. Python GUI development via the TKinter package. 
4. Python video manipulation via the VLC package. 
5. Skills associated with presenting to an audience. 
6. Skills associated with working with a team. 
7. Programming for a Raspberry Pi. 
8. Hardware testing and analysis. 
9. Conveying complex ideas to individuals that lack the knowledge you possess. 
