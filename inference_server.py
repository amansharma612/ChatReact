# LOADING ALL THE REQUIRED MODULES TO RUN THE API
from nltk.tokenize import word_tokenize
from keras.utils import pad_sequences
from keras.utils.np_utils import to_categorical
import pickle
import numpy as np
from keras.layers import Embedding
from keras.layers import Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation
from keras.layers import Input, Dense
from keras.models import Sequential
from sklearn import preprocessing
import tensorflow as tf
from fastapi import FastAPI, Request
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# REQUIRED PARAMS AND OBJECTS
input_length = 15
model = tf.keras.models.load_model('saved_model/my_model')

f = open('tokenizer.pickle', 'rb')
tok = pickle.load(f)
f.close()
askdlaskd
from nltk.corpus import stopwords
words = set(stopwords.words("english"))
count = 0
for elem in iter(words):
    count = count + 1
    if count == 20:
        break
    print(elem)

def give_answer(query):
    responses = [
        "I dont know about it",
        "Are you requesting aircraft information?",
        "Trying to find the cost",
        "Finding the airline Information",
        "Requesting Flight Information?",
        "Finding the time",
        "Requesting Ground Service for the same",
        "Finding the seats information"
    ]
    words_text = ' '.join([word for word in query.split() if word not in (words)])
    words_text.replace("\d+", "")
    tokens_for_testing = tok.texts_to_sequences([words_text])
    model_input = pad_sequences(tokens_for_testing, input_length)
    out_vec = model.predict(model_input)
    val = np.argmax(out_vec)
    return responses[val]   


# ------------------------FAST API IMPLEMENTATION---------------------
class Item(BaseModel):
    message: str


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/message/')
async def create_message(item: Item):
    return {"message": give_answer(item.message)}