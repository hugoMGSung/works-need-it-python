int redPin = 11;
int greenPin = 12;
int bluePin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) {
    char inChar = Serial.read();
    if (inChar == '1') {
      Serial.print(inChar);
      setColor(0, 255, 0); // green
    } else if (inChar == '2') {
      Serial.print(inChar);
      setColor(255, 0, 0); // red
    }
    else {
      setColor(0, 0, 0); // off
    }
  }
}

void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue); 
}
