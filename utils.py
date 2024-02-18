import pickle
import json
import numpy as np
import config

def get_prediction(Gender, Married, Dependents, Education, Self_Employed,
                   ApplicantIncome, CoapplicantIncome, LoanAmount,
                   Loan_Amount_Term, Credit_History, Property_Area):

    with open(config.model_pickle, 'rb') as f:
        model = pickle.load(f)

    with open(config.model_encod, 'r') as f:
        data = json.load(f)

    Gender = data['Gender'][Gender]
    Married = data['Married'][Married]
    Dependents = data['Dependents'][Dependents]
    Education = data['Education'][Education]
    Self_Employed = data['Self_Employed'][Self_Employed]
    Property_Area = data['Property_Area'][Property_Area]

    test_array = np.array([[Gender, Married, Dependents, Education, Self_Employed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount,
                            Loan_Amount_Term, Credit_History, Property_Area]])

    result = model.predict(test_array)[0]

    return result
