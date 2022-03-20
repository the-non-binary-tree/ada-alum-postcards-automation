class Sender:
    def __init__(self, fullname, email, postcardNum):
        self.fullname = fullname
        self.email = email
        self.postcardNum = postcardNum
        self.recipients = []

    def __repr__(self):
        recipients = 'No match yet'
        if self.recipients:
            recipients = str()
            recipient_names = [recipient.fullname for recipient in self.recipients]
            recipients = ', '.join(recipient_names)
        return f'''
Full name: {self.fullname}
Email: {self.email}
Number of Postcards: {self.postcardNum}
Recipients: {recipients}
        '''

    def setRecipients(self, recipients):
        self.recipients = recipients
