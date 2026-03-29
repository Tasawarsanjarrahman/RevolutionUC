#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#define L298N_IN1   5
#define L298N_IN2   4

#define SERVICE_UUID      "12345678-1234-1234-1234-123456789abc"
#define CHAR_WRITE_UUID   "12345678-1234-1234-1234-123456789abd"
#define CHAR_NOTIFY_UUID  "12345678-1234-1234-1234-123456789abe"

BLEServer*         pServer       = nullptr;
BLECharacteristic* pNotify       = nullptr;
bool deviceConnected             = false;
bool systemEnabled               = false;
unsigned long lastNotify         = 0;

// ---- HÀM MOTOR ----
void motorForward() {
  digitalWrite(L298N_IN1, HIGH);
  digitalWrite(L298N_IN2, LOW);
}

void motorStop() {
  digitalWrite(L298N_IN1, LOW);
  digitalWrite(L298N_IN2, LOW);
}

class ServerCallbacks : public BLEServerCallbacks {
  void onConnect(BLEServer* pServer) {
    deviceConnected = true;
    Serial.println("[BLE] Điện thoại đã kết nối!");
  }
  void onDisconnect(BLEServer* pServer) {
    deviceConnected = false;
    systemEnabled   = false;
    motorStop();
    Serial.println("[BLE] Mất kết nối → Tắt hệ thống");
    BLEDevice::startAdvertising();
  }
};

class WriteCallbacks : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* pChar) {
    String cmd = pChar->getValue().c_str();
    cmd.trim();

    Serial.print("[BLE] Lệnh: ");
    Serial.println(cmd);

    if (cmd == "ON") {
      systemEnabled = true;
      motorForward();
      Serial.println("[HỆ THỐNG] BẬT → Motor chạy");
    }
    else if (cmd == "OFF") {
      systemEnabled = false;
      motorStop();
      Serial.println("[HỆ THỐNG] TẮT → Motor dừng");
    }
    else {
      Serial.println("[BLE] Lệnh không hợp lệ");
    }
  }
};

void setup() {
  Serial.begin(115200);
  Serial.println("\n=== KHỞI ĐỘNG ===");

  // -- L298N --
  pinMode(L298N_IN1, OUTPUT);
  pinMode(L298N_IN2, OUTPUT);
  motorStop();
  Serial.println("[OK] L298N sẵn sàng");

  // -- BLE --
  BLEDevice::init("ESP32_Motor");
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
  Serial.println("[OK] BLE: ESP32_Motor");
}