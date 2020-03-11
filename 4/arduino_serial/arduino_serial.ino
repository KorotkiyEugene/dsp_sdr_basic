
void setup() { 
    Serial.begin(115200);
    while (!Serial) {;}
}

void loop() {
    char line[30];
    if (Serial.available()) {
        Serial.readStringUntil('\n').toCharArray(line,30);
        if (strstr(line,":A0?")==line) {
            Serial.print(".A0 "); Serial.println(analogRead(A0));
        } else if (strstr(line,":A1?")==line) {
            Serial.print(".A1 "); Serial.println(analogRead(A1));
        }
    //delay(3);
   }
}
