
#                              PUBLISHER CODE                                     

from paho.mqtt import client as mqtt
import time

#clientId = "MQTT"
port= 1883
broker = "localhost"

client= mqtt.Client()
client.connect(broker,port,60)

message=input("Enter the message to be send:")
if client.publish("Testing",message):
    print("The message is published successfully")

time.sleep(10)

client.loop_forever()
