from flask import Flask, escape, request, jsonify
import requests
import cv2
import numpy as np
import codecs, json

app = Flask(__name__)

@app.route('/img', methods=['POST'])
def login():

    path = request.json['path']

    img_numpy = cv2.imread(path)/255



    payload = json.dumps( {'instances': [img_numpy.tolist()]} )
    #print(payload)



    r = requests.post("http://localhost:8501/v1/models/redblack:predict", data=payload)
    print(r.text)

    return 'Hello, World!'


app.run('0.0.0.0',5002)
