#include <SoftwareSerial.h>

int j = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  
}

void loop() {
  // put your main code here, to run repeatedly:

  int i;

  while(j<10)
  {
    for (i=0; i<48; i++)
    {
      Serial.print(random(100));
      Serial.print(" ");
      
    }
  
    Serial.println("");
  j++;
  }

}
