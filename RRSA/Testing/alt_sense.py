#TEST OF ALTITUDE SENSOR
import time
import board
from adafruit_dps310.basic import DPS310
i2c = board.I2C()
dps310 = DPS310(i2c)
dps310.initialize()
while True:
	dps310.wait_pressure_ready()
	print("Pressure = %.6f hPa"%dps310.pressure)
