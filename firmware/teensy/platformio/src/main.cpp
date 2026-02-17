#include <Arduino.h>
#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>

// GUItool: begin automatically generated code
AudioInputI2S            i2s1;           //xy=522,444
AudioOutputI2S           i2s2;           //xy=662,443
AudioConnection          patchCord1(i2s1, 0, i2s2, 0);
AudioConnection          patchCord2(i2s1, 1, i2s2, 1);
// GUItool: end automatically generated code

AudioControlSGTL5000   sgtl5000;

void setup() {
  AudioMemory(16);
  Serial.begin(115200);
  sgtl5000.enable();
  sgtl5000.volume(0.5);
  delay(1000);
}

void loop() {
  Serial.print("alive\n");
  delay(1000);
}