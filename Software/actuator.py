import serial

#Initialize (open port)
actuatorControl = serial.Serial('/dev/rfcomm0',9600,timeout=0.01)

#Transmit datem
actuatorControl.write(b'500') #Substitute EXTENSION_LENGTH for the variable holding the actuator extension length