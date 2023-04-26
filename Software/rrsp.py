# Imports
#from GUI import *
import os
import glob
import numpy
import vlc
import time
import serial
import math

instance = vlc.Instance()

# Global variables
ser = serial.Serial('/dev/ttyS0', 9600, timeout=0.01)
ser.reset_input_buffer()
actuatorControl = serial.Serial('/dev/rfcomm0', 9600)

initial = 0
rate = 0.0
rate2 = 0.0
finalRate = 0.0
revsPerSec = 0.0
radsPerSec = 0.0
rate_in = 0.0
T1 = 0.0
T2 = 0.0
alt_prev = 0 # User's current altitude
alt_curr = 0 # User's next altitude from data
velocity = 0 # Angular velocity of bike
torque_count = 0 # Variable for counting torque values
torque_check = False # For leaving while loop
torque_res = 0 # Torque for resistance system
torque_calc = 0 # Calculated torque from get_torque()
speeds = open("spd_2.txt")
velocities = speeds.read().splitlines()
speeds.close()
pressures = open("alt_2.txt").read().splitlines()
altitude_list = []
numpy.seterr(divide = 'ignore')

# Torque values to be applied to the Resistance System
torques = [ 0.1096, 0.1180, 0.1264, 0.1433, 0.1601, 0.1770, 0.1938, 0.2107, 0.2275,
            0.2444, 0.2697, 0.2950, 0.3202, 0.3455, 0.3708, 0.4045, 0.4382, 0.4719,
            0.5057, 0.5478, 0.5899, 0.6321, 0.6826, 0.7332, 0.7922, 0.8512, 0.9186,
            0.9860, 1.0619, 1.1377, 1.2220, 1.3147, 1.4074, 1.5085, 1.6180, 1.7360,
            1.8624, 1.9972, 2.1404, 2.2920, 2.4605, 2.6374, 2.8227, 3.0249, 3.2438,
            3.4712, 3.7154, 3.9764, 4.2626, 4.5655, 4.8853, 5.2302, 5.6003, 5.9954,
            6.4157, 6.8693, 7.3564, 7.8768, 8.4304, 9.0255, 9.6621, 10.340, 11.067,
            11.844, 12.677, 13.568, 14.524, 15.544, 16.636, 17.807, 19.057, 20.393,
            21.821, 23.355, 24.994, 26.750, 28.629, 30.641, 32.788, 35.086, 37.543,
            40.145, 42.989, 46.002, 49.228]
# Functions
def speed():
    global ser
    global initial
    global rate 
    global rate2 
    global finalRate
    global rate_in
    global revsPerSec
    global radsPerSec
    global T1
    global T2
#     if(initial < 1):
#         user_input = await ainput(prompt='cmd >> ')
#         initial += 1
#         rate = 0.0
    if ser.in_waiting > 0:
        rate = float(ser.readline().decode('utf-8').rstrip())
        print("This is rate: ",rate)
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
        print("Speed: ",rate)
    return radsPerSec


def pressure_convert(pressure_list):
    altitude_list = [len(pressure_list)]
    for pressure in range(len(pressure_list)):
        # Note the 288.706 is (temperature in F + 459.67)*5/9 where temp is 60 F. A thermometer can be used to further improve realism
        altitude_list.append(numpy.log((float(pressure)*100)/101325)*287.053*(288.706))
    return altitude_list
       
def set_torque(alt_prev, alt_curr, velocity):
    mass = 180 * 0.453592 # GUI functionality is being problematic due to its connection to the Switch. Average American weight of 180 lbs is used
    gravity = 9.81
    energy_change = (alt_curr - alt_prev) * mass * gravity
    power = energy_change/0.100 # Time period is 100 ms
    if velocity == 0:
        return 0
    else:
        torque = power/velocity
        return torque

def set_state(torque, velocity):
    # Primary variables
    radius_magmain = 0.0254 # Radius of a single magnet in meters
    conductivity = 3.77*(10^7) # of aluminum
    thickness_fly = 0.00635 # in meters
    diameter_mag = 0.1016 # in meters. Note that this is the effective diameter when using all magnets
    radius_fly = 0.0508 # in meters
    mu0 = 4*3.1415*(10^-7) # Magnetic permeability in a vacuum
    
    # Variables for dipole
    Br = 1.48 # Max residual flux density in Tesla
    volume_mag = 3.1415*(radius_magmain*radius_magmain)*thickness_fly # Volume of a magnet
    dipole = Br*volume_mag/mu0 # Magnetic dipole moment

    # Calculation for distance
    numerator = 2*mu0*dipole*(numpy.sqrt(torque))
    denominator = 40000*(5.568)*numpy.sqrt((conductivity*(diameter_mag*diameter_mag)*thickness_fly*(radius_fly*radius_fly)*velocity))
    x = numerator/denominator
    distance = numpy.cbrt(x)
    if math.isnan(distance) == True:
        distance = 0.0
    #actuatorRatio = 1 - (distance/0.1016)
    #actuatorActual = int(750 * actuatorRatio)
    #actuatorControl.write(b'900') # Return relation of distance versus total extension of actuator
    

def find_torque(torque_calc):
    torque_check = False
    torque_count = 0
    while torque_check is False:
        
        if torque_count < 84:
            if torque_calc <= torques[torque_count+1] and torque_calc >= torques[torque_count]:
                torque_res = torques[torque_count]
                torque_check = True
            else:
                torque_count = torque_count + 1
                
        elif torque_count == 84:
            if torque_calc >= torques[torque_count]:
                torque_res = 49.228
                torque_check = True

            else:
                torque_res = 0
                print("ERROR: Torque not in range")
                torque_check = True
    #check this
    return torque_res
    #-----

#         else:
#             if torque_calc >= ((torques(torque_count) + torques(torque_count-1))/2) and ((torques(torque_count+1) + torques(torque_count))/2):
#                 torque_res = torques(torque_count)
#                 torque_check = True
#             else:
#                 torque_count = torque_count + 1

def set_video(velocity, velocity_recorded):
    framerate_multiplier = velocity/velocity_recorded
    vidRate = float(framerate_multiplier)
    #p.set_rate(vidRate)


altitudes = pressure_convert(pressures)
run_index = 0 # Tracking point in run files
player = instance.media_player_new()
media = instance.media_new("vid_2.h264")
player.set_media(media)
player.play()
#p = vlc.MediaPlayer("vid_2.h264")
#p.play()
while True:
    velocity = speed()
    print("Velocity: ",velocity)
    if alt_curr != 0:
        alt_prev = alt_curr
    alt_curr = altitudes[run_index]
    setTorque = set_torque(alt_prev, alt_curr, velocity)
    print("Torque to be set: ",setTorque)
    findTorque = find_torque(setTorque)
    set_state(findTorque, velocity)
    print("setState")
#     set_video(velocity, float(velocities[run_index]))
    run_index = run_index + 1
    #velocities.close()
    #pressures.close()

