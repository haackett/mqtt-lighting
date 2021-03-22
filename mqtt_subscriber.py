import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import json
from pi_led_controller import PiLedController


BROKER = "127.0.0.1"

### MQTT CLIENT METHODS ###
def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK")
    else:
        print("Bad connection. Returned code: ", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected. Result code: ", rc)

def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    m_in = json.loads(m_decode)
    print(m_in)
    if (m_in["type"] == "set"):
        setLeds(ledController, m_in)

def disconnect(client):
    client.loop_stop()
    client.disconnect()



### HELPER METHODS ###
def setLeds(ledController : PiLedController, m_in):
    ledController.setPin(ledController.redPin, int(m_in["r"]))
    ledController.setPin(ledController.greenPin, int(m_in["g"]))
    ledController.setPin(ledController.bluePin, int(m_in["b"]))



client = mqtt.Client("pi")
client.on_connect= on_connect
client.on_log= on_log
client.on_disconnect= on_disconnect
client.on_message= on_message

ledController = PiLedController()

print("Connecting to broker", BROKER)
client.connect(BROKER, 1883, 60)
client.subscribe("house/leds")
while True:
    client.loop()


