#include <ArduinoBLE.h>
#include <Serial.h>

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
}

void loop() {
    if(!digitalRead(2) && applyTime1) {
      time1ms = millis();
      applyTime1 = 0;
      applyTime2 = 1;
      //Serial.print("Hit one time:");
      //Serial.println(time1ms);
      while(!digitalRead(2)){
        
      }

     // counter = 0;
      /*while(!digitalRead(2) && counter < 10) {
        counter = counter + 1;
        delay(100);
      } //traps until off tape or spent 3 seconds
      if(counter >= 10) { //spent too much time on tape hit 1, speed is zero
        applyTime1 = 1;
        applyTime2 = 0;
        Serial.println("Been stopped on tape 1");
        Serial.print("Time for one revolution:");
        Serial.println(0);
        Serial1.println(0);
        counter = 0;
      }*/

    }
    else if(!digitalRead(2) && applyTime2) {
      
      time2ms = millis();
      applyTime2 = 0;
      applyTime1 = 1;
      //Serial.print("Hit two time:");
      //Serial.println(time2ms);
      time1s = time1ms / 1000;
      time2s = time2ms / 1000;
      timeDiff = time2s - time1s;  //time (seconds) between two tape hits
      revSpeed = 20 * timeDiff; //time (seconds) for one wheel revolution at current moment
      if (revSpeed > 0.18 && revSpeed < 20) {  //accounts for debouncing issues //0.18
        Serial.print("Time for one revolution:");
        Serial.println(revSpeed);
        Serial1.println(revSpeed);
      }

      
      /*counter = 0;
      while(!digitalRead(2) && counter < 10) {
        counter = counter + 1;
        delay(100);
      } //traps until off tape or spent 1 seconds
      if(counter >= 10) { //spent too much time on tape hit 2, speed is zero
        Serial.println("Been stopped for 1 sec");
        Serial.print("Time for one revolution:");
        Serial.println(0);
        Serial1.println(0);
        counter = 0;
      }
    }
    if(counter >= 10 && digitalRead(2)) { //been stopped for 3 seconds
      Serial.println("Been stopped for 1 sec");
      Serial.print("Time for one revolution:");
      Serial.println(0);
      Serial1.println(0);
      counter = 0;
    }*/
}
}
