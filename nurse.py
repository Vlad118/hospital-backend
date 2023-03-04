class Nurse:
    def __init__(self):
        self.nurse_id = None
        self.forename = None
        self.surname = None
        self.email = None
        self.password = None
        self.location = None

    def __getNurse__(self):
        return self.forename, self.surname