#!/usr/bin/env python
# coding: utf-8

import webbrowser
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
from flask import Flask, render_template, request

# Load model and data
model = load_model('model.h5')
with open('intents.json', encoding='utf-8') as file:
    intents = json.load(file)
words = pickle.load(open('texts.pkl', 'rb'))
classes = pickle.load(open('labels.pkl', 'rb'))

lemmatizer = WordNetLemmatizer()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"found in bag: {w}")
    return np.array(bag)

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    if not ints:
        return "Sorry, I'm not sure I understand. Can you try asking in a different way?"
    
    tag = ints[0]['intent']
    list_of_intents = intents_json.get('intents', [])
    
    for intent in list_of_intents:
        if intent['tag'] == tag:
            return random.choice(intent.get('responses', ["Sorry, I don't have a response for that."]))
    
    return "Sorry, I'm not sure I understand. Can you try asking in a different way?"

def chatbot_response(msg):
    ints = predict_class(msg, model)
    if not ints:
        return "Sorry, I'm not sure I understand. Can you try asking in a different way?"
    res = get_response(ints, intents)
    return res

# Flask setup
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run()
