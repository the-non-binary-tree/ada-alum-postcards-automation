class Recipient:
    def __init__(self, firstname, lastname, cohort, email):
        self.firstname = firstname
        self.lastname = lastname
        self.cohort = cohort
        self.__email = email

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# mock = Recipient("enby tree", 17, "mockemail")
# print(mock)
