// Analog pins
const int analogPin0 = A0,analogPin1 = A1;
// Analog values
int analogValue0,analogValue1;

unsigned long lastTime,sampleTime;

void setup() {
  
  Serial.begin(9600);
  
  // Initial analog values
  analogValue0 = 0;
  analogValue1 = 0;

  // Communication sample time 
  sampleTime = 40;
  lastTime = millis();
  
}

void loop() {

 // Execute each sample time
 if (millis()-lastTime >= sampleTime)
 {
  lastTime=millis();
  analogValue0 = analogRead(analogPin0);
  analogValue1 = analogRead(analogPin1);
  
  // Add necessary data
  Serial.println(scaling(analogValue0,0,1023,0,5));
  Serial.println(scaling(analogValue1,0,1023,-50,50));
 }

}

float scaling(float x, float in_min, float in_max, float out_min, float out_max) 
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
