import sys
from utils.get_recipients import get_all_recipients
import constants

student_directory = constants.STUDENT_DIRECTORY
print(student_directory)
all_students = get_all_recipients(student_directory)

print(all_students)