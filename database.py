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

#TODO add connect.close() to close the database
