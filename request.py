class Request:
    """Class for request table"""

    def __init__(self):
        self.request_id = None
        self.patient_id = None
        self.priority = None
        self.type_of_request = None
        self.location = None

    def __getRequest__(self):
        request_info = []
        request_info.append(patient_id)
        request_info.append(type_of_request)
        request_info.append(location)

        return tuple(request_info)                        