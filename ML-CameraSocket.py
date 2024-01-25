'''
Author:Sarbjeet Singh
Contact: https://www.sarbzone.com/
GitHub: https://github.com/SpunkySarb

'''
import keras as keras
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send
import base64


'''
#TODO 1: Load your Model Correctly...
'''
model = keras.models.load_model(
    "MODEL PATH HERE",
    custom_objects={"KerasLayer": hub.KerasLayer} #<---comment this if not needed..(This is used when you have custom layer during training which was loaded using hub.KerasLayer)
)
model.summary()


app = Flask(__name__)
CORS(app)

socketio = SocketIO(app)


@socketio.on("message")
def handle_message(message):
    '''
    This socket route recieves the message -> (image) as base64 string and then
    converts it to image tensor.

    Then you can perform your operations like:
    Resizing, Predicting, etc.

    Returns the string message you want to show to your ML-Camera App after prediction.
    for example: "Found Dog" or "Found Cat"
    
    '''
    image_data = base64.b64decode(message)

    image_array = np.frombuffer(image_data, dtype=np.float32).reshape(224, 224, 3)

    image = tf.constant(image_array, dtype=tf.float32)



    #TODO 2: Resize your image if you want to another dimensions, or leave as it is if you used the same dimensions.
    image_resized = tf.image.resize(image, [224, 224])

    # TODO 3: Add batch dimension if your model accepts batched data if not then you should remove this line to avoid incorrect shape errors.
    image_batch = tf.expand_dims(image_resized, 0)
    
    # TODO 4: Predict your output
    prediction = model.predict(image_batch)[0] 
    # TODO 5: Transform your prediction to Human readable format.
    value = prediction[0]
    animal = "Meow-Meow its a Cat "
    if round(value) == 1:
        animal = "Woof-Woof its a Dog 🐶"
    else:
        animal = "Meow-Meow its a Cat "

    send(animal) #TODO 6:Pass the predicted results in string format to send to the ML- Camera App.....


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080) #Do not change the PORT from 8000s to 5000s or anything else: try:8081, 8082, 8083 if need to change. Otherwise you may run into access denied by server Error. 403
