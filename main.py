from database import Database
from priorityqueue import PriorityQueue

class Main: 
    def __init__(self):
        db_file = ... #TODO
        self.db = Database(db_file)
        self.priorityqueue = PriorityQueue(self.db)

    def add_request(self, request):
        self.priorityqueue.insert(request)

    def get_next_request(self):
        return self.priorityqueue.extract_max()
