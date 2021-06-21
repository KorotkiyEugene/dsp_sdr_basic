const byte adcPin = 0;                // A0

const int MAX_RESULTS = 400;

volatile int results [MAX_RESULTS][2];
volatile int active_buffer;
volatile int finish_buffer;
volatile int resultNumber;

// ADC complete ISR
ISR (ADC_vect)
{
    results [resultNumber++][active_buffer] = ADC;

    if (resultNumber >= MAX_RESULTS)
    {
        resultNumber = 0;
        active_buffer = active_buffer ? 0 : 1;
        finish_buffer = 1;
    }
    
}  // end of ADC_vect
  
EMPTY_INTERRUPT (TIMER1_COMPB_vect);
 
void setup ()
{
    Serial.begin(115200); // set baudrate
    while (!Serial) {;}

    active_buffer = 0;
    finish_buffer = 0;
    resultNumber = 0;
  
    // reset Timer 1
    TCCR1A  = 0;
    TCCR1B  = 0;
    TCNT1   = 0;
    TCCR1B  = bit (CS11) | bit (WGM12);  // CTC, prescaler of 8
    TIMSK1  = bit (OCIE1B); 
    OCR1A   = 319;    
    OCR1B   = 319; // 160 uS period - sampling frequency 6.25 kHz

    ADCSRA  =  bit (ADEN) | bit (ADIE) | bit (ADIF); // turn ADC on, want interrupt on completion
    ADCSRA |= bit (ADPS2);  // Prescaler of 16
    //  ADCSRA |= (1 << ADPS1) | (1 << ADPS0);    // 8 prescaler for 153.8 KHz
    ADMUX   = bit (REFS0) | (adcPin & 7);
    ADCSRB  = bit (ADTS0) | bit (ADTS2);  // Timer/Counter1 Compare Match B
    ADCSRA |= bit (ADATE);   // turn on automatic triggering
}

void loop () 
{ 
    while (!finish_buffer) { }
    
    for (int i = 0; i < MAX_RESULTS; i++)
    {
        Serial.println (results [i][1-active_buffer]);
    }

    finish_buffer = 0;
}
