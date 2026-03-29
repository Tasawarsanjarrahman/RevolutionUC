#include "servo.h"
#include <ESP32Servo.h>

#define SERVO_PIN   10

Servo myServo;

void servoInit() {
  myServo.attach(SERVO_PIN);
  myServo.write(0);
}

void servoSetAngle(int angle) {
  angle = constrain(angle, 0, 180);
  myServo.write(angle);
}