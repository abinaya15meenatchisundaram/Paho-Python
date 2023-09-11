# Paho-Python
[Python](https://www.python.org/) is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python’s design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. 
 
[MQTT](https://www.emqx.io/mqtt) is a kind of lightweight IoT messaging protocol based on the publish/subscribe model, which can provide real-time and reliable messaging service for IoT devices, only using very little code and bandwidth. It is suitable for devices with limited hardware resources and the network environment with limited bandwidth. Therefore, MQTT protocol is widely used in IoT, mobile internet, IoV, electricity power, and other industries.

This article mainly introduces how to use the paho-mqtt client and implement connection, subscribe, messaging, and other functions between the client and MQTT broker, in the Python project.

## Project initialization
This project uses Python 3.6 to develop and test. Readers can use the following command to confirm the Python version. 

```
➜  ~ python3 --version
Python 3.6.7
```
      
### Choose the MQTT client
The Paho Python Client provides a client class with support for both MQTT v3.1 and v3.1.1 on Python 2.7 or 3.x. It also provides some helper functions to make publishing one off messages to an MQTT server very straightforward.

### Using pip to install the Paho MQTT client
Pip is a management tool for the Python package. This tool provides find, download, install and uninstall functions for Python package.
```
pip3 install paho-mqtt
```
## Connect to the MQTT broker
This article will use the free public MQTT broker provided by EMQ X. This service is based on MQTT IoT cloud platform to create. The accessing information of the broker is as follows:

+ Broker: broker.emqx.io
+ TCP Port: 1883
+ Websocket Port: 8083

## Import the Paho MQTT client
```
from paho.mqtt import client as mqtt_client
```

## Set the parameter of MQTT Broker connection
Set the address, port and topic of MQTT Broker connection. At the same time, we call the Python function random.randint to randomly generate the MQTT client id.
```
brokerAddress="localhost"
port=1883
user="root"
password="root"
```
## Write the MQTT connect function
Write the connect callback function on_connect. This function will be called after connecting the client, and we can determine whether the client is connected successfully according to rc in this function. Usually, we will create an MQTT client at the same time and this client will connect to broker.emqx.io.

```
def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected=True
        client.subscribe("Testing")
        client.on_message=on_message
    else:
        print("Client is not connected")
```

## Subscribe to messages
Write the message callback function on_message. This function will be called after the client received messages from the MQTT Broker. In this function, we will print out the name of subscribed topics and the received messages.

```
def on_message(client,userdata,message):
    print("Message received")
    print("Message received" +":"+ str(message.payload.decode("utf-8")))
    print("Topic"+":"+ str(message.topic))
```
## Publish messages
Run the code of publishing messages, we will see that the client connects successfully and publishes messages successfully
```
python3 pub.py
```
## Subscribe to messages
Run the code of subscribing to messages, we will see that the client connects successfully and receives the published messages successfully
```
python3 sub.py
```
Copyright notice: this article was originally written by EMQ. If you want to reprint, please indicate the source clearly. The link of original article：https://www.emqx.io/blog/how-to-use-mqtt-in-python

