#Data sampling program for the RRSA subsystem

import picamera2
from libcamera import Transform
import time #Needed to determine speed of bike and take samples at discrete intervals
from gpiozero import LED, Button
import board
from adafruit_dps310.basic import DPS310 #Execute sudo pip3 install adafruit-circuitpython-dps310 in the terminal to make this work
from threading import Thread

#The classes below are meant to run in different threads to enable parallel processing of the data
#Thread application based on: http://robsraspberrypi.blogspot.com/2016/01/raspberry-pi-python-threading.html
class Get_Speed:
	def __init__(self):
		self._running = True
	def terminate(self):
		self._running = False
	def run(self):
		global wheel_speed
		global pause
		while self._running:
			while pause:
				pass
			reed.wait_for_press()
			reed_trig_T1 = time.time()
			reed.wait_for_release()
			reed.wait_for_press()
			reed_trig_T2 = time.time()
			reed.wait_for_release()
			wheel_period = reed_trig_T2 - reed_trig_T1
			wheel_speed = 2.0*3.141592653589793/wheel_period #bike wheel angular velocity in rad/s

class Get_Pressure:
	def __init__(self):
		self._running = True
	def terminate(self):
		self._running = False
	def run(self):
		global pressure
		global pause
		dps310.initialize() #starts the pressure sensor in continous measurement mode
		while self._running:
			while pause:
				pass
			dps310.wait_pressure_ready()
			pressure = dps310.pressure
		dps310.reset() #uninitializes the sensor, stopping measurements

class Log_Data: #logs the data at ~10 Hz
	def __init__(self):
		self._running = True
	def terminate(self):
		self._running = False
	def run(self):
		global pressure
		global wheel_speed
		global pause
		while self._running:
			while pause:
				pass
			spd_f = open(spd_name, "w")
			alt_f = open(alt_name, "w")
			while pause == False:
				spd_f.write("%.3f"%wheel_speed)
				spd_f.write("\n")
				alt_f.write("%.3f"%pressure) #records the pressure in hPa (has 0.002 hPa precision)
				alt_f.write("\n")
				time.sleep(0.1)
			spd_f.close()
			alt_f.close()

#The below is needed to initialize the threads
gs = Get_Speed()
gs_thread = Thread(target=gs.run)
gp = Get_Pressure()
gp_thread = Thread(target=gp.run)
ld = Log_Data()
ld_thread = Thread(target=ld.run)

#NOTE: the number of zeros determines the max number of files which may be recorded before overwriting the first.
vid_name = "/home/rrsa/recordings/vid_0.h264"
alt_name = "/home/rrsa/recordings/alt_0.txt"
spd_name = "/home/rrsa/recordings/spd_0.txt"

rec_inc = 0 #tracks index of correct file number

 #Used to make rec_inc variable persistant across sessions
inc_file = open("/home/rrsa/scripts/rec_inc.txt", "r")
rec_inc = int(inc_file.read())
inc_file.close()
if rec_inc != 0:
	vid_name = vid_name.replace("0", str(rec_inc), 1)
	alt_name = alt_name.replace("0", str(rec_inc), 1)
	spd_name = spd_name.replace("0", str(rec_inc), 1)

rec_led = LED(4)
rec_led.on() #Turns recording light off (inverted logic)
rec_button = Button(1)
reed = Button(11) #speed sensing reed switch
wheel_period = 0.0
global wheel_speed #speed measured in angular velocity
global pressure  #pressure in hPa
global pause #boolean to stop execution of threads when not recording
wheel_speed = 0.01 #Initialize wheel speed to a very small nonzero value (relative framerate calculations require division by this number)
pressure = 1013.25 #Initialize pressure to one atmosphere
pause = False

#absolute times of reed switch triggering
reed_trig_T1 = 0.0
reed_trig_T2 = 0.0

i2c = board.I2C()
dps310 = DPS310(i2c)

cam = picamera2.Picamera2()
video_config = cam.create_video_configuration(main={"size":(1280,720)})
video_config["transform"] = Transform(hflip=1,vflip=1) #Transform is used to account for orientation of camera. Camera could be manually oriented instead.
cam.configure(video_config)
#cam.set_controls({"FrameDuration":(16666.66666666,16666.66666666)}) #Set to 60 FPS (default 30); inaccurate code - left as placeholder

#Starts the threads
gs_thread.start()
gp_thread.start()
ld_thread.start()

while 1: #Main loop; handles video recording and executive functions
	rec_button.wait_for_press()
	pause = False
	cam.start_recording(picamera2.encoders.H264Encoder(bitrate=6500000), vid_name) #Record with 6.5 Mbps bitrate
	rec_led.off() #Uses inverted logic; this turns it on
	rec_button.wait_for_release()
	cam.stop_recording()
	pause = True

	#Use the below to terminate the threads if the program ever needs to be stopped
	#gs.terminate()
	#gp.terminate()
	#ld.terminate()

	rec_inc = rec_inc + 1

	#Report the current recording number of the presently recorded recording by flashing the recording light
	#ADDENDUM: if the recordings have looped around, this is the number or recordings since the loop began, not the total number of recordings
	for i in range(rec_inc):
		rec_led.on()
		time.sleep(0.3)
		rec_led.off()
		time.sleep(0.3)

	#Limits total recordings to 10; overwrites first recording when an 11th recording is made
	if rec_inc > 9:
		rec_inc = 0

	vid_name = vid_name.replace(str(rec_inc - 1), str(rec_inc), 1)
	alt_name = alt_name.replace(str(rec_inc - 1), str(rec_inc), 1)
	spd_name = spd_name.replace(str(rec_inc - 1), str(rec_inc), 1)
	inc_file = open("/home/rrsa/scripts/rec_inc.txt", "w")
	inc_file.write(str(rec_inc)) #Writes new file index to file to preserve variable across sessions
	inc_file.write("\r")
	inc_file.close()
	rec_led.on() #Inverted logic; this turns it off
