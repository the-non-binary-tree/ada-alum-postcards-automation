class Recipient(object):
    def __init__(self, fullname, cohort, email):
        self.fullname = fullname
        self.cohort = cohort
        self.__email = email