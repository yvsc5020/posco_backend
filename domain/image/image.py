import base64
import os
from pororo import Pororo
from jamo import h2j, j2hcj
import paho.mqtt.client as mqtt
import json
import pickle

path = 'domain/separate/c2i.pickle'

with open(path, 'rb') as fr:
    change = pickle.load(fr)


def caption(file):
    dir = 'domain/image/file'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    model = Pororo(task='caption', lang='ko')

    img = base64.b64decode(file)
    path = 'domain/image/file/image.jpg'
    with open(path, 'wb') as f:
        f.write(img)

    caption_res = model(path)

    result = []

    mqttc = mqtt.Client('posco_backend')
    mqttc.connect("localhost", 1883)

    split_text = list(caption_res.replace('.', ''))

    for word in split_text:
        change_int_list = []
        word = list(j2hcj(h2j(word)))

        while len(word) != 3:
            word.append("")

        for char in word:
            change_int_list.append(change[char])

        result.append(change_int_list)

    mqttc.publish('test', json.dumps(result))

    return caption_res
