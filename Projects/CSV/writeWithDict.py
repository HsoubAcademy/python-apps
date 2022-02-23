import csv
from pathlib import Path

# file = open(Path.home() / Path('Desktop', 'employees.csv'), 'a', newline='')
# DictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'], delimiter=';')
# DictWriter.writerow({'Name': 'Ali', 'Salary': '1500', 'Date': '04/09/2021'})
# file.close()

file = open(Path.home() / Path('Desktop', 'employees_test.csv'), 'w', newline='')
DictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'])
DictWriter.writeheader()

DictWriter.writerow({'Name': 'Reem', 'Salary': '1500', 'Date': '04/09/2021'})
DictWriter.writerow({'Salary': '1000', 'Name': 'Hadi', 'Date': '04/09/2021'})
file.close()