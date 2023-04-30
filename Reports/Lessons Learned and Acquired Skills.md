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

