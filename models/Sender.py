class Sender:
    def __init__(self, firstname, lastname, email, postcardNum, deliveryMethod):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.postcardNum = postcardNum
        self.deliveryMethod = deliveryMethod

    def __repr__(self):
        recipients = '\n'.join(self.recipients) if self.recipients else 'No match yet' 
        return f'''
Full name: {self.firstname} {self.lastname}
Email: {self.email}
Number of Postcards: {self.postcardNum}
Recipients: {recipients}
Delivery Method: {self.deliveryMethod}
        '''

    def setRecipients(self, recipients):
        self.recipients = recipients
