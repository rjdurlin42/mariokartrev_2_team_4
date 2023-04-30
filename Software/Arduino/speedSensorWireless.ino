#include <ArduinoBLE.h>
#include <Serial.h>
#include <ArduinoBLE.h>

BLEService speedService("a123f5cd-58ee-49e5-ad0e-976cb1035500");
BLEFloatCharacteristic speedCharacter("a123f5cd-58ee-49e5-ad0e-976cb1035501", BLERead | BLEWrite);

float time1ms, time2ms, time1s, time2s, timeDiff, revSpeed = 0;
int counter = 0;
bool applyTime1 = 1;
bool applyTime2,data = 0;



void setup() {
  Serial.begin(9600); //allows communication to computer
  Serial1.begin(9600); //enable uart
  pinMode(2,INPUT); //output from tach
  pinMode(7,OUTPUT); //gate connection to mosfet
  digitalWrite(7,HIGH);
  BLE.begin();
  BLE.setAdvertisedService(speedService);
  speedService.addCharacteristic(speedCharacter);
  BLE.addService(speedService);
  BLE.setLocalName("SpeedSensor");
  BLE.setDeviceName("SpeedSensor");
  BLE.advertise();
}

void loop() {
    BLEDevice central = BLE.central();
    if(central) {
      if(!digitalRead(2) && applyTime1) {
        time1ms = millis();
        applyTime1 = 0;
        applyTime2 = 1;
        while(!digitalRead(2)){
        }
      }
      else if(!digitalRead(2) && applyTime2) {
        time2ms = millis();
        applyTime2 = 0;
        applyTime1 = 1;
        time1s = time1ms / 1000;
        time2s = time2ms / 1000;
        timeDiff = time2s - time1s;  //time (seconds) between two tape hits
        revSpeed = 20 * timeDiff; //time (seconds) for one wheel revolution at current moment
        if (revSpeed > 0.18 && revSpeed < 20) {  //accounts for debouncing issues
          Serial.print("Time for one revolution:");
          Serial.println(revSpeed);
          speedCharacter.writeValue(revSpeed);
        }
      }
    }
}
