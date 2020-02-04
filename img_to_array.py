from flask import Flask, escape, request, jsonify
import requests
import cv2
import numpy as np
import codecs, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Img2Array"

@app.route('/img', methods=['POST'])
def img():
    print('Received POST on /img')

    # Extract path from request
    path = request.json['path']

    # Normalization of input
    img_numpy = cv2.imread(path)/255

    # prepare payload
    payload = json.dumps( {'instances': [img_numpy.tolist()]} )

    # Send request
    r = requests.post("http://192.168.179.25:30111/v1/models/redblack:predict", data=payload)

    return r.text


app.run('0.0.0.0',5002)
