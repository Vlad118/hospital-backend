import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.cursor = None

    def connect_db(self, db_file):
        """ Creates a database connection with the SQLite database """
        connect = sqlite3.connect(db_file)
        self.cursor = connect.cursor()

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

    def insert(self, ID, request):
        self.cursor.execute()

#TODO add connect.close() to close the database
