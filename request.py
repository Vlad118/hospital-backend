class Request:
    """Class for request table"""

    def __init__(self):
        self.request_id = None
        self.patient_id = None
        self.priority = None
        self.type_of_request = None
        self.location = None
        self.extra_info = None

    def __init__(self,requestid, patientid, priority, type, location, extrainfo): 
        self.request_id = requestid
        self.patient_id = patientid
        self.priority = priority
        self.type_of_request = type
        self.location = location
        self.extra_info = extrainfo