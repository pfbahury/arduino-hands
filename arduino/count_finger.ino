#define pin0 2
#define pin1 3
#define pin2 4
#define pin3 5
#define pin4 6

char pythonSignal;

void setup(){
  Serial.begin(9600);
  pinMode(pin0, OUTPUT);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);
}

void loop(){
  pythonSignal = Serial.read();

  switch (pythonSignal) {
    case '1' : //caso 1 dedo levantado
      
      digitalWrite(pin0, HIGH);
      digitalWrite(pin1, LOW);
      digitalWrite(pin2, LOW);
      digitalWrite(pin3, LOW);
      digitalWrite(pin4, LOW);
      break;

    case '2':
      digitalWrite(pin0, HIGH);
      digitalWrite(pin1, HIGH);
      digitalWrite(pin2, LOW);
      digitalWrite(pin3, LOW);
      digitalWrite(pin4, LOW);
      break;

    case '3':
      digitalWrite(pin0, HIGH);
      digitalWrite(pin1, HIGH);
      digitalWrite(pin2, HIGH);
      digitalWrite(pin3, LOW);
      digitalWrite(pin4, LOW);
      break;

    case '4':
      digitalWrite(pin0, HIGH);
      digitalWrite(pin1, HIGH);
      digitalWrite(pin2, HIGH);
      digitalWrite(pin3, HIGH);
      digitalWrite(pin4, LOW);
      break;

    case '5':
      digitalWrite(pin0, HIGH);
      digitalWrite(pin1, HIGH);
      digitalWrite(pin2, HIGH);
      digitalWrite(pin3, HIGH);
      digitalWrite(pin4, HIGH);
      break;

    case '0':
      digitalWrite(pin0, LOW);
      digitalWrite(pin1, LOW);
      digitalWrite(pin2, LOW);
      digitalWrite(pin3, LOW);
      digitalWrite(pin4, LOW);
      break;
    
  }

}

void turnOffLeds() {
    digitalWrite(pin0, LOW);
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
    digitalWrite(pin3, LOW);
    digitalWrite(pin4, LOW);
}