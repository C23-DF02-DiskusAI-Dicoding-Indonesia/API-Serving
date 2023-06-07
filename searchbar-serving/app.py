from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import string
import json

app = Flask(__name__)
CORS(app)  # Mengaktifkan CORS untuk aplikasi Flask

model = load_model('model.h5')
with open('tokenizer.json') as f:
    tokenizer = tokenizer_from_json(json.load(f))

@app.route('/')
def index():
    return "API is running."


@app.route('/suggest', methods=['POST'])
def suggest():
    query = request.form.get('query')  # Access form data using request.form.get()
    token_list = tokenizer.texts_to_sequences([query])[0]
    token_list = pad_sequences(
        [token_list], maxlen=model.input_shape[1], padding='pre')
    predicted = model.predict(token_list)
    predicted = np.argsort(-predicted)[0][:3]

    suggestions = []
    for index in predicted:
        for word, word_index in tokenizer.word_index.items():
            if word_index == index:
                suggestions.append(f"{query} {word}")
                break
    
    return jsonify({'suggestions': suggestions})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
