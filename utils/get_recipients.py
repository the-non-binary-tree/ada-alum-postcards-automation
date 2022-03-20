import sys
sys.path.append("/Users/sophiale/sandbox/python/ada-alum-postcards-automation/models")
from Recipient import Recipient
import csv
import random
import os

'''
Iterate through a csv file to get the info of current students
INPUT:
filename: filepath to a csv file
recipients: the array to which info about current students is stored
OUTPUT:
None
'''
def parse_file(filename, recipients):
    print('Starting parsing file:')
    current_cohort = 17 
    with open(filename) as file_raw:
        data_raw = csv.reader(file_raw, delimiter=',')
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

'''
Get all current students who will receive a postcard
INPUT:
sources: filepath of the directory that contains all csv files of current students
OUTPUT: an array of Recipient instances
'''
def get_all_recipients(sources):
    recipients = list()
    directory = os.fsencode(sources)
    for csvFile in os.listdir(directory):
        filename = os.fsdecode(csvFile)
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, csvFile)
            parse_file(filepath, recipients)

    random.shuffle(recipients)
    print(len(recipients))
    return recipients

