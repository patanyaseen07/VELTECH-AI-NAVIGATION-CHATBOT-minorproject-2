# VELTECH-AI-NAVIGATION-CHATBOT         


The Vel Tech AI Navigation Chatbot is designed to assist users in navigating the Vel Tech University campus. By leveraging Natural Language Processing (NLP) and deep learning, the chatbot can understand user queries and provide all college queries and also accurate directions using an interactive indoor map.

## Features
- Interactive Chat Interface: Users can interact with the chatbot through a simple and user-friendly interface.
- NLP and Deep Learning: Utilizes NLP and deep learning to understand and respond to user queries.
- Indoor Navigation: Provides hyperlinks to an indoor map for easy navigation of campus buildings.
- Text-to-Speech Functionality: The chatbot can speak responses using a text-to-speech synthesis.

Your virtual guide to Vel Tech! Get answers about:
Campus directions and building locations
Department and faculty information
Events and schedules
Library resources
...and more!

<img width="5536" height="1752" alt="diagram" src="https://github.com/user-attachments/assets/c71c469f-d60c-47e5-9bd2-367110e6a01b" />


To explain this project from start to end, here's a detailed step-by-step guide:

## Step 1: Project Setup & Dependencies
First, set up your environment. Create a virtual environment and install dependencies.

Show requirements.txt: Flask, NLTK, TensorFlow, Keras, etc.

Command: pip install -r requirements.txt

Download NLTK data: nltk.download('punkt') and nltk.download('wordnet')

These libraries handle web serving, text processing, and machine learning.



## Step 2: Understanding the Data (intents.json)
Chatbots need training data. Our intents.json defines patterns and responses for university info.

Show structure: Tags like "welcome", "hours", "departments" with patterns (user inputs) and responses.

Patterns are example questions, responses are bot replies. This covers greetings, timings, fees, etc.

For 'hours', patterns like 'what is college timing?' map to responses about class schedules.



## Step 3: Training the Model (Training.py)
Train the AI model. Training.py processes intents into a neural network.

Code: Load intents, tokenize patterns, create bag-of-words, train Keras sequential model (128 neurons, dropout, softmax output).

Lemmatization reduces words to roots. Bag-of-words vectorizes input. Model predicts intent from user text.

Run training: python Training.py (200 epochs, saves model.h5, texts.pkl, labels.pkl).

This creates a trained model that classifies user intents.



## Step 4: Building the Flask App (app.py)
With the model trained, build the backend. app.py loads the model and handles chat logic.

Functions: clean_up_sentence (tokenize/lemmatize), bow (create input vector), predict_class (get intent), get_response (fetch reply).

Routes: "/" renders index.html, "/get" processes user messages via chatbot_response().

Flask serves the web page and responds to AJAX requests from the frontend.



## Step 5: Creating the Web Interface (index.html & CSS)
For the frontend, use HTML, CSS, and JS. index.html has a chat UI with message bubbles.

CSS: Styles for chat area, messages, input form.

JS: Handles form submission, appends messages, voice recognition (SpeechRecognition API), text-to-speech (SpeechSynthesis).

Voice button uses browser APIs for speech input. Mute button toggles TTS.


## Step 6: Running & Demo
Run the app: python app.py (opens at localhost:5000).

Demo: Type queries like "what are college hours?" or "where is Vel Tech?"

Voice: Click mic, speak, bot responds with voice.

The bot uses the trained model to predict intent and reply with university info.
<img width="1565" height="1120" alt="Screenshot 2025-10-08 163435" src="https://github.com/user-attachments/assets/7e8570df-f349-46a4-92b4-5fcc8dc6b2c8" />


<img width="1831" height="1038" alt="image" src="https://github.com/user-attachments/assets/7a2494bb-d7f1-42d2-abf6-7bbfdd8f0615" />


## Improvements
Add more intents, integrate APIs, use transformers like BERT for better accuracy.

Challenges: Training data quality affects responses. Voice works in modern browsers.


## Installation
1. Clone the repository:
git clone https://github.com/patanyaseen07/VELTECH-AI-NAVIGATION-CHATBOT-minorproject-2.git
2. Install dependencies:
pip install -r requirements.txt
3. Run the project:
python app.py

## Technologies Used
• Python
• Flask
• TensorFlow/Keras
• NLTK

## Contributing
Feel free to fork this project, make changes, and submit a pull request. Contributions are always welcome!

