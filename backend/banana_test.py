import pathlib
import np
import tensorflow as tf

AUTOTUNE = tf.data.AUTOTUNE

batch_size = 32
img_height = 800
img_width = 600

new_model = tf.keras.models.load_model('saved_models/banana_model')

def predict(image):
    predictions = new_model.predict(image)
    print(predictions); ds
    return predictions


