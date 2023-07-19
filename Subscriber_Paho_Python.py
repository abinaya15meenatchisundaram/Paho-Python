
#                                SUBSCRIBER CODE                                

import paho.mqtt.client as mqttclient
import time


def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected=True
        client.subscribe("Testing")
        client.on_message=on_message
    else:
        print("Client is not connected")

def on_message(client,userdata,message):
    print("Message received")
    print("Message received" +":"+ str(message.payload.decode("utf-8")))
    print("Topic"+":"+ str(message.topic))

              
connected =False
messagereceived=False

brokerAddress="localhost"
port=1883
user="root"
password="root"

client=mqttclient.Client()
client.username_pw_set(user,password=password)
client.on_connect=on_connect

client.connect(brokerAddress,port,60)

client.loop_start()
client.subscribe("Testing")
while connected!=True:
    time.sleep(0.2)
while messagereceived!=True:
    time.sleep(0.2)
client.loop_stop()

