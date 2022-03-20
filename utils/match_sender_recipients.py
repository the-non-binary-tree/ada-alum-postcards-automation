import sys
sys.path.append("/Users/sophiale/sandbox/python/ada-alum-postcards-automation/models")
from Recipient import Recipient
from Sender import Sender
import random

'''
Set recipients for one Sender instance
INPUT:
sender: one Sender instance
recipients: an array of all Recipient instances whom currently was not assigned to a Sender
OUTPUT:
None
'''
def get_recipients_for_one_sender(sender, recipients):
    postcardNum = sender.postcardNum
    if len(recipients) <= postcardNum:
        sender.setRecipients(recipients)
        recipients.clear()
    else:
        random.shuffle(recipients)
        pickRecipients = list()
        for _ in range(postcardNum + 1):
            cur = recipients.pop()
            pickRecipients.append(cur)

        sender.setRecipients(pickRecipients)

'''
Set recipients for all instances of Sender
INPUT:
senders: an array of all instances of Sender
recipients: an array of all instances of Recipient
OUTPUT:
None
'''
def match_all_senders(senders, recipients):
    for sender in senders:
        get_recipients_for_one_sender(sender, recipients)
