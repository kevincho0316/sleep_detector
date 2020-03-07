
String sig;
char Ard1[5]={0};
char Ard2[5]={0};
char check[1];
int value_1=0;
int value_2=0;

void setup()
{
  Serial.begin(9600);
  pinMode(13,OUTPUT); // LED 연결
}

void loop()
{ 
  /* 문자열로 저장*/
  while(Serial.available()) 
   {
     char wait = Serial.read();
     sig.concat(wait);
   } 
  
    /* 입력 문자열 슬라이싱 */
    sig.substring(0,1).toCharArray(check,2);

    if(check[0] == 'Q')
      {
      if (sig.length()==9)
        {
          sig.substring(1,5).toCharArray(Ard1,5);
          sig.substring(5,9).toCharArray(Ard2,5);
          value_1 = atoi(Ard1);
          value_2 = atoi(Ard2);
          sig = "";
        }
       else if (sig.length()>9)
        {sig = "";}
       }
     else if (check[0] != 'Q')
      {sig = "";}

     /* 수신 확인*/ 
      //x.write(value_1);
     // y.write(value_2);
      if (value_1 == 12){
        digitalWrite(13,HIGH);
        }
}
