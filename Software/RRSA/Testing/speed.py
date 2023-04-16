#TESTS SPEED SENSING
from gpiozero import Button
import time

reed = Button(11)
wheel_period = 0.0
wheel_speed = 0.0
reed_trig_T1 = 0.0
reed_trig_T2 = 0.0
while True:
	reed.wait_for_press()
	reed_trig_T1 = time.time()
	reed.wait_for_release()
	reed.wait_for_press()
	reed_trig_T2 = time.time()
	reed.wait_for_release()
	wheel_period = reed_trig_T2 - reed_trig_T1
	wheel_speed = 2.0*3.141592653589793/wheel_period
	print("Angular Velocity: ", wheel_speed, " rad/s")
