# 📸 Tensor Camera App
Introducing our innovative Tensor Camera App, designed to streamline the process of testing and evaluating newly trained models in real-world scenarios. Our app seamlessly integrates with Python servers, providing a user-friendly interface to send camera feeds for instant predictions.

>Download Links will be provided here when the App is Published.⏳⏳

## 🤔 How to use Tensor Camera ?

1. Download the Tensor Camera from App Store.
2. Download the `ML-CameraSocket.py` file.
3. Load your Computer Vision Model.
4. Check all the `#TODOs:`
5. Set the Prediction Logic: `Example Below:`
```
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

```
6. Run the Server.

>📝 NOTE: Make Sure your `PC` and `Mobile` are connected to the same `Wifi`

7. You will see the following output:
```
 * Serving Flask app 'ML-WebSocket'
 * Debug mode: off
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.2.118:8080
 ```

>📝 NOTE: Do not Use `127.0.0.1:8080` in the Server Configuration

8. Use the correct `IP Address` and `PORT` in the App.
9. Press Test Connection
10. When `Connected` then open the Camera and See the Real-Time 🪄Magic.
