class Request:
    """Class for request table"""

    def __init__(self):
        self.request_id = None
        self.patient_id = None
        self.priority = None
        self.type_of_request = None
        self.location = None

    def __init__(self,requestid, patientid, priority, type, location): 
        self.request_id = requestid
        self.patient_id = patientid
        self.priority = priority
        self.type_of_request = type
        self.location = location

    def __getRequest__(self):
        return self.patient_id, self.type_of_request, self.location