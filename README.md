# Happy Granny
## Overview
The Smart Pill Dispenser is an automated medication management device designed specifically for elderly users. It helps organize, classify, and distribute pills accurately according to a predefined schedule, reducing the risk of missed or incorrect medication intake.

---

## Product Type
**Smart Medication Dispensing Device for Elderly**

---

## Product Description
The system consists of a conveyor mechanism powered by a TT DC geared motor and controlled by an ESP32-S3 microcontroller. Mechanical arms (pushers), driven by SG90 servo motors, are used to direct pills into designated compartments.

- Microcontroller: ESP32-S3  
- Actuation System: TT DC gear motor + L298N motor driver  
- Sorting Mechanism: 2 arms powered by SG90 servos  
- Connectivity: Bluetooth communication with a mobile device  

---

## Electronic Components
- 1 × TT DC Gear Motor  
- 1 × L298N Motor Driver  
- 1 × ESP32-S3  
- 2 × SG90 Servo Motors  

---

## Key Features
- Automated pill sorting based on schedule  
- Machine learning-based pill recognition via mobile camera  
- Bluetooth communication between mobile device and hardware  
- Precise control using SG90 servo motors for accurate dispensing  
- Weekly medication organization (by days of the week)  
- Designed for ease of use by elderly users  

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
The Smart Pill Dispenser follows a streamlined workflow: **Scanner → Schedule → Transmit → Position Arm → Transport Pill**. Users first scan pills using the mobile application, then schedule them for specific days of the week. The classified data is sent to the ESP32-S3, which first positions the servo arm at the correct compartment, followed by motor activation to transport the pill to its designated location.

---

## System Architecture
- Mobile Application
  - Camera input + Machine Learning model  
  - User interface for scheduling  
  - Bluetooth communication  

- Embedded System (ESP32-S3)
  - Receives classification data  
  - Controls TT motor via L298N driver  
  - Controls SG90 servos  
  - Executes dispensing logic  

- Mechanical System
  - Conveyor belt  
  - TT DC gear motor  
  - Servo-driven arms  
  - Compartment tray  

---

## Use Case
Designed for elderly individuals who need assistance managing daily medication. The system minimizes human error and simplifies the process of organizing pills.

---

## Future Improvements
- Voice assistant integration  
- Reminder notifications  
- IoT cloud synchronization  
- Health monitoring integration  
