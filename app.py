from flask import Flask,request,abort,jsonify
from flask_cors import CORS
import numpy as np
import pickle
app = Flask(__name__)
CORS(app)
model = pickle.load(open('xgbModel.pkl','rb'))
@app.route('/')
def index():
    return "Hello"

@app.route('/predict')
def predictValue():
    try:
        windSpeed = float(request.args.get('windSpeed'))
        windDirection = float(request.args.get('windDirection'))
        windGust = float(request.args.get('windGust'))
        print(windSpeed,windDirection,windGust)
        output = model.predict(np.array([[windSpeed,windDirection,windGust]]))
        print(output)
        activePower = output[0]
        return jsonify(output=str(activePower))
    except Exception as e:
        print("error",e)
        abort(400)
if __name__ == "__main__":
    app.run(debug=True)