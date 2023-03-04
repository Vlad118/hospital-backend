class Request:
    """Class for request table"""

    def __init__(self):
        self.request_id = None
        self.patient_id = None
        self.priority = None
        self.type_of_request = None
        self.location = None

    def __getRequest__(self):
        return self.patient_id, self.type_of_request, self.location