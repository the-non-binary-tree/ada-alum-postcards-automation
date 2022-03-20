class Recipient:
    def __init__(self, fullname, cohort, email):
        self.fullname = fullname
        self.cohort = cohort
        self.__email = email

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# mock = Recipient("enby tree", 17, "mockemail")
# print(mock)
