# save this as app.py
from flask import Flask, request, render_template
import pickle
import pandas as pd
import openpyxl

app = Flask(__name__)
model = pickle.load(open('ML_Model1', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction.html', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        Gender = int(request.form['Gender'])
        Married = int(request.form['Married'])
        Dependents = int(request.form['Dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])
        Credit_History = int(request.form['Credit_History'])
        Property_Area = int(request.form['Property_Area'])
        ApplicantIncome = int(request.form['ApplicantIncome'])
        CoapplicantIncome = int(request.form['CoapplicantIncome'])
        LoanAmount = int(request.form['LoanAmount'])
        Loan_Amount_Term = int(request.form['Loan_Amount_Term'])


        
        feature = [[Gender, Married,Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]] 
        print(feature)
        prediction = model.predict(feature)
        data = {
        'Gender': [Gender],
        'Married': [Married],
        'Dependents': [Dependents],
        'Education': [Education],
        'Self_Employed': [Self_Employed],
        'Credit_History': [Credit_History],
        'Property_Area': [Property_Area],
        'ApplicantIncome': [ApplicantIncome],
        'CoapplicantIncome': [CoapplicantIncome],
        'LoanAmount': [LoanAmount],
        'Loan_Amount_Term': [Loan_Amount_Term]
        }
        df = pd.DataFrame(data)

        df.to_excel('LoanExcelSheet.xlsx', index=False)

        if prediction==1:
            return render_template("prediction.html", prediction_text="Congratulations!! you are eligible for getting the loan", prediction_color = "green")
        
        if prediction==0:
            return render_template("prediction.html", prediction_text="Sorry, According to our Calculations, you are not eligible for getting the loan", prediction_color = "red")




    else:
        return render_template("prediction.html")


predict
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug =True)
