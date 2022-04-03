import sys
from utils.get_recipients import get_remaining_recipients
from utils.get_senders import get_all_senders
from utils.match_sender_recipients import match_all_senders
import constants
import csv
from models.Sender import Sender
from models.Recipient import Recipient

recipients = get_remaining_recipients()

# should be get remaining senders
senders = get_all_senders()

match_all_senders(senders, recipients)

print(senders)

# export to csv
HEADERS = ["Full Name", "Email Address", "Number of Postcards", "List of Assigned Students' Names"]
rows = list()
for sender in senders:
    assigned_recipients = ', '.join([recipient.fullname for recipient in sender.recipients])
    row = [
        sender.fullname,
        sender.email,
        sender.postcardNum,
        assigned_recipients
    ]
    rows.append(row)

with open('C17-Postcard-Matches.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(HEADERS) 
    write.writerows(rows)