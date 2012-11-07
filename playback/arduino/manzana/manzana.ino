#include <SimpleMessageSystem.h>

#include <CapacitiveSensor.h>
 
#define THRESHOLD 0
#define NO_OF_MANZANAS 4
#define MANZANAS_FOR_GOD_MODE 3

/*
 * CapitiveSense Library Demo Sketch
 * Paul Badger 2008
 * Uses a high value resistor e.g. 10M between send pin and receive pin
 * Resistor effects sensitivity, experiment with values, 50K - 50M. Larger resistor values yield larger sensor values.
 * Receive pin is the sensor pin - try different amounts of foil/metal on this pin
 */


CapacitiveSensor   cs_4_2 = CapacitiveSensor(4,2);        // 10M resistor between pins 4 & 2, pin 2 is sensor pin, add a wire and or foil if desired
CapacitiveSensor   cs_4_6 = CapacitiveSensor(4,6);        // 10M resistor between pins 4 & 6, pin 6 is sensor pin, add a wire and or foil
CapacitiveSensor   cs_4_8 = CapacitiveSensor(4,8);        // 10M resistor between pins 4 & 8, pin 8 is sensor pin, add a wire and or foil
CapacitiveSensor   cs_4_10 = CapacitiveSensor(4,10); 

int timming;
int Manzana[NO_OF_MANZANAS-1];
int OldManzana[NO_OF_MANZANAS-1];
void setup()                    
{
timming = 170;

  Serial.begin(9600);
   cs_4_8.set_CS_Timeout_Millis(timming); /////////////hack
   cs_4_6.set_CS_Timeout_Millis(timming); /////////////hack 
   cs_4_2.set_CS_Timeout_Millis(timming); /////////////hack 
   cs_4_10.set_CS_Timeout_Millis(timming);
   cs_4_8.set_CS_AutocaL_Millis(0x000000FF);     // turn off autocalibrate on channel 1 - just as an example
   InitManzanas();


}

void InitManzanas(void)
{int i;
  for (i=0;i<NO_OF_MANZANAS;i++)
    Manzana[i]=0;
    OldManzana[i]=0;
}

void UpdateManzana(int ManzanaId, long total)
{
  if (total < THRESHOLD)
    Manzana[ManzanaId] = 1;
  else 
    Manzana[ManzanaId] = 0;
}

int NoOfTouchedManzanas(void)
{int i, count;
    count = 0;
    for (i=0;i<NO_OF_MANZANAS;i++)
      if (Manzana[i]== 1)
        count++;
  
  return count;
}

void SendManzanaEvent(void)
{int i;
  if (NoOfTouchedManzanas() >= MANZANAS_FOR_GOD_MODE)
    Serial.write("X"); /* send the character for GOD MODE*/
  else
    /* Send the events for the active manzanas*/
    for(i=0;i<NO_OF_MANZANAS;i++)
      if (Manzana[i]== 1)
        Serial.write(65+i); /*65 is the ASCII code for A*/
}

int NoOfTouchedManzanasOnStateChange(void)
{int i, count;
    count = 0;
    for (i=0;i<NO_OF_MANZANAS;i++)
      if ((Manzana[i]== 1)&&(OldManzana[i]==0))
        count++;
  
  return count;
  
}
void SendManzanaEventOnStateChange(void)
{int i;
  if (NoOfTouchedManzanasOnStateChange() >= MANZANAS_FOR_GOD_MODE)
    Serial.write("X"); /* send the character for GOD MODE*/
  else
    /* Send the events for the active manzanas*/
    for(i=0;i<NO_OF_MANZANAS;i++)
      if ((Manzana[i]== 1)&&(OldManzana[i]==0))
        Serial.write(65+i); /*65 is the ASCII code for A*/
 
  /* update the OldManzanas buffer */
  for(i=0;i<NO_OF_MANZANAS;i++)
    OldManzana[i]=Manzana[i];
}

void loop()                    
{   

    
    /* Update the totals */
    long total0 =  cs_4_2.capacitiveSensor(30);
    long total1 =  cs_4_6.capacitiveSensor(30);
    long total2 =  cs_4_8.capacitiveSensor(30);
    long total3 =  cs_4_10.capacitiveSensor(30);
  
    /*update the manzanas*/
    UpdateManzana(0,total0);
    UpdateManzana(1,total1);
    UpdateManzana(2,total2);
    UpdateManzana(3,total3);
     
    /* send the manzana event on the serial port */
    SendManzanaEvent();
    //SendManzanaEventOnStateChange();
    Serial.write(10);
    Serial.write(13);

delay(10);                             // arbitrary delay to limit data to serial port 
}
