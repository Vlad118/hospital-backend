from database import Database
from priorityqueue import PriorityQueue
from request import Request

class Main: 
    def __init__(self):
        db_file = 'request_and_nurses.db' 
        self.db = Database(db_file)
        self.db.connect_db()
        self.db.clear_requests()
        self.priorityqueue = PriorityQueue(self.db)

    def add_request(self, request):
        self.priorityqueue.insert(request)

    def get_next_request(self):
        return self.priorityqueue.extract_max()
    
    def check_patient_id(self,id):
        return self.db.check_patient_id(id)
    
    def check_nurse(self,id, password):
        return self.db.check_nurse(id,password)
    
    def get_task(self,id):
        return self.get_next_request()
    
    def register_nurse(self, nurse):
        return self.db.insert_nurse(nurse)
    
main = Main()

