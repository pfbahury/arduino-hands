int ledPins[] = {2, 3, 4, 5, 6};
int numLeds = 5;

void setup() {
  // Configurar pinos como saída
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    data.trim()
    
    if (data.length() == numLeds) {
      for (int i = 0; i < numLeds; i++) {
        if (data[i] == '1') {
          digitalWrite(ledPins[i], HIGH);
        } else if (data[i] == '0') {
          digitalWrite(ledPins[i], LOW);
        }
      }
      delay(50);
    }
  }
}
