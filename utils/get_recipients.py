import sys
sys.path.append("/Users/sophiale/sandbox/python/ada-alum-postcards-automation/models")
from Recipient import Recipient
import csv

def parse_file(filename, recipients):
    print('Starting parsing file:')
    current_cohort = 17 
    with open(filename) as file_raw:
        print(f'Opening file {filename}')
        data_raw = csv.reader(file_raw, delimiter=',')
        print('Iterating over each line in the file:')
        firstline = True
        columns = list()
        for row in data_raw:
            if firstline:
                columns = row
                firstline = False
                continue

            firstname = row[columns.index("First Name")]
            lastname = row[columns.index("Last Name")]
            email = row[columns.index("Email")]

            # instance a Recipient
            recipient = Recipient(
                firstname, lastname, current_cohort, email)

            recipients.append(recipient)

    print('Finish parsing file and filter data.')

def get_all_recipients():
    sources = [
        "/Users/sophiale/sandbox/python/ada-alum-postcards-automation/assets/Full Campus View-Grid view (1).csv",
        "/Users/sophiale/sandbox/python/ada-alum-postcards-automation/assets/Full Campus View-Grid view.csv"
    ]
    recipients = list()
    for filename in sources:
        parse_file(filename, recipients)

    return recipients
