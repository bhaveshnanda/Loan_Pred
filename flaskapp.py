# save this as app.py
from flask import Flask, request, render_template
import pickle

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

        if prediction==1:
            return render_template("prediction.html", prediction_text="Congratulations!! you will get the loan from Bank", prediction_color = "green")
        
        if prediction==0:
            return render_template("prediction.html", prediction_text="Sorry, According to our Calculations, you will not get the loan from Bank", prediction_color = "red")




    else:
        return render_template("prediction.html")


predict
if __name__ == "__main__":
    app.run(debug=True)
