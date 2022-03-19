import csv
from models import Recipient

def parse_file(filename):
    print('Starting parsing file:')
    current_cohort = 17
    list_of_current_students_to_receive_postcards = list()
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

            fullname = row[columns.index('Full Name')]
            email = row[columns.index('Email')]

            # instance a Recipient
            recipient = models.Recipient(
                fullname, current_cohort, email)

            list_of_current_students_to_receive_postcards.append(recipient)

    print('Finish parsing file and filter data.')
    print(f'Number of students in C{current_cohort} is {len(list_of_current_students_to_receive_postcards)}')
    return list_of_current_students_to_receive_postcards


parse_file('../assets/Full Campus View-Grid view.csv')

