import paho.mqtt.client as mqtt
import json


def connectMqtt():
    def onConnect(client, userdata, flags, rc):
        if rc == 0:
            print('Successfully connect to MQTT broker')
        else:
            print(f'Failed to connect to MQTT broker, status code {rc}')

    client = mqtt.Client()
    client.on_connect = onConnect
    client.connect('test.mosquitto.org', 1883, 60)
    return client


def send(data: object):
    client = connectMqtt()
    client.loop_start()
    client.publish('room/ledcontroller', json.dumps(data), qos=2)
    client.loop_stop()
