from flask import Flask, request,renderm_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

## Route for a home page

@app.route("/")
def index():
    return renderm_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return renderm_template("home.html")
    else:
        data = CustomData