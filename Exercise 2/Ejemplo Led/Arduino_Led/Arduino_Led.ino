//Declaracion de salidas digitales D2 y D3
int led1 = 13;//2
int led2 = 3;
//Variable que recive el dato enviado en Python
int option;

void Bucle()
{
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    option = Serial.read();
    Serial.println(option);
    if(option == 'P'){
      digitalWrite(led1,HIGH);
      digitalWrite(led2,LOW);
    }
    if(option == 'N'){
      digitalWrite(led1,LOW);
      digitalWrite(led2,HIGH);
    }
    if(option == 'D'){
      digitalWrite(led1,LOW);
      digitalWrite(led2,LOW);
      
      }
   }
  
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  digitalWrite(led1,LOW);
  digitalWrite(led2,LOW);

}

void loop() {
  Bucle();
}
