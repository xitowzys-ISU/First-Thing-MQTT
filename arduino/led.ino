void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop() {
  while (Serial.available() > 0) {
    uint8_t bright = Serial.read();
    analogWrite(9, bright);
  }
}