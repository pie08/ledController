from flask import Flask
from flask import *

app = Flask(__name__)

@app.route('/api/leds', methods=['POST'])
def leds():
    print(request)