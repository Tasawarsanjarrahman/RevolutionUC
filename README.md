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

### Step 1: Pill Recognition
The user uses a mobile application equipped with a camera and integrated machine learning model to scan pills. The system identifies each pill individually (one pill at a time).

### Step 2: Classification
The mobile application classifies pills according to a predefined schedule (e.g., days of the week).

### Step 3: Data Transmission
After recognition, the mobile device sends the pill classification data to the ESP32-S3 via Bluetooth.

### Step 4: System Activation
Upon receiving the data:
- The ESP32-S3 activates the conveyor system via the L298N motor driver  
- Controls the timing and movement of the SG90 servo-driven arms  

### Step 5: Dispensing Process
- The user places pills onto the conveyor belt  
- The conveyor transports pills to sorting positions  
- Based on received data, the ESP32-S3 selects the correct servo arm  
- Each SG90 servo rotates to a specific angle  
- Pills slide along the arm and fall into the correct compartment  

### Step 6: Storage
Pills are sorted into designated compartments corresponding to the scheduled days.

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
