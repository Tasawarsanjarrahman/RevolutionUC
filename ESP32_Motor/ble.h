#ifndef BLE_H
#define BLE_H

class String;

void bleInit();
void bleSendStatus(const String& status);
extern bool deviceConnected;
extern bool systemEnabled;

#endif