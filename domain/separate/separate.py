from jamo import h2j, j2hcj
import pickle
import paho.mqtt.client as mqtt
import json

path = 'domain/separate/c2i.pickle'

mqttc = mqtt.Client()
mqttc.connect("broker.mqtt-dashboard.com", 1883)

with open(path, 'rb') as fr:
    change = pickle.load(fr)


def split_text(text: str):
    mqttc.connect("broker.mqtt-dashboard.com", 1883)

    result = []

    split_text = list(text)

    for word in split_text:
        change_int_list = []
        word = list(j2hcj(h2j(word)))

        while len(word) != 3:
            word.append("")

        for char in word:
            change_int_list.append(change[char])

        result.append(change_int_list)

    mqttc.publish("posco_jamo", json.dumps(result))

    return json.dumps(result)
