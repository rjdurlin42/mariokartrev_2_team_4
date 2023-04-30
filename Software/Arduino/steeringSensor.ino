#include <Adafruit_ADS1X15.h>
#include <ArduinoBLE.h>

BLEService steeringService("a123f5cd-58ee-49e5-ad0e-976cb10355fe");
BLEUnsignedShortCharacteristic steeringCharacter("a123f5cd-58ee-49e5-ad0e-976cb10355ff", BLERead | BLEWrite);
BLEBooleanCharacteristic leftCharacter("a123f5cd-58ee-49e5-ad0e-976cb1035678", BLERead | BLEWrite);
BLEBooleanCharacteristic rightCharacter("a123f5cd-58ee-49e5-ad0e-976cb1035679", BLERead | BLEWrite);

Adafruit_ADS1015 ADS; //initialize ads
unsigned short steeringData;
bool startTime = 1;
bool startSleeping;
float time1, time2, test1, test2, thereAndBack;


void setup() {
  Serial.begin(19200); //allows communication to computer
  pinMode(7,INPUT_PULLUP);
  pinMode(8,INPUT_PULLUP); 
  pinMode(2,OUTPUT);
  digitalWrite(2,HIGH); //begins powering potentiometer
  BLE.begin();
  BLE.setAdvertisedService(steeringService);
  steeringService.addCharacteristic(steeringCharacter);
  steeringService.addCharacteristic(leftCharacter);
  steeringService.addCharacteristic(rightCharacter);
  BLE.addService(steeringService);
  BLE.setLocalName("SteeringSensor");
  BLE.setDeviceName("SteeringSensor");
  BLE.advertise();
  ADS.setGain(GAIN_TWOTHIRDS);
  if (!ADS.begin()) {
    Serial.println("Failed to initialize ADS.");
    while (1);
  }
}

void loop() {
  BLEDevice central = BLE.central();
  if (startTime == 1) {
    time1 = millis();
    startTime = 0;
  }
  time2 = millis();
  if ((time2 - time1) > 20000) { //if no connection for 20 seconds
    startSleeping = 1;
  } 
  while (startSleeping == 1) { //power saving mode
    delay(3000); //sleep for 3 seconds
    Serial.println("Sleeping");
    central = BLE.central();
    if (central) { //connected
      startSleeping = 0;
    }
  }
  if (central) {
    Serial.println("* Connected to central device!");
    Serial.print("* Device MAC address: ");
    Serial.println(central.address());
    Serial.println(" ");
    while (central.connected()) {
      if(!digitalRead(7)) {           //right handlebar pushed
        leftCharacter.writeValue(1);
        Serial.println("Right");
      }
      else {
        leftCharacter.writeValue(0);
      }
      if(!digitalRead(8)) {       //left handlebar pushed
        rightCharacter.writeValue(1);
        Serial.println("Left");
      }
      else {
        rightCharacter.writeValue(0);
      }
      steeringData = ADS.readADC_SingleEnded(0);
      steeringCharacter.writeValue(steeringData);
    }
    Serial.println("* Disconnected to central device!");
    startTime = 1;
  }
}
