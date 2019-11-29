from flask import Flask
import subprocess
import json
import cv2
import numpy as np
from flask import request
import os

app = Flask(__name__)

EVAL_LUA = "th /opt/neural-networks/neuraltalk2/eval.lua -gpuid -1 -model /data/models/model.t7 -num_images 1 -dump_json 1 -image_folder /data/images"

def eval():
    subprocess.call(EVAL_LUA.split())

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/image', methods=['POST'])
def store_image():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("/data/images/1.jpg", img)
    os.chdir("/opt/neural-networks/neuraltalk2")
    eval()
    with open('/opt/neural-networks/neuraltalk2/vis/vis.json', 'r') as file:
        return file.read()
    return '{"captions":"error", "image_id":"0"}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
