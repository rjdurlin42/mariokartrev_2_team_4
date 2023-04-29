# Imports
import serial
import time

# Constants for Linear Actuator positions
NOMINAL = b'1'
NO_RES = b'300'
SMALL_HILL = b'600'
MED_HILL = b'650'
BIG_HILL = b'675'
WATER = b'675'
WATER_HILL = b'725'
SODA = b'750'

motorCon = serial.Serial('/dev/ttyS0', 9600, timeout=0.01)
motorCon.reset_input_buffer()

def mk_stadium():
    enterCheck = input("Press Enter when race is starting.")
    if enterCheck == "":
        print("Race at Mario Kart Stadium is starting...")
        time.sleep(4)
        motorCon.write(NO_RES)
        print('3!')
        time.sleep(1)
        print('2!')
        time.sleep(1)
        print('1!')
        time.sleep(1)
        print("GO!")
        for i in range(0, 3):
            motorCon.write(NO_RES)
            time.sleep(13)
            motorCon.write(SMALL_HILL)
            time.sleep(9)
            motorCon.write(NO_RES)
            time.sleep(5)
            motorCon.write(BIG_HILL)
            time.sleep(6)
            motorCon.write(NO_RES)
            time.sleep(9)
            motorCon.write(SMALL_HILL)
            time.sleep(2)
            motorCon.write(NO_RES)
            time.sleep(2)
    motorCon.write(NOMINAL)
    print("Race complete!")
    time.sleep(3)

    enterCheck = input("Press Enter when race is starting.")
    if enterCheck == "":
        return

def water_park():
    print("Race at Water Park is starting...")
    time.sleep(4)
    motorCon.write(NO_RES)
    print('3!')
    time.sleep(1)
    print('2!')
    time.sleep(1)
    print('1!')
    time.sleep(1)
    print("GO!")
    for i in range(0, 3):
        motorCon.write(NO_RES)
        time.sleep(3)
        motorCon.write(SMALL_HILL)
        time.sleep(1)
        motorCon.write(NO_RES)
        time.sleep(6)
        motorCon.write(MED_HILL)
        time.sleep(4)
        motorCon.write(WATER)
        time.sleep(4)
        motorCon.write(WATER_HILL)
        time.sleep(2)
        motorCon.write(BIG_HILL)
        time.sleep(7)
        motorCon.write(NO_RES)
        time.sleep(4)
        motorCon.write(WATER)
        time.sleep(9)
        motorCon.write(WATER_HILL)
        time.sleep(2)
        motorCon.write(NO_RES)
        time.sleep(6)
    motorCon.write(NOMINAL)
    print("Race complete!")
    time.sleep(3)
    enterCheck = input("Press Enter when race is starting.")
    if enterCheck == "":
        return
    
def ss_canyon():
    print("Race at Sweet Sweet Canyon is starting...")
    time.sleep(4)
    motorCon.write(NO_RES)
    print('3!')
    time.sleep(1)
    print('2!')
    time.sleep(1)
    print('1!')
    time.sleep(1)
    print("GO!")
    for i in range(0, 3):
        motorCon.write(SMALL_HILL)
        time.sleep(11)
        motorCon.write(NO_RES)
        time.sleep(10)
        motorCon.write(SODA)
        time.sleep(6)
        motorCon.write(BIG_HILL)
        time.sleep(5)
        motorCon.write(NO_RES)
        time.sleep(7)
        motorCon.write(MED_HILL)
        time.sleep(2)
        motorCon.write(SMALL_HILL)
        time.sleep(2)
        motorCon.write(MED_HILL)
        time.sleep(1)
        motorCon.write(NO_RES)
        time.sleep(4)
    motorCon.write(NOMINAL)
    print("Race complete!")
    time.sleep(3)
    enterCheck = input("Press Enter when race is starting.")
    if enterCheck == "":
        return
    
def thwomp_ruins():
    print("Race at Thwomp Ruins is starting...")
    time.sleep(4)
    motorCon.write(NO_RES)
    print('3!')
    time.sleep(1)
    print('2!')
    time.sleep(1)
    print('1!')
    time.sleep(1)
    print("GO!")
    for i in range(0, 3):
        motorCon.write(NO_RES)
        time.sleep(3)
        motorCon.write(SMALL_HILL)
        time.sleep(8)
        motorCon.write(NO_RES)
        time.sleep(11)
        motorCon.write(MED_HILL)
        time.sleep(2)
        motorCon.write(NO_RES)
        time.sleep(5)
        motorCon.write(SMALL_HILL)
        time.sleep(8)
        motorCon.write(BIG_HILL)
        time.sleep(5)
        motorCon.write(NO_RES)
        time.sleep(9)
    motorCon.write(NOMINAL)
    print("Race complete!")
    time.sleep(10)

def main():
    print("Thank you for using the Mario Kart Exercise Bike!")
    mk_stadium()
    water_park()
    ss_canyon()
    thwomp_ruins()
    print("Mushroom Cup Complete!")

if __name__ == "__main__":
    main()