from flask import Flask, jsonify, render_template, request

from project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Welcome to Insurance Prediction System")   
    return render_template("path.html")


@app.route("/predict_charges", methods = ["POST", "GET"])

def get_insurance_charges():
    if request.method == "GET":
        print("GET Method")

        age = eval(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = eval(request.args.get("bmi"))
        children = eval(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_charges()
        
        return render_template("path.html", prediction = charges)
    

    else:
        print("POST Method")

        age = eval(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = eval(request.form.get("bmi"))
        children = eval(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_charges()
        
        return render_template("path.html", prediction = charges)
    
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run()