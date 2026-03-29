#include "ble.h"
#include "motor.h"
#include "servo.h"

unsigned long lastNotify = 0;

// setup() function: Initializes the system by setting up serial communication,
// initializing motor, servo, and BLE modules, and printing status messages.
// This function runs once at the start of the program.
void setup() {
  Serial.begin(115200);
  Serial.println("\n=== INITIALIZING ===");

  motorInit();
  servoInit();
  bleInit();

  Serial.println("=== READY ===\n");
}

// loop() function: Main program loop that runs repeatedly.
// It checks every second if the system status has changed and sends
// a BLE notification with the current system state (ON or OFF).
void loop() {
  if (millis() - lastNotify > 1000) {
    lastNotify = millis();
    String status = "SYS:"  + String(systemEnabled  ? "ON"  : "OFF");
    bleSendStatus(status);
  }
}