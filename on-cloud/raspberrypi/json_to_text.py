import json

def convert_txt(str):
    out = []
    j = json.loads(str)
    for i in range(len(j)):
        out.append(j[i]['caption'])
    return out

with open("/home/pi/Documents/aisight_rpi/captions/vis.json") as f:
    inp = f.read()
    txt = convert_txt(str(inp))

with open("/home/pi/Documents/aisight_rpi/captions/tts.txt","w") as f:
    for i in range(len(txt)):
        f.write(txt[i] + ". ")

