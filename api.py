import os
from main import Main
from request import Request
from flask import Flask, request
from flask_cors import CORS
from flask import Response

app = Flask(__name__)
CORS(app)

main = Main()

@app.route('/')
def home():
    return 'Home Page Route' # Codrin what is the point of doing these things

# get login information and return state with nurse name if required
@app.route('/api/login', methods = ['GET', 'POST'])
def login_patient():
    selected_person = request.json.get('person')

    if selected_person == "NURSE":
        try:
            nurse_id = int(request.json.get("nurse_id"))
            nurse_password = request.json.get('nurse_password')
            if main.check_nurse(nurse_id, nurse_password):
                return "Success", 202
            else:
                return "Fail", 404
            
        except:
            print("exception")
            return "Fail", 404

    else:   # patient
        patient_id = request.json.get('id')
        if main.check_patient_id(patient_id):
            return "Success", 200
        else:
            return "Fail", 404

@app.route('/api/get_next_task', methods = ['GET', 'POST'])
def get_next_task():
    task = main.get_next_request() # tuple(patient_id, type_of_request, location)
    return_dict = []
    return_dict['patient_id'] = task.patient_id
    return_dict['type_of_request'] = task.type_of_request
    return_dict['location'] = task.location
    return return_dict # (patient_id, type_of_request, location)

@app.route('/api/send_request', methods = ['GET', 'POST'])
def send_request():
    patient_id = request.form.get('patient_id')
    type_of_request = request.form.get('type_of_request')
    location = None # completely unimplemented, future project!
    extra_info = request.form.get('extra_info')

    request = Request()
    request.patient_id = patient_id
    request.priority = main.get_priority_from_type()
    request.type_of_request = type_of_request
    request.location = location # todo
    request.extra_info = extra_info
    
    main.add_request(request)   # adds request to database where request_id is generated

# Run the application
if __name__ == '__main__':
    app.run(debug = True)