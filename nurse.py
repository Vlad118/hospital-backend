class Nurse:
    def __init__(self):
        self.nurse_id = None
        self.forename = None
        self.surname = None
        self.email = None
        self.password = None
        self.location = None

    def __init__(self, id, forename, surname, email, password, location):
        self.nurse_id = id
        self.forename = forename
        self.surname = surname
        self.email = email
        self.password = password
        self.location = location
