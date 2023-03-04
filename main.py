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
    
main = Main()
request = Request()
request.patient_id = 100
request.priority = 10


r2 = Request()
r2.patient_id = 200
r2.priority = 20

r3 = Request()
r3.priority = 15
r3.patient_id = 30

main.add_request(request)
main.add_request(r2)
main.add_request(r3)

print(main.get_next_request())
print(main.get_next_request())
print(main.get_next_request())



