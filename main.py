from database import Database
from priorityqueue import PriorityQueue
from request import Request
from nurse import Nurse

class Main: 
    def __init__(self, cleardbs=False):
        db_file = 'request_and_nurses.db' 
        self.db = Database(db_file)
        self.db.connect_db()

        if(cleardbs):
            self.db.clear_requests()
            self.db.clear_nurses()
            self.db.clear_patients()
        self.priorityqueue = PriorityQueue(self.db)

    def add_request(self, request):
        self.priorityqueue.insert(request)

    def get_next_request(self):
        return Request(*self.priorityqueue.extract_max())
    
    def check_patient_id(self,id):
        return self.db.check_patient_id(id)
    
    def check_nurse(self,id, password):
        return self.db.check_nurse(id,password)
    
    def get_task(self,id):
        return self.get_next_request()
    
    def get_nurse_info(self, id):
        nurse_record = self.db.get_nurse(id)
        return Nurse(*nurse_record)
    
    def register_nurse(self, nurse):
        return self.db.insert_nurse(nurse)
    
    def register_patient(self,id,forename, surname):
        return self.db.insert_patient(id,forename,surname)
    
    def get_priority_from_type(self, type):
        if type == "FOOD":
            return 1
        if type == "WATER":
            return 3
        if type == "TOILET":
            return 5
        if type == "PAINKILLERS":
            return 5
        if type == "DYING":
            return 10
    
main = Main(cleardbs=True)

