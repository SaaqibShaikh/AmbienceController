// Arduino IDE: 
// File -> Examples -> 04.Communication -> PhysicalPixel

const int R =9; // pin the LED is attached to
const int G =10;
const int Y =11;
int incomingByte;      // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(Y, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'R') {
      digitalWrite(R,HIGH);
      digitalWrite(G,LOW);
      digitalWrite(Y,LOW);
    } 
      if (incomingByte == 'G') {
      digitalWrite(G,HIGH);
      digitalWrite(R,LOW);
      digitalWrite(Y,LOW);
      }
      if (incomingByte == 'Y') {
      digitalWrite(Y,HIGH);
      digitalWrite(R,LOW);
      digitalWrite(G,LOW);
      }
      if (incomingByte == 'W') {
      digitalWrite(G,LOW);
      digitalWrite(R,LOW);
      digitalWrite(Y,LOW);
      }
      if (incomingByte == 'P') {
      digitalWrite(G,HIGH);
      digitalWrite(R,HIGH);
      digitalWrite(Y,HIGH);
      }
  }
}