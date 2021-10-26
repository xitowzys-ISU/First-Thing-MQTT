void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop() {
  int signal0 = analogRead(A0);

  int strength0 = signal0;
  Serial.println(strength0);
  analogWrite(9, strength0);
  delay(200);
}