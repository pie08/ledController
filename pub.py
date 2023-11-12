import paho.mqtt.client as mqtt
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pattern')
args = parser.parse_args()


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


client = connectMqtt()
client.loop_start()

if args.pattern:
    data = json.dumps({
        'pattern': args.pattern,
        'args': {'color': (127, 0, 127), 'colors': [(127, 0, 127), (127, 0, 0)]}
    })
else:
    data = json.dumps({
        'pattern': 'rainbow',
        'args': {}
    })

client.publish('room/ledcontroller', data, qos=2)
client.loop_stop()
