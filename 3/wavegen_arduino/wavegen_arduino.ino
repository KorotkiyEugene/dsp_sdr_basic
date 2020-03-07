#include "waveform_table.h"

#define SAMPLES_NUM 256

int i = 0;           // sample number
int sample_time = 1; // sample time in micro seconds

//int sine[SAMPLES_NUM];

void setup() {
    DDRD = 0xFF;
   
    /*float x; 
    float y; 
    for(int i=0;i<SAMPLES_NUM; i++)
     {
          x = (float)i;
          y = sin((x/SAMPLES_NUM)*2*PI);
          sine[i] = int(y*7) + 8;
     }*/
}

void loop() {

    PORTD = sineTable[i];

    i++;

    if(SAMPLES_NUM == i) 
        i = 0;

    delayMicroseconds(sample_time);
}
