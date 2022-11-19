import json
import wiotp.sdk.device
import time
import random
myConfig = {
 "identity": {
 "orgId": "yu1n93",
 "typeId": "Module",
 "deviceId": "55555"
 },
 "auth": {
 "token": "5555555555"
 }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
for i in range(0,20):
 tablet=["Paracetamol","Aspirine","Dolo 650","Insulin","Vicks"]
 medicinetime=[12.00,1.00,2.00,3.00,5.00,18.00,20.00,7.00]
 name = "Madhu"
 medicine=random.choice(tablet)
 medicinetime=random.choice(medicinetime)
 mydata = {'Patient Name': name, 'Medicine Name': medicine, 'Time': medicinetime}
 client.publishEvent("MEDICINE REMINDER", "json", data=mydata, qos=0, onPublish=None)
 print("Data published to IBM IOT platform :", mydata)
 time.sleep(5)
client.disconnect() 
