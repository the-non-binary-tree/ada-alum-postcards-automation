import sys
sys.path.append("/Users/sophiale/sandbox/python/ada-alum-postcards-automation/models")
from Sender import Sender
import csv

'''
Iterate through a csv file to get the info of senders
INPUT:
filename: filepath to a csv file
senders: the array to which info about senders is stored
OUTPUT:
None
'''
def parse_file(filename, senders):
    print('Starting parsing file:')
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
            postcardNum = row[columns.index("Number of Postcards")]
            deliveryMethod = row[columns.index("Delivery Method")]

            # instance a Sender
            sender = Sender(
                firstname, lastname, email, postcardNum, deliveryMethod)

            senders.append(sender)

    print('Finish parsing file and filter data.')

'''
Get all alumns who will send a postcard
INPUT:
sources: array of filepaths
OUTPUT: array of Sender instances
'''
def get_all_senders(sources):
    senders = list()
    for filename in sources:
        parse_file(filename, senders)

    return senders
