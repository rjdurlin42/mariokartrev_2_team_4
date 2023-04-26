import os
import numpy
import time
import serial
import math

ser = serial.Serial('/dev/ttyS0', 9600, timeout=0.01)
ser.reset_input_buffer()

initial = 0
rate = 0.0
rate2 = 0.0
finalRate = 0.0
revsPerSec = 0.0
radsPerSec = 0.0
rate_in = 0.0
T1 = 0.0
T2 = 0.0
cycle_check = 0
while True:
    if ser.in_waiting > 0:
        rate = float(ser.readline().decode('utf-8').rstrip())
        
        if rate == None:
            print("in rate == none")
            rate = rate2
    if rate2 != rate:
        T1 = time.time() #Time of last change in rate
    else:
        T2 = time.time() #Current time provided rate has not changed
    if T2 - T1 > 0.5: #Set rate timeout to one second
        rate = 0.0
        rate2 = 0.0
    rate2 = rate
    finalRate = rate
    if finalRate == 0:
        radsPerSec = 0
    else:
        revsPerSec = 1 / finalRate
        radsPerSec = revsPerSec * 6.283
        if radsPerSec > 32:
            radsPerSec = 32
        if cycle_check == 10000:
            print("Speed: ",radsPerSec)
            cycle_check = 0
        else:
            cycle_check += 1
