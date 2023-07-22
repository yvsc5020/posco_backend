from jamo import h2j, j2hcj
import pickle
import paho.mqtt.client as mqtt
import json

path = 'domain/separate/c2i.pickle'

with open(path, 'rb') as fr:
    change = pickle.load(fr)


def split_text(text: str):
    result = []

    mqttc = mqtt.Client('posco_backend')
    mqttc.connect("localhost", 1883)

    split_text = list(text)

    for word in split_text:
        change_int_list = []
        word = list(j2hcj(h2j(word)))

        while len(word) != 3:
            word.append("")

        for char in word:
            change_int_list.append(change[char])

        result.append(change_int_list)

    mqttc.publish('test', json.dumps(result))

    return "200"
