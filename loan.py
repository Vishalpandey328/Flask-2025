from flask import Flask
import pickle

app=Flask(__name__)

model_file=open("classifier.pkl","rb")
model = pickle.load(model_file)

model.pridct()
# lets create endpoint

@app.route('/')
def home():
    return "<h1>Loan Approval</h1>"

@app.route('/pridct')
def pridct():
    return "I Will Predict"