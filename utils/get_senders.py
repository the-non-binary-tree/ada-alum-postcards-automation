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

            fullname = row[columns.index("Your First & Last Name")]
            email = row[columns.index("Your Email Address")]
            postcardNum = int(row[columns.index("How many cards/post cards can you commit to writing?")])

            # instance a Sender
            sender = Sender(
                fullname, email, postcardNum)

            senders.append(sender)

    print('Finish parsing file and filter data.')

'''
Get all alumns who will send a postcard
INPUT:
sources: an array of filepaths
OUTPUT: an array of Sender instances
'''
def get_all_senders():
    senders = list()
    sources = ['/Users/sophiale/sandbox/python/ada-alum-postcards-automation/assets/C17 POSTCARD SIGNUP (Responses) - Form Responses 1.csv']
    for filename in sources:
        parse_file(filename, senders)
    # print(senders)
    return senders