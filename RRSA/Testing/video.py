#TEST RECORDING TO VIDEO FILE AS CONTROLLED BY BUTTON

import picamera2
from libcamera import Transform
from gpiozero import Button, LED

rec_button = Button(1)
rec_led = LED(4)
rec_led.on()
cam = picamera2.Picamera2()
video_config = cam.create_video_configuration(main={"size":(1280, 720)})
video_config["transform"] = Transform(hflip=1,vflip=1)
cam.configure(video_config)
rec_button.wait_for_press()
cam.start_recording(picamera2.encoders.H264Encoder(bitrate=10000000),"/home/rrsa/recordings/test_video1.h264")
rec_led.off()
rec_button.wait_for_release()
cam.stop_recording()
print("DONE")
