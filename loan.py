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
        loan_req = request.get_json()
        if loan_req['Gender']=='Male':
            Gender = 0
        else:
            Gender = 1
        if loan_req['Married']=='Unmerried':
            Married = 0
        else:
            Married = 1
        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History = loan_req['Credit_History']
        result = model.predict([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]])   
        
        if result == 0:
            pred = "Rejected"
        else:
            
            pred = "Approved"        
        return {"Loan_approval_status":pred}
    else:
        return "I Will Predict"