
from flask import Flask, render_template
from firebase import firebase

app = Flask(__name__)

firebase_url = "https://people-f979d-default-rtdb.firebaseio.com/"  
firebase = firebase.FirebaseApplication(firebase_url, None)

@app.route('/')
def index():
    result = firebase.get('/sensor_readings/distance', None)
    latest_key = max(result.keys())
    distance = result[latest_key]
    
    return render_template('ultrasonic.html', distance=distance)

if __name__ == '__main__':
    app.run(debug=True)
