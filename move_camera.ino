#include <Wire.h>

#define SLAVE_ADDRESS 0x04
#define DIR1_PIN 2
#define STEP1_PIN 3
#define DIR2_PIN 4
#define STEP2_PIN 5
#define DIR3_PIN 6
#define STEP3_PIN 7

int state = 0;
int flr,slt;
char fr;

int sleep = 1;
int wait = 1000;
int numstep_x = 3300 ;
int numstep_z ;
int numstep_plate = 90;
int microstep = 1200;

char ch;
int i,j;


void z_slot(char ch);


void setup(){
    pinMode(DIR1_PIN, OUTPUT);
    pinMode(STEP1_PIN, OUTPUT);
    pinMode(DIR2_PIN, OUTPUT);
    pinMode(STEP2_PIN, OUTPUT);
    pinMode(DIR3_PIN, OUTPUT);
    pinMode(STEP3_PIN, OUTPUT);

    Serial.begin(9600);
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(receiveData);

}

void loop(){
   delay(100);
}

void plateround(int rnd){
        digitalWrite(DIR3_PIN,HIGH);
        for(int i=0;i<numstep_plate;i++){
           digitalWrite(STEP3_PIN,LOW);
           delay(sleep);
           digitalWrite(STEP3_PIN,HIGH);
           delay(sleep);
       }

}

void move_cam(){

      plateround(numstep_plate);
      delay(wait);
}



void receiveData(int byteCount) {
    fr = Wire.read();

   Serial.print("Move Camera");
   Serial.print("\n");

   if(flr == 1){
    move_cam();
   }

}

void sendData() {
  Wire.write(fr);
}
