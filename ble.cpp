#include "ble.h"
#include "motor.h"
#include "servo.h"
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#define SERVICE_UUID      "12345678-1234-1234-1234-123456789abc"
#define CHAR_WRITE_UUID   "12345678-1234-1234-1234-123456789abd"
#define CHAR_NOTIFY_UUID  "12345678-1234-1234-1234-123456789abe"

BLEServer*         pServer = nullptr;
BLECharacteristic* pNotify = nullptr;
bool deviceConnected        = false;
bool systemEnabled          = false;

class ServerCallbacks : public BLEServerCallbacks {
  void onConnect(BLEServer* pServer) {
    deviceConnected = true;
    Serial.println("[BLE] Connected!");
  }
  void onDisconnect(BLEServer* pServer) {
    deviceConnected = false;
    systemEnabled   = false;
    motorStop();
    BLEDevice::startAdvertising();
    Serial.println("[BLE] Disconnected!");
  }
};

class WriteCallbacks : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* pChar) {
    String cmd = pChar->getValue().c_str();
    cmd.trim();
    Serial.print("[BLE] Command: ");
    Serial.println(cmd);

    // ---- System ----
    if (cmd == "ON") {
      systemEnabled = true;
      Serial.println("[SYS] ON");
    }
    else if (cmd == "OFF") {
      systemEnabled = false;
      motorStop();
      Serial.println("[SYS] OFF");
    }

    // ---- Motor ----
    else if (cmd == "M_F")  motorForward();
    else if (cmd == "M_B")  motorBackward();
    else if (cmd == "M_S")  motorStop();

    // ---- Servo ----
    else if (cmd.startsWith("S:")) {
      int angle = cmd.substring(2).toInt();
      servoSetAngle(angle);
      Serial.print("[SERVO] Angle: ");
      Serial.println(angle);
    }

    else {
      Serial.println("[BLE] Invalid command");
    }
  }
};

void bleInit() {
  BLEDevice::init("ESP32_Device");
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new ServerCallbacks());

  BLEService* pService = pServer->createService(SERVICE_UUID);

  BLECharacteristic* pWrite = pService->createCharacteristic(
    CHAR_WRITE_UUID,
    BLECharacteristic::PROPERTY_WRITE
  );
  pWrite->setCallbacks(new WriteCallbacks());

  pNotify = pService->createCharacteristic(
    CHAR_NOTIFY_UUID,
    BLECharacteristic::PROPERTY_NOTIFY
  );
  pNotify->addDescriptor(new BLE2902());

  pService->start();
  BLEDevice::startAdvertising();
  Serial.println("[OK] BLE: ESP32_Device");
}

void bleSendStatus(String status) {
  if (deviceConnected) {
    pNotify->setValue(status.c_str());
    pNotify->notify();
  }
}