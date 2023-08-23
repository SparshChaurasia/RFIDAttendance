#include <SPI.h>
#include <MFRC522.h>

 
#define SS_PIN 10
#define RST_PIN 9


MFRC522 mfrc522(SS_PIN, RST_PIN);  // Instance of the RFID sensor 


void setup() 
{
  // Begin serial connection to the computer
  Serial.begin(9600);  
  SPI.begin();      
  mfrc522.PCD_Init();   
}

void loop() 
{
  // Check it new card is detected
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  
  String uid = get_UID();

  Serial.print(uid);
  delay(1800);
}

String get_UID() {
  String content = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();

  return content;
}

