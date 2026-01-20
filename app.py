import streamlit as st
import tensorflow as tf
import pickle
import json
import numpy as np
import time
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Load model & resources
@st.cache_resource
def load_resources():
    model = tf.keras.models.load_model("saved_model/next_word_lstm.keras")

    with open("saved_model/tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    with open("saved_model/config.json", "r") as f:
        config = json.load(f)

    return model, tokenizer, config["max_len"]

model, tokenizer, max_len = load_resources()


# index → word mapping
index_to_word = {index: word for word, index in tokenizer.word_index.items()}


# Real-time prediction function (0.2s delay)
def predict_next_words_realtime(text, num_words=20, delay=0.2):
    output_placeholder = st.empty()
    generated_text = text

    for _ in range(num_words):
        token_text = tokenizer.texts_to_sequences([generated_text])[0]

        padded_token_text = pad_sequences([token_text], maxlen=max_len, padding='pre')
        predicted_index = np.argmax(model.predict(padded_token_text, verbose=0))
        predicted_word = index_to_word.get(predicted_index)

        if predicted_word is None:  break

        generated_text += " " + predicted_word
        output_placeholder.markdown(f"### {generated_text}")

        time.sleep(delay)


# UI
st.set_page_config(page_title="Next Word Predictor", layout="centered")
st.title("Next Word Prediction (LSTM)")
st.caption("Real-time word generation (0.2 sec delay)")

seed_text = st.text_input("Enter seed text", value="Three Phonetic Components")

num_words = st.slider("Number of words to generate", min_value=10, max_value=100, value=20)

if st.button("Generate"):
    if seed_text.strip() == "":
        st.warning("Please enter some seed text.")
    else:
        predict_next_words_realtime(seed_text, num_words=num_words, delay=0.2)
