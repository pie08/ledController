from flask import Flask
from flask import *
from send import send
# get all functions in a file
from inspect import getmembers, isfunction
import ledController
print(getmembers(ledController, isfunction))

app = Flask(__name__)


@app.route('/api/leds', methods=['POST'])
def leds():
    try:
        data = request.get_json()
        # validate request
        # send request data to mqtt server
        send(data)
        return Response(status=200)
    except:
        return Response(status=500)
