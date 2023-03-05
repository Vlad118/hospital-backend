import os
from main import Main
from request import Request
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page Route' # Codrin what is the point of doing these things

# get login information and return state with nurse name if required
@app.route('/api/login', methods = ['GET', 'POST'])
def login_patient():
    selected_person = request.form.get('person')
    return_dict = []

    if selected_person == "NURSE":
        nurse_id = request.form.get("nurse_id")
        nurse_password = request.form.get('nurse_password')

        if Main.check_nurse(nurse_id, nurse_password):
            nurse = Main.get_nurse_info()
            return_dict['status'] = 202 # OK accepted nurse
            return_dict['forename'] = nurse.forename
            return_dict['surname'] = nurse.surname
        else:
            return_dict['status'] = 404 # error not found

    else:   # patient
        patient_id = request.form.get('id')
        if Main.check_patient_id(patient_id):
            return_dict['status'] = 202 # OK accepted patient
        else:
            return_dict['status'] = 404 # error not found

    return return_dict # (status) for patient; (status, forename, surname) for nurse

@app.route('/api/get_next_task', methods = ['GET', 'POST'])
def get_next_task():
    task = Main.get_next_request() # tuple(patient_id, type_of_request, location)
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
    request.priority = Main.get_priority_from_type()
    request.type_of_request = type_of_request
    request.location = location # todo
    request.extra_info = extra_info
    
    Main.add_request(request)   # adds request to database where request_id is generated

# Run the application
if __name__ == '__main__':
    app.run(debug = True)