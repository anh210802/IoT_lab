import sys
from Adafruit_IO import MQTTClient
import time
import random

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "anh_iot2108"
AIO_KEY = "aio_qmXK07Iekix6Obfy7AFuUsTsUgeT"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
while True:
    counter = counter - 1
    if counter <= 0 :
        counter = 10
        #TODO
        print("Random data is publising...")
        temp = random.randint(15, 60)
        client.publish("sensor1", temp)
        humi = random.randint(0, 100)
        client.publish("sensor2", humi)
        light = random.randint(0, 500)
        client.publish("sensor3", light)
    time.sleep(1)
    pass