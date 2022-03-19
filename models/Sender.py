class Sender:
    def __init__(self, fullname, email, postcardNum, deliveryMethod):
        self.fullname = fullname
        self.email = email
        self.postcardNum = postcardNum
        self.deliveryMethod = deliveryMethod

    def matchRecipients(self, recipients):
        if len(recipients) <= self.postcardNum:
            self.recipients = recipients
        else:
            self.recipients = recipients[:self.postcardNum + 1]
