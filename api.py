from flask import Flask
from flask import *
from send import send

app = Flask(__name__)


@app.route('/api/leds', methods=['POST'])
def leds():
    try:
        data = request.get_json()
        send(data)
        return Response(status=200)
    except:
        return Response(status=500)
