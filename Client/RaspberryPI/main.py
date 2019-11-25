
from time import sleep
import time
import json
import subprocess
import requests
import cv2


def take_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    time.sleep(-1)
    return frame

def convert_txt(str):
    out = []
    j = json.loads(str)
    for i in range(len(j)):
        out.append(j[i]['caption'])
    return out

def main():
    speech = "aplay /app/lookdave.wav"
    API_ENDPOINT = "http://34.69.114.102:5000/image"
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    while True:
        frame = take_image()
        _, img_encoded = cv2.imencode('.jpg', frame)
        r = requests.post(url = API_ENDPOINT, data=img_encoded.tostring(), headers=headers)
        out = r.text
        out = out.split("[")[1].split("]")[0]
        out = json.loads(out)
        caption = out['caption']
        subprocess.check_output(["pico2wave", "-w", "lookdave.wav", caption])
        subprocess.call(speech.split())
   
        
if __name__ == "__main__":
    main()