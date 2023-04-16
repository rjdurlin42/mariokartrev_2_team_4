#TEST OF RECORDING BUTTON ILLUMINATION
from gpiozero import LED, Button

rec_led = LED(4)
rec_led.on() #Need to initialize as on, since logic is inverted
rec_button = Button(1)
while True:
	rec_button.wait_for_press()
	rec_led.off() #Again, logic inverted; this makes the light turn on
	rec_button.wait_for_release()
	rec_led.on()
