#include <DHTesp.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <BLE2902.h>

#define SERVICE_UUID        "d47e7069-ca9a-47e2-8c94-b85a87190927"
#define CHARACTERISTIC_UUID "47de1cee-d731-4fea-a7ba-b8742d734992"

BLECharacteristic *pCharacteristic;

DHTesp dht;

int dhtPin = 13;
int val = 0;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

  Serial.println("Mulai sensing");
  dht.setup(dhtPin, DHTesp::DHT11);
  
  Serial.println("Mulai server");
  BLEDevice::init("Notify Temp");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  pCharacteristic = pService->createCharacteristic(
                                        CHARACTERISTIC_UUID, 
                                        BLECharacteristic::PROPERTY_READ |
                                        BLECharacteristic::PROPERTY_WRITE |
                                        BLECharacteristic::PROPERTY_NOTIFY);
  pCharacteristic->addDescriptor(new BLE2902());

  pService->start();
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(true);
  pAdvertising->setMinPreferred(0x12);
  BLEDevice::startAdvertising();
  Serial.println("Server sudah siap!");

}

void loop() {
  // put your main code here, to run repeatedly:

  //float t = dht.getTemperature();
  float t = dht.getTemperature();
  pCharacteristic->setValue((uint8_t*)&val, 4);
  pCharacteristic->notify();
  Serial.print("Value : "); Serial.println(val);
  //Serial.print("Temperature : "); Serial.println(t);

  val++;
  delay(2000);
  

}
