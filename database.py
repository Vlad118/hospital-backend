import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file

    def connect_db(db_file):
        """ Creates a database connection with the SQLite database """
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXIST requests
            ([request_id] INTERGER PRIMARY KEY, [patient_id] INTEGER, 
            [priority] INTEGER, [type_of_request] TEXT, [location] TEXT)
            '''
        ) #location within hospital (wing, ward...)

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXIST nurse
            ([nurse_id] INTEGER PRIMARY KEY, [forename] TEXT, [surname] TEXT,
              [email] TEXT, [password] TEXT, [location])'''
        ) #location is within hospital (to be able to link to patient)

#TODO add connect.close() to close the database
