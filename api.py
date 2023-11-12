from flask import Flask
from flask import *
from flask_cors import CORS, cross_origin
from send import send

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/leds', methods=['POST'])
@cross_origin()
def leds():
    try:
        print(request.mimetype)
        data = request.get_json()
        print('test')
        print(data)
        # send request data to mqtt server
        send(data)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)
