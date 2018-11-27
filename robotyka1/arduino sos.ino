void setup()
{
  pinMode(13, OUTPUT);
}

void loop(){
  for (int i = 0; i < 3; i = i + 1){
    digitalWrite(13, HIGH);
    delay(300);
    digitalWrite(13, LOW);
    delay(300);
  }
  for (int x = 0; x < 3; x = x + 1){
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
  }
  for (int d = 0; d < 3; d = d + 1){
    digitalWrite(13, HIGH);
    delay(300);
    digitalWrite(13, LOW);
    delay(300);
  }
  delay(3000);
}
