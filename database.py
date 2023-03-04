import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connect = None
        self.cursor = None

    def connect_db(self):
        """ Creates a database connection with the SQLite database """
        self.connect = sqlite3.connect(self.db_file)
        self.cursor = self.connect.cursor()

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS requests
            ([request_id] INTERGER PRIMARY KEY, [patient_id] INTEGER, 
            [priority] INTEGER, [type_of_request] TEXT, [location] TEXT)
            '''
        ) #location within hospital (wing, ward...)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXIST nurse
            ([nurse_id] INTEGER PRIMARY KEY, [forename] TEXT, [surname] TEXT,
              [email] TEXT, [password] TEXT, [location] TEXT)'''
        ) #location is within hospital (to be able to link to patient)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXIST patient
            ([patient_id] INTEER PRIMARY KEY, [forename] TEXT, [surname] TEXT)'''
        )


    ### REQUESTS ###
    def get_request(self, id):
            self.cursor.fetchone(id) #FIXME not sure if this is correct

    def remove_request(self, id):
        self.cursor.execute(
            f'''
            DELETE FROM requests
            WHERE request_id = {id}'''
        )
        self.connect.commit()


    def insert_request(self, request):
        self.cursor.execute(
            f'''
            INSERT INTO requests VALUES
            ({request.request_id},{request.patient_id},{request.priority},{request.type_of_request},{request.location})
            '''
        )
        self.connect.commit()

    def change_id_of_request(self,old_id,new_id):
        self.cursor.execute(
            f'''
            UPDATE requests
            SET request_id = {new_id}
            WHERE request_id = {old_id};
            '''
        )
        self.connect.commit()

    def get_priority_of_request(self, id):
        result = self.cursor.execute(
            f'''
            SELECT priority from requests
            WHERE request_id = {id}
            '''
        ).fetchone()
        try:
            return result[0]
        except IndexError:
            print("Oh snap")
            quit()


    ### NURSE ###

    ### PATIENT ###
    def check_patient_id(id): # check if patientID exists in db, return boolean
        params = id
        patient_exists = False
        patient_id = self.cursor.execute(
            ''' 
            SELECT patient_id from patient
            WHERE patient_id = (?)''', params
        )
        if patient_id != "":
            patient_exists = True
        
        return patient_exists

    
    def check_nurse(id, password): # check if nurseID AND password matches, return boolean 
        params = id, password
        nurse_id_exists = False
        password_correct = False
        nurse_id = self.cursor.execute(
            '''
            SELECT nurse_id from nurse
            WHERE nurse_id = (?)''', params[0]
        )
        nurse_password = self.cursor.execute(
            '''
            SELECT password from nurse
            WHERE nurse_id = (?) && password = (?)''', params[0], params[1]
        )

        if nurse_id != "":
            nurse_id_exists = True
        
        if nurse_password != "":
            password_correct = True
        
        return nurse_id_exists & password_correct





#TODO add connect.close() to close the database
