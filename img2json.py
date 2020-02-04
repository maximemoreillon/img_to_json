from flask import Flask, escape, request, jsonify
import requests
import cv2
import numpy as np
import json

PORT = 5002
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Img2Array v6"

@app.route('/img', methods=['POST'])
def img():
    print('Received POST on /img')

    # Extract path from request
    #path = request.json['path']

    # Normalization of input
    #img_numpy = cv2.imread(path)/255

    # prepare payload
    #payload = json.dumps( {'instances': [img_numpy.tolist()]} )

    # Send request
    return "banana"
    # r = requests.post("http://192.168.179.25:30111/v1/models/redblack:predict", data=payload)

    # return r.text

app.run('0.0.0.0',PORT)
