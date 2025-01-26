from flask import Flask

app=Flask(__name__)

# lets create endpoint

@app.route('/')
def home():
    return "<h1>Flask Web API</h1>"

@app.route('/ping')
def pinger():
    return {"messege":"Hello There"}
