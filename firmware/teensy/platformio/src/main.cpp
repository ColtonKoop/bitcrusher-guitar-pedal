#include <Arduino.h>
#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>
#include <Bounce.h>

// GUItool: begin automatically generated code
AudioInputI2S            i2s1;           //xy=449,475
AudioEffectBitcrusher    bitcrusher1;    //xy=587,446
AudioMixer4              mixer1;         //xy=731,488
AudioOutputI2S           i2s2;           //xy=868,494
AudioConnection          patchCord1(i2s1, 0, bitcrusher1, 0);
AudioConnection          patchCord2(i2s1, 1, mixer1, 1);
AudioConnection          patchCord3(bitcrusher1, 0, mixer1, 0);
AudioConnection          patchCord4(mixer1, 0, i2s2, 0);
// GUItool: end automatically generated code

AudioControlSGTL5000   sgtl5000;

// --- pins (adjust as needed) ---
const int POT_PIN = A1;        // Audio shield VOL is often A1; confirm if different
const int BUTTON_PIN = 2;      // any free digital pin
const int LED_PIN = 13;        // built-in LED, or use an external LED pin

Bounce button = Bounce(BUTTON_PIN, 10); // 10 ms debounce

bool bypass = false;           // false = use wet/dry, true = full dry
float mix = 0.5f;              // current wet/dry from the knob
float lastReportedMix = -1.0f; // force initial print
elapsedMillis potTimer;

void setup() {
  AudioMemory(16);
  Serial.begin(115200);
  while (!Serial && millis() < 2000) {
    // allow time for Serial Monitor to connect
  }
  Serial.println("Boot: wet/dry control ready");

  bitcrusher1.bits(4);
  bitcrusher1.sampleRate(4000);

  // init mixer
  mixer1.gain(0, 0.5); // wet
  mixer1.gain(1, 0.5); // dry
  mixer1.gain(2, 0);
  mixer1.gain(3, 0);

  sgtl5000.enable();
  sgtl5000.volume(0.5);
  sgtl5000.lineInLevel(5); // 1.33 Vpp

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH); // effect on by default
}

void loop() {
  button.update();

  // Toggle bypass on button press (active-low)
  if (button.fallingEdge()) {
    bypass = !bypass;
    if (bypass) {
      // full dry
      mixer1.gain(0, 0.0f);
      mixer1.gain(1, 1.0f);
      digitalWrite(LED_PIN, LOW);
      Serial.println("Bypass ON: full dry");
    } else {
      // restore current knob mix
      mixer1.gain(0, mix);
      mixer1.gain(1, 1.0f - mix);
      digitalWrite(LED_PIN, HIGH);
      Serial.print("Bypass OFF: mix=");
      Serial.println(mix, 3);
    }
  }

  // Read pot periodically to reduce noise/jitter
  if (potTimer > 10) {
    potTimer = 0;
    int raw = analogRead(POT_PIN); // 0..1023 on Teensy
    mix = raw / 1023.0f;           // 0..1

    if (!bypass) {
      mixer1.gain(0, mix);           // wet
      mixer1.gain(1, 1.0f - mix);    // dry
    }

    if (abs(mix - lastReportedMix) >= 0.01f) {
      Serial.print("Knob mix=");
      Serial.println(mix, 3);
      lastReportedMix = mix;
    }
  }
}
