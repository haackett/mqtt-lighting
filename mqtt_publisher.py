import paho.mqtt.client as mqtt
import sys
import json
import os
import time
from api import Api

BROKER = "127.0.0.1"

greenJson = {"type":"set",
            "r":0,
            "g":255,
            "b":0}

redJson = {"type":"set",
            "r":255,
            "g":0,
            "b":0}


client = mqtt.Client(os.environ["COMPUTERNAME"])

if client.connect(BROKER, 1883, 60) != 0:
    print("Could not connect to MQTT broker")
    sys.exit(-1)


api = Api()

client.loop_start()
while True:
    dir = api.callApi()    
    if dir == 1:
        print("turning the lights green")
        client.publish("house/leds", json.dumps(greenJson))
    if dir == -1:
        print("turning the lights red")
        client.publish("house/leds", json.dumps(redJson))
    time.sleep(10)

client.loop_end()
client.disconnect()





