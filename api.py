import os
from main import Main
from flask import Flask, request, flash, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page Route'

# get login information and return patient or nurse state
@app.route('/api/login', methods = ['GET', 'POST'])
def login_patient():
    selected_person = request.form.get('person')
    patient_id = request.form.get('id')
    if selected_person == "NURSE":
        nurse_password = request.form.get('password')
        
        if Main.check_nurse(nurse_id, nurse_password):
            return 
        else:
            return # allow for login retry how
    else:
        if Main.check_patient_id(patient_id):
            return selected_person
        else:
            return # allow for login retry how

@app.route('/api/login/nurse', methods = ['GET', 'POST'])
def get_next_task():
    if request.form.get('break_active') == False: # ensuring BREAK button is not pressed
        request_tuple = Main.get_next_request.getRequest() # tuple(patient_id, type_of_request, location)

    return # task information ?

# Run the application
if __name__ == '__main__':
    app.run(debug = True)