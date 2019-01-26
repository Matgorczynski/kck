// na podstawie: zał. 1. http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/Temp/TMP35_36_37.pdf
// Rezystor ustawiony na 100 kOhm
int fotokomorka = 0;  
int pomiarswiatla; 
const int temp = 1;
 
float pobierzNapiecie(int pin){
  return (analogRead(1) * 0.004882814); //formuła zmienia wartości 0-1023 na 0.0-0.5V, które są realnymi wartościami potencjału 
} 

void setup(void) {
  Serial.begin(9600);   
}
 
void loop(void) {
  pomiarswiatla = analogRead(fotokomorka);  //przypisanie wartosci z wejscia analogowego 0 do zmiennej
  Serial.print(pomiarswiatla); //wyswietlenie pomiaru
  Serial.print(" lx; "); // jednostka SI
  
  float napiecie, tempC; // zmienne o wartosciach liczb rzeczywistych
  napiecie = pobierzNapiecie(temp); //przypisanie wartosci funkcji
  tempC = (napiecie - 0.5)*100.0; // na podstawie załącznika 1, wykresu (fig.6.) na s. 5 
  Serial.print(tempC);
  Serial.print(" C; ");
  
  if (pomiarswiatla < 100) {
    Serial.println(" Jest ciemno.");
  } 
  	else {
    Serial.println(" Jest jasno.");
  } 
  if(tempC > 10){
    Serial.println("Jest wiecej niz 10 stopni C");
  }
    else{
    Serial.println("Jest mniej niz 10 stopni C.");
  }
  

  delay(2000);
}