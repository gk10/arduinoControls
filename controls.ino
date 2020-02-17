int analogPin = A0;
int val = 0;
int tempVal = 0;
int maxRange = 1000;
int minRange =0;
void setup() {

 Serial.begin(9600);


}

void loop() {
  val = analogRead(analogPin);
  Serial.println(val);
  
  if(val > tempVal+2 && val < maxRange){
    Serial.println("FORWARDS"); 
  }
  if(val < tempVal-2 && val > minRange){
    Serial.println("BACKWARDS"); 
  }
  tempVal = val;
  // put your main code here, to run repeatedly:

}

