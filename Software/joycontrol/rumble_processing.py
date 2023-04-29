# Imports
import time
import serial
from numpy import random

# Initializations
actuatorControl = serial.Serial('/dev/rfcomm0')
#resistance_state = 0 # Resistance state to be requested by the linear actuator.
button_prev = False
# Functions
def set_resistance(state):
    #resistance_state = state
    actuatorControl.write(state.encode())

def get_resistance():
    return resistance_state

#def three_rotations():
 #   button_count = 0
  #  while True:
   #     if button_count == 50:
    #        button_count = 0
     #       button_prev = False
      #      return True

       # if button_prev is True and command.a_button.ispressed() is False:
        #    button_prev = False
        #elif button_prev is False and command.a_button.ispressed() is True:
         #   button_prev = True
          #  button_count = button_count + 1
        
# Main Loop
while True:
    #print("Input four bytes here with spaces in between in form")
    #input1 = input()
    #byte1, byte2, byte3, byte4 = input1.split()
    #byte1 = int(byte1, 16)
    #byte2 = int(byte2, 16)
    #byte3 = int(byte3, 16)
    #byte4 = int(byte4, 16)
    rng = random.randint(100)
    if rng <= 5:
        rumble_data = [0xa2, 0x10, 0, 0x80, 0x6a, 0x60, 0x80,0x80, 0x6a, 0x60, 0x80, 0 ,0 ,0]
    elif rng <= 15:
        rumble_data = [0xa2, 0x10, 0, 0xca, 0x00, 0x00, 0x40,0xca, 0x00, 0x00, 0x40, 0 ,0 ,0]
    else:
        rumble_data = [0xa2, 0x10, 0, 0,0,0,0,0,0,0,0, 0 ,0 ,0]
    #rumble_data = [0xa2, 0x10, 0, byte1, byte2, byte3, byte4, byte1, byte2, byte3, byte4,0 ,0 ,0]
    if rumble_data[0:2] == [0xa2, 0x10]:
        if rumble_data[3:7] == [0x80, 0x6a, 0x60, 0x80]:
            print("Hit by shell!\n")
            set_resistance('650')
            time.sleep(5)
        
        elif rumble_data[3] == 0xca and rumble_data[6] == 0x40:
            print("You're offroad!\n")
            set_resistance('512')
            time.sleep(5)
                
        elif rumble_data[3] == 0x67 and rumble_data[6] == 0x58:
            print("You're offroad!\n")
            set_resistance('256')
            time.sleep(1)

        elif rumble_data[3] == 0xdc and rumble_data[6] in range(0x40, 0x50, 0x01):
            print("You're offroad!\n")
            set_resistance('256')
            time.sleep(1)

        elif rumble_data[3] == 0x62 and rumble_data[5:7] == [0x63, 0x40]:
            print("You're offroad!\n")
            set_resistance('256')
            time.sleep(1)
        else:
            print("Nothing special is happening.\n")
            set_resistance('1')
            time.sleep(1)




