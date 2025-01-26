from flask import Flask, request
import pickle

app = Flask(__name__)

model_file = open("classifier.pkl", "rb")
model = pickle.load(model_file)


# model.predict(inputs)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Loan Approval Application</h1>"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # use model and predict

        pass
    else:
        return "I Will Predict"