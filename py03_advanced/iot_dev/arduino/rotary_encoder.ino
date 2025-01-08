#define DT 2
#define CLK 3
#define SW 4

void setup() {
  Serial.begin(9600);
  pinMode(DT, INPUT);
  pinMode(CLK, INPUT);
  pinMode(SW, INPUT);
  digitalWrite(SW, HIGH);
}

void loop() {
  int counter;
  byte DialPos;
  byte Last_DialPos;
  
  counter = 0;
  
  while (1) 
  {
    DialPos = (digitalRead(CLK) << 1) | digitalRead(DT);
    if (DialPos == 3 && Last_DialPos == 1) {
      counter--;
    }
    if (DialPos == 3 && Last_DialPos == 2) {
      counter++;
    }
    Serial.println(counter);
    
    if (!digitalRead(SW))
      Serial.println("Switch pressed!!");
     
    Last_DialPos = DialPos;
  }
}