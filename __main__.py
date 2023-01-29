from os import environ
from os.path import dirname, join
# environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from joblib import load
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from deep_translator import GoogleTranslator

NUM_WORDS = 189
MAX_TEXT_LEN = 910
MODEL_PATH = "training_1/model"
model_dir = dirname(MODEL_PATH)

if __name__ == "__main__":
    translator = GoogleTranslator(source="it", target="en")
    model = tf.keras.models.load_model(MODEL_PATH)
    tokenizer_path = join(model_dir, "tokenizer.joblib")
    tokenizer: Tokenizer = load(tokenizer_path)
    while True:
        messages = [input("Message: ")]
        translated_messages = list(map(translator.translate, messages))
        for translated_message in translated_messages:
            print(f"Translated Message: {translated_message}")
        sequences = tokenizer.texts_to_sequences(translated_messages)
        X = pad_sequences(sequences, maxlen=NUM_WORDS)
        print(sequences)
        y = model.predict(X, verbose=0).flatten()
        for prediction in y:
            if y > 0.5:
                print("Not SPAM")
            else:
                print("SPAM")
