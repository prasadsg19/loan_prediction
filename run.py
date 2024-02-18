from flask import Flask, request, jsonify, render_template
from utils import get_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def loan_prediction():
    # Retrieve form data
    Gender = request.form['Gender']
    Married = request.form['Married']
    Dependents = request.form['Dependents']
    Education = request.form['Education']
    Self_Employed = request.form['Self_Employed']
    ApplicantIncome = float(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = float(request.form['Credit_History'])
    Property_Area = request.form['Property_Area']

    result = get_prediction(Gender, Married, Dependents, Education, Self_Employed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount,
                            Loan_Amount_Term, Credit_History, Property_Area)
    final={0:'Not Approved',1:'Approved'}

    # Render the template with prediction result
    return render_template('index.html', prediction_result=final[result])

if __name__ == "__main__":
    app.run(debug=False)
