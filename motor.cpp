#include "motor.h"
#include "Arduino.h"

#define L298N_IN1   5
#define L298N_IN2   4

void motorInit() {
  pinMode(L298N_IN1, OUTPUT);
  pinMode(L298N_IN2, OUTPUT);
  motorStop();
}

void motorForward() {
  digitalWrite(L298N_IN1, HIGH);
  digitalWrite(L298N_IN2, LOW);
}

void motorBackward() {
  digitalWrite(L298N_IN1, LOW);
  digitalWrite(L298N_IN2, HIGH);
}

void motorStop() {
  digitalWrite(L298N_IN1, LOW);
  digitalWrite(L298N_IN2, LOW);
}