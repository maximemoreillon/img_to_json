from flask import Flask, escape, request, jsonify
import requests
import cv2
import numpy as np
import json

PORT = 5002
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Img2Array v10"

@app.route('/img', methods=['POST'])
def img():
    print('Received POST on /img')

    # Extract path from request
    uri = request.json['uri']
    print(uri)
    try:
        response = requests.get(uri, timeout=3)
    except :
        return "Error getting image"
    else:
        image = np.array(bytearray(response.content), dtype=np.uint8)

        # Normalization included
        image_numpy = cv2.imdecode(image, -1)/255


        # prepare payload
        payload = json.dumps( {'instances': [image_numpy.tolist()]} )

        # Send request
        r = requests.post("http://172.16.98.148:30111/v1/models/redblack:predict", data=payload)

        return r.text

app.run('0.0.0.0',PORT)
