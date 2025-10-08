#!/usr/bin/env python
# coding: utf-8

import nltk
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import random    

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()
words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Read intents.json with utf-8 encoding
try:
    with open('intents.json', encoding='utf-8') as data_file:
        intents = json.load(data_file)
except FileNotFoundError:
    print("Error: 'intents.json' file not found.")
    exit()
except json.JSONDecodeError:
    print("Error: 'intents.json' file is not a valid JSON.")
    exit()

# Process intents
for intent in intents.get('intents', []):
    for pattern in intent.get('patterns', []):
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))    

# Save words and classes
with open('texts.pkl', 'wb') as f:
    pickle.dump(words, f)
with open('labels.pkl', 'wb') as f:
    pickle.dump(classes, f)   

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Shuffle training data
random.shuffle(training)

# Convert training data to NumPy arrays
train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])

print("Training data created")  

# Create model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax')) 

# Compile model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])        

# Train and save model
try:
    hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
    model.save('model.h5')  # Removed hist argument
    print("Model trained and saved successfully.")
except Exception as e:
    print(f"Error during model training or saving: {e}")
