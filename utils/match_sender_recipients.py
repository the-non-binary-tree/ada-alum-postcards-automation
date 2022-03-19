import sys
sys.path.append("/Users/sophiale/sandbox/python/ada-alum-postcards-automation/models")
from Recipient import Recipient
from Sender import Sender

'''

'''
def get_recipients_for_one_sender(sender, recipients):
    postcardNum = sender.postcardNum
    if len(recipients) <= postcardNum:
        sender.setRecipients(recipients)
    else:
        pickRecipients = list()
        for _ in range(postcardNum + 1):
            cur = recipients.pop()
            pickRecipients.append(cur)

        sender.setRecipients(pickRecipients)


def match_all_senders(senders, recipients):
    for sender in senders:
        get_recipients_for_one_sender(sender, recipients)