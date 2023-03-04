import math

class PriorityQueue:
    """Priority Queue implemented as a max heap"""
    def __init__(self, db):
        self.db = db
        self.size = 0

    def left(self,i):
        """Returns ID of left child"""
        return i * 2 + 1
    
    def right(self,i):
        """Returns ID of right child"""
        return i * 2 + 2
    
    def parent(self,i):
        """Returns ID of parent"""
        return math.floor((i-1)/2)
    
    def switch_nodes(self,i,j):
        """Switches ID of nodes at index i and j"""
        self.db.change_ID_of_request(i,-1)
        self.db.change_ID_of_request(j,i)
        self.db.change_ID_of_request(-1,i)
 
    def extract_max(self):
        """Returns request with highest priority"""
        request = self.db.get_request(0)
        self.db.remove_request(0)
        self.db.change_id_of_request(self.size-1,0)
        self.max_heapify(0)
        return request

    def insert(self, request):
        """Adds new request to DB and priority queue"""
        self.size += 1
        request.request_id = self.size - 1
        self.db.insert_request(request) # add request to DB with ID self.size-1

        j = self.size - 1
        while (j != 0 and self.db.get_priority_of_request(j) > self.db.get_priority_of_request(self.parent(j))):
            self.switch_nodes(j,self.parent(j))
            j = self.parent(j)

    # This is not used, but I thought Mary would enjoy ;)
    def max_heapify(self, i):
        """Maintains maxheap property when violation occurs"""
        l = self.left(i)
        r = self.right(i)
        largest = i

        priority_l = self.db.get_priority_of_request(l)
        priority_r = self.db.get_priority_of_request(r)
        priority_i = self.db.get_priority_of_request(i)

        priority_largest = priority_i

        if l < self.size and priority_l > priority_i:
            largest = l
            priority_largest = priority_l
        
        if r < self.size and priority_r > priority_largest:
            largest = r
            priority_largest = priority_r

        if largest != i:
            self.switch_nodes(i,largest)
            self.max_heapify(largest)
