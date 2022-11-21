import numpy as np
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from IPython.display import HTML


from skforecast.utils import save_forecaster
from skforecast.utils import load_forecaster
import pickle
import skforecast

app = Flask(__name__)
model = load_forecaster('forecaster.pkl')


@app.route('/predict',methods=['POST'])
def predict():
    json_ = request.json
    prediction = model.predict(int(json_))
    return jsonify({"Prediction":list(prediction)})


if __name__ == "__main__":
    app.run(debug=True)


