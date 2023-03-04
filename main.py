from database import Database
from priorityqueue import PriorityQueue
from request import Request

class Main: 
    def __init__(self):
        db_file = 'request_and_nurses.db' 
        self.db = Database(db_file)
        self.db.connect_db()
        self.priorityqueue = PriorityQueue(self.db)

    def add_request(self, request):
        self.priorityqueue.insert(request)

    def get_next_request(self):
        return self.priorityqueue.extract_max()
    
main = Main()
request = Request()
request.patient_id = 1
request.priority = 1

r2 = Request()
r2.priority = 2

main.add_request(request)
main.add_request(r2)

print(main.get_next_request())
input()

