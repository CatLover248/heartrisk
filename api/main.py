from model import Heart
from flask import Flask, request, jsonify

#Initalize ML model
print("Initalizing model... This may take some time")
m = Heart()
m.init_model()

#Initalize Flask
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    Age = float(data["Age"])
    Sex = float(data["Sex"])
    Cholesterol = float(data["Cholesterol"])
    Diastolic = float(data["Diastolic"])
    Systolic = float(data["Systolic"])
    Heart_Rate = float(data["Heart_Rate"])
    Diabetes = float(data["Diabetes"])
    Family_History = float(data["Family_History"])
    Smoking = float(data["Smoking"])
    Obesity = float(data["Obesity"])
    Alcohol_Consumption = float(data["Alcohol_Consumption"])
    Exercise_Hours_Per_Week = float(data["Exercise_Hours_Per_Week"])
    Diet = float(data["Diet"])
    Previous_Heart_Problems = float(data["Previous_Heart_Problems"])
    Medication_Use = float(data["Medication_Use"])
    Stress_Level = float(data["Stress_Level"])
    Sedentary_Hours_Per_Day = float(data["Sedentary_Hours_Per_Day"])
    Income = float(data["Income"])
    BMI = float(data["BMI"])
    Sleep_Hours_Per_Day = float(data["Sleep_Hours_Per_Day"])
    Triglycerides = float(data["Triglycerides"])
    Physical_Activity_Days_Per_Week = float(data["Physical_Activity_Days_Per_Week"])
    return jsonify(Heart_Failure_Risk=str(m.predict_risk_at_heartfailure([Age,Sex,Cholesterol,Diastolic,Systolic,
        Heart_Rate, Diabetes,Family_History,Smoking,Obesity,Alcohol_Consumption,Exercise_Hours_Per_Week,Diet,Previous_Heart_Problems,Medication_Use,Stress_Level,Sedentary_Hours_Per_Day,
        Income,BMI,Sleep_Hours_Per_Day,Triglycerides,Physical_Activity_Days_Per_Week])))



app.run(debug=True)

