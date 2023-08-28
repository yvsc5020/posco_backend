import base64
from jamo import h2j, j2hcj
import paho.mqtt.client as mqtt
import json
import pickle
import os
from PIL import Image
import googletrans
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

translater = googletrans.Translator()

path = 'domain/separate/c2i.pickle'

mqttc = mqtt.Client()
mqttc.connect("broker.mqtt-dashboard.com", 1883)

with open(path, 'rb') as fr:
    change = pickle.load(fr)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}


def predict_step(image_path):
    i_image = Image.open(image_path)
    if i_image.mode != "RGB":
        i_image = i_image.convert(mode="RGB")

    pixel_values = feature_extractor(images=i_image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds


def caption(file):
    mqttc.connect("broker.mqtt-dashboard.com", 1883)

    dir = 'domain/image/file'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    img = base64.b64decode(file)
    path = 'domain/image/file/image.jpg'
    with open(path, 'wb') as f:
        f.write(img)

    text = predict_step(path)[0]

    result = []

    split_text = list(text.replace('.', ''))

    for word in split_text:
        change_int_list = []
        word = list(j2hcj(h2j(word)))

        while len(word) != 3:
            word.append("")

        for char in word:
            change_int_list.append(change[char])

        result.append(change_int_list)

    mqttc.publish('posco', json.dumps(result))

    return text
