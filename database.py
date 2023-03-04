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
            ([request_id] INTERGER, [patient_id] INTEGER, 
            [priority] INTEGER, [type_of_request] TEXT, [location] TEXT)
            '''
        ) #location within hospital (wing, ward...)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS nurse
            ([nurse_id] INTEGER PRIMARY KEY, [forename] TEXT, [surname] TEXT,
              [email] TEXT, [password] TEXT, [location])'''
        ) #location is within hospital (to be able to link to patient)

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
        params = (request.request_id, request.patient_id, request.priority, request.type_of_request, request.location)
        self.cursor.execute("INSERT INTO requests VALUES(?,?,?,?,?)",params)
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

#TODO add connect.close() to close the database
