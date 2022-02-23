import csv
from pathlib import Path

# add multiple lines
# header = ['Name', 'Salary', 'Date']
# data = [
#     ['Hadi', 1000, '04/08/2021'],
#     ['Sara', 800, '06/04/2021'],
#     ['Reem', 400, '25/02/2020'],
#     ['Yara', 750, '09/07/2020'],
#     ['Anas', 1200, '15/04/2019']
# ]
#
# file = open(Path.home() / Path('Desktop', 'employees.csv'), 'w', newline='')
# writer = csv.writer(file)
# writer.writerow(header)
# writer.writerows(data)
# file.close()

# delimiter and lineterminator Keyword
file = open(Path.home() / Path('Desktop', 'employees.csv'), 'w', newline='')
writer = csv.writer(file, delimiter='\t', lineterminator='\n----------------------------\n')
writer.writerow(['Hadi', 1000, '04/08/2021'])
writer.writerow(['Anas', 1200, '15/04/2019'])
writer.writerow(['Reem', 400, '25/02/2020'])
file.close()