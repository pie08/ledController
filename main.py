import paho.mqtt.client as mqtt
import json
import threading
import multiprocessing
from ledController import *

# non-blocking threaded class for controlling leds
class process(threading.Thread):
    def __init__(self, data):
        self.data = data
        self.pattern = str(self.data.get('pattern')).lower()
        self.args = self.data.get('args') or {}
        self.color = colorFromArray(self.args.get('color') if self.args else [127, 0, 127])
        self.delay = self.args.get('delay') if self.args else None
        self.running = True
        self.reset = True
        threading.Thread.__init__(self)

    def run(self):
        while self.running:
            try:
                if self.reset:
                    reset()

                if self.pattern == 'colorwipe':
                    colorWipe(strip, self.color, self.delay or 50)

                if self.pattern == 'theaterchase':
                    theaterChase(strip, self.color, self.delay or 50)

                if self.pattern == 'police':
                    police(strip, self.delay or 200)

                if self.pattern == 'policefull':
                    policeFull(strip, self.delay or 200)

                if self.pattern == 'policefade':
                    policeFade(strip, self.delay or 20)

                if self.pattern == 'twinkle':
                    twinkle(strip, self.color, self.args.get('count') or 3, self.delay or 2)

                if self.pattern == 'twinklerandom':
                    twinkleRandom(strip, self.args.get('count') or 3, self.delay or 20)

                if self.pattern == 'snowsparkle':
                    snowSparkle(strip, self.color, self.delay or 150, self.args.get('speed') or 100)

                if self.pattern == 'horizontalbounce':
                    horizontalBounce(strip, self.color, self.args.get('delayreturn') or 0, self.delay or 20, self.args.get('length') or 10)

                if self.pattern == 'colorcycle':
                    colors = []
                    for color in self.args.get('colors'):
                        colors.append(colorFromArray(color))
                    colorCycle(strip, colors, self.delay or 20, )

                if self.pattern == 'usarandom':
                    usaRandom(strip, self.args.get('step') or 1, self.args.get('fill') or False, self.delay or 100)

                if self.pattern == 'breathing':
                    colors = []
                    for color in self.args.get('colors'):
                        colors.append(colorFromArray(color))
                    breathing(strip, colors, self.args.get('delayExit') or 0, self.delay or 20)

                if self.pattern == 'breathingrandom':
                    breathingRandom(strip, self.args.get('delayExit') or 0, self.delay or 20)

                if self.pattern == 'backandforth':
                    colors = []
                    for color in self.args.get('colors'):
                        colors.append(colorFromArray(color))
                    backAndForth(strip, colors[0], colors[1], self.args.get('delayreturn') or 0, self.delay or 25)

                if self.pattern == 'runninglights':
                    runningLights(strip, self.color, self.args.get('precision') or 2, self.delay or 50)

                if self.pattern == 'meteor':
                    meteor(strip, self.color, self.args.get('decay') or 150, self.args.get('size') or 3, self.delay or 30)

                if self.pattern == 'rainbow':
                    rainbow(strip, self.delay or 20)

                if self.pattern == 'rainbowcycle':
                    rainbowCycle(strip, self.delay or 20)

                if self.pattern == 'theaterchaserainbow':
                    theaterChaseRainbow(strip, self.delay or 50)

                if self.pattern == 'off':
                    colorWipe(strip, Color(0, 0, 0), 10)
                    
            except Exception as err:
                print(err)

    def setData(self, data):
        self.data = data
        self.pattern = str(self.data.get('pattern')).lower()
        self.args = self.data.get('args')
        self.color = colorFromArray(self.args.get('color') if self.args else [127, 0, 127])
        self.delay = self.args.get('delay') if self.args else None
        self.reset = self.args.get('reset') or True if self.args else True

    def kill(self):
        self.running = False

p = process({ 'pattern': None })

# The callback for when the client receives a CONNACK response from the server.
def connectMqtt():
    def onConnect(client, userdata, flags, rc):
        if rc == 0:
            print('Successfully connect to MQTT broker')
            client.subscribe('room/ledcontroller')
        else:
            print(f'Failed to connect to MQTT broker, status code {rc}')

    client = mqtt.Client()
    client.on_connect = onConnect
    client.connect('test.mosquitto.org', 1883, 60)
    return client

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    p.setData(data)


client = connectMqtt()
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
import time
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
try:
    p.start()
    client.loop_forever()
except KeyboardInterrupt:
    p.kill()
    p.join()
    colorWipe(strip, Color(0, 0, 0), 20)
    