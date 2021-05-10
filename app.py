import joblib

def predict_tran(age,gender,educationbackground,maritalstatus,empdepartment,empjobrole,btf,distancefromhome,EmpEducationLevel,EmpEnvironmentSatisfaction,EmpHourlyRate,EmpJobInvolvement,EmpJobLevel,EmpJobSatisfaction,NumCompanesWorked,overtime,EmpLastSalaryHikePercent,EmpRelationshipSatisfaction,TotalWorkExperienceInYears):
    model = joblib.load('performance.pkl')
    prediction = model.predict([[age,gender,educationbackground,maritalstatus,empdepartment,empjobrole,btf,distancefromhome,EmpEducationLevel,EmpEnvironmentSatisfaction,EmpHourlyRate,EmpJobInvolvement,EmpJobLevel,EmpJobSatisfaction,NumCompanesWorked,overtime,EmpLastSalaryHikePercent,EmpRelationshipSatisfaction,TotalWorkExperienceInYears]])
    
    if prediction == 2:
        return 'Average Performer'
    
    elif prediction == 3:
        return 'Good Performer'

    elif prediction == 4:
        return 'Excellent Performer'    


import flask
from flask import render_template, request, url_for
from flask_cors import CORS

app = flask.Flask(__name__,)
CORS(app)

@app.route('/',methods=['GET'])
def default():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    #extract data from post request
    age = float(request.form['age'])
    gender = float(request.form['gender'])
    educationbackground = float(request.form['educationbackground'])
    maritalstatus = float(request.form['maritalstatus'])
    empdepartment = float(request.form['empdepartment'])
    empjobrole = float(request.form['empjobrole'])
    btf = float(request.form['btf'])
    distancefromhome = float(request.form['distancefromhome'])
    EmpEducationLevel = float(request.form['EmpEducationLevel'])
    EmpEnvironmentSatisfaction = float(request.form['EmpEnvironmentSatisfaction'])
    EmpHourlyRate = float(request.form['EmpHourlyRate'])
    EmpJobInvolvement = float(request.form['EmpJobInvolvement'])
    EmpJobLevel = float(request.form['EmpJobLevel'])
    EmpJobSatisfaction = float(request.form['EmpJobSatisfaction'])
    NumCompanesWorked = float(request.form['NumCompanesWorked'])
    overtime = float(request.form['overtime'])
    EmpLastSalaryHikePercent = float(request.form['EmpLastSalaryHikePercent'])
    EmpRelationshipSatisfaction = float(request.form['EmpRelationshipSatisfaction'])
    TotalWorkExperienceInYears = float(request.form['TotalWorkExperienceInYears'])
    print(age,gender,educationbackground,maritalstatus,empdepartment,empjobrole,btf,distancefromhome,EmpEducationLevel,EmpEnvironmentSatisfaction,EmpHourlyRate,EmpJobInvolvement,EmpJobLevel,EmpJobSatisfaction,NumCompanesWorked,overtime,EmpLastSalaryHikePercent,EmpRelationshipSatisfaction,TotalWorkExperienceInYears)
    prediction = predict_tran(age,gender,educationbackground,maritalstatus,empdepartment,empjobrole,btf,distancefromhome,EmpEducationLevel,EmpEnvironmentSatisfaction,EmpHourlyRate,EmpJobInvolvement,EmpJobLevel,EmpJobSatisfaction,NumCompanesWorked,overtime,EmpLastSalaryHikePercent,EmpRelationshipSatisfaction,TotalWorkExperienceInYears)
    print(prediction)
    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
