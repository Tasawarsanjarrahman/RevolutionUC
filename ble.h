#ifndef BLE_H
#define BLE_H

void bleInit();
void bleSendStatus(String status);

extern bool deviceConnected;
extern bool systemEnabled;

#endif