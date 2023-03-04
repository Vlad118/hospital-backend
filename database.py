import sqlite3
from sqlite3 import Error

class Database():

    def connect_db(db_file):
        """ Creates a database connection with the SQLite database """
        connect = None
        try:
            connect = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as err:
            print(err)
        finally:
            if connect:
                connect.close()

#TODO add connect.close() to close the database
