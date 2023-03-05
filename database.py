import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connect = None
        self.cursor = None

    def connect_db(self):
        """ Creates a database connection with the SQLite database """
        self.connect = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.connect.cursor()

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS requests
            ([request_id] INTERGER, [patient_id] INTEGER, 
            [priority] INTEGER, [type_of_request] TEXT, [location] TEXT, [extra_info] TEXT)
            '''
        ) #location within hospital (wing, ward...)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS nurse
            ([nurse_id] INTEGER PRIMARY KEY, [forename] TEXT, [surname] TEXT, [email] TEXT,
            [password] TEXT, [location] TEXT)'''
        ) #location is within hospital (to be able to link to patient)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS patient
            ([patient_id] INTEGER PRIMARY KEY, [forename] TEXT, [surname] TEXT)'''
        )


    ### REQUESTS ###
    def get_request(self, id):
        params = (id,)
        result = self.cursor.execute(
            '''
            SELECT * from requests
            WHERE request_id = ?
            ''',params
        ).fetchone()
        if result == None:
            return -1
        return result

    def remove_request(self, id):
        params = (id,)
        self.cursor.execute(
            '''
            DELETE FROM requests
            WHERE request_id = ?''',params
        )
        self.connect.commit()


    def insert_request(self, request):
        params = (request.request_id, request.patient_id, request.priority, request.type_of_request, request.location, request.extra_info)
        self.cursor.execute("INSERT INTO requests VALUES(?,?,?,?,?,?)",params)
        self.connect.commit()

    def change_id_of_request(self,old_id,new_id):
        params = (new_id,old_id)
        self.cursor.execute(
            '''
            UPDATE requests
            SET request_id = ?
            WHERE request_id = ?
            ''',params
        )
        self.connect.commit()

    def clear_requests(self):
        self.cursor.execute("DELETE FROM requests")
        self.connect.commit()

        
    def clear_patients(self):
        self.cursor.execute("DELETE FROM patient")
        self.connect.commit()

        
    def clear_nurses(self):
        self.cursor.execute("DELETE FROM nurse")
        self.connect.commit()

    def get_priority_of_request(self, id):
        params = (id,)
        result = self.cursor.execute(
            '''
            SELECT priority from requests
            WHERE request_id = ?
            ''',params
        ).fetchone()
        if result == None:
            return -1
        return result[0]


    ### NURSE ###
    def insert_nurse(self, nurse):
        params = nurse.nurse_id, nurse.forename, nurse.surname, nurse.email, nurse.password, nurse.location
        self.cursor.execute(
            '''
            INSERT INTO nurse VALUES
            (?, ?, ?, ?, ?, ?)''', params
        )
        self.connect.commit()

    def get_nurse(self, id):
        params = (id,)
        result = self.cursor.execute(
            '''
            SELECT * from nurse
            WHERE nurse_id = ?
            ''',params
        ).fetchone()
        return result


    def remove_nurse(self, id):
        params = (id,)
        self.cursor.execute(
            '''
            DELETE FROM nurse
            WHERE nurse_id = ?''', params
        )
        self.connect.commit()

    def check_nurse(self, id, password): # check if nurseID AND password matches, return boolean 
        params = (id, password)
        password_correct = False
        result = self.cursor.execute(
            '''
            SELECT * from nurse
            WHERE nurse_id = ? AND password = ?''', params
        ).fetchone()

        return result != None

    ### PATIENT ###
    def insert_patient(self, id, forename, surname):
        params = (id, forename, surname)
        self.cursor.execute(
            '''
            INSERT INTO patient VALUES
            (?, ?, ?)''', params
        )
        self.connect.commit()

    def remove_patient(self, id):
        params = (id,)
        self.cursor.execute(
            '''
            DELETE FROM patient
            WHERE patient_id = (?)''', params
        )
        self.connect.commit()

    def check_patient_id(self, id): # check if patientID exists in db, return boolean
        params = (id,)
        patient_exists = False
        patient_id = self.cursor.execute(
            ''' 
            SELECT patient_id from patient
            WHERE patient_id = (?)''', params
        ).fetchone()
        if patient_id != None:
            patient_exists = True
        
        return patient_exists






#TODO add connect.close() to close the database
