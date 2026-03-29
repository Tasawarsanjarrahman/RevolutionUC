# Happy Granny

## Overview
This project is a hardware-based pill dispensing system built with an ESP32-S3 microcontroller. The system integrates Bluetooth communication, servo motors, and a DC motor to automate pill dispensing after scanning through a mobile application.
It is specifically designed for elderly users to support safer and more reliable daily medication management.

Original concept preserved:
- Scan pill using mobile app
- Send data via Bluetooth (BLE)
- ESP32 processes command
- Servo positions dispensing arm
- Motor moves pill into output

---

## System Architecture
`Mobile App -> BLE -> ESP32 -> Servo Control -> Motor Driver -> Pill Dispensing`

---

## Components (Bill of Materials)

### Core Components
- ESP32-S3
- TT DC Geared Motor
- L298N Motor Driver
- 2x SG90 Servo Motors

### Additional Required Components
- Jumper wires (male-to-male, male-to-female)
- Breadboard or PCB
- External power supply (recommended: 7V-12V for motor driver)
- 5V regulated supply for ESP32 and servos
- USB cable for programming ESP32

---

## Pin Mapping (Current Firmware + Expansion Example)

| Component | ESP32 Pin | Status |
| --- | --- | --- |
| Servo 1 (active in firmware) | GPIO 10 | Used in current code |
| Motor IN1 | GPIO 5 | Used in current code |
| Motor IN2 | GPIO 4 | Used in current code |
| ENA (PWM, optional speed control) | GPIO 9 | Optional wiring |

NOTE: Verify pins with your actual hardware and firmware before final wiring.

---

## Wiring Overview

### Motor Driver (L298N)
- IN1 -> ESP32 GPIO 5
- IN2 -> ESP32 GPIO 4
- Motor terminals -> DC Motor
- VCC -> External power supply (for example 9V)
- GND -> Common ground with ESP32

### Servos (SG90)
- Servo 1 signal -> GPIO 10
- VCC -> 5V
- GND -> Common ground

### ESP32 Power
- Powered via USB or regulated 5V input

IMPORTANT: All grounds must be connected together.

---

## Power Considerations
- Do not power motors directly from ESP32.
- Use external supply for motor driver.
- Servos may require a stable 5V supply.
- Ensure common ground between all components.

---

## Firmware Setup

### Requirements
- Arduino IDE
- ESP32 board package installed

### Required Libraries (typical)
- BLE library
- Servo library (`ESP32Servo`)

### Steps
1. Open `ESP32_Motor/ESP32_Motor.ino`.
2. Select board: ESP32-S3.
3. Install required libraries.
4. Connect ESP32 via USB.
5. Upload code.

---

## Firmware Structure
- `ESP32_Motor/ESP32_Motor.ino` -> Main entry point
- `ESP32_Motor/ble.cpp` -> BLE communication handling
- `ESP32_Motor/servo.cpp` -> Servo positioning control
- `ESP32_Motor/motor.cpp` -> DC motor control

---

## Operation Flow
1. User scans pill via mobile app.
2. App sends command via BLE.
3. ESP32 receives signal.
4. Servo aligns the correct compartment.
5. Motor activates to dispense pill.
6. System resets and waits for the next command.

---

## Working Principle

### Step 1: Scanner
The user uses a mobile application with camera and machine learning to scan and classify pills. The system identifies each pill individually.

### Step 2: Scheduling and Classification
After scanning, the application allows the user to schedule which day of the week to take the pills and completes the classification process.

### Step 3: Data Transmission
The application sends the classified data to the ESP32-S3 microcontroller via Bluetooth.

### Step 4: Arm Positioning
The ESP32-S3 rotates the servo arm to the correct box position corresponding to the scheduled day.

### Step 5: Pill Transport
After arm positioning, the motor runs to transport the pill to the designated compartment.

---

## Process Summary
The Smart Pill Dispenser follows this workflow: **Scanner -> Schedule -> Transmit -> Position Arm -> Transport Pill**.

---

## Calibration Guide

### Servo Calibration
Adjust servo angles in code for:
- Closed/home position
- Open/dispense position

### Motor Timing
Tune delay values to control:
- Dispense duration
- Over-rotation prevention

### Alignment
Ensure servo positions align with physical compartments accurately.

---

## Use Case
Designed for elderly individuals who need assistance managing daily medication. The system minimizes human error and simplifies medication organization.

---

## Future Improvements
- Voice assistant integration
- Reminder notifications
- IoT cloud synchronization
- Health monitoring integration
