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
            CREATE TABLE IF NOT EXIST requests
            ([request_id] INTERGER PRIMARY KEY, [patient_id] INTEGER, 
            [priority] INTEGER, [type_of_request] TEXT, [location] TEXT)
            '''
        ) #location within hospital (wing, ward...)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXIST nurse
            ([nurse_id] INTEGER PRIMARY KEY, [forename] TEXT, [surname] TEXT,
              [email] TEXT, [password] TEXT, [location])'''
        ) #location is within hospital (to be able to link to patient)

        def get_priority_request(self):
            self.cursor


        def remove_request(self, id):
            self.cursor.execute(
                f'''
                DELETE FROM requests
                WHERE request_id = {id}'''
            )


        def insert_request(self, request):
        self.cursor.execute(
            f'''
            INSERT INTO requests VALUES
                ({request.request_id},{request.patient_id},{request.priority},{request.type_of_request},{request.location})
            '''
        )
        self.connect.commit()

#TODO add connect.close() to close the database
