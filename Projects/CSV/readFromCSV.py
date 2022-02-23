import csv
from pathlib import Path

file = open(Path.home() / Path('Desktop', 'employees.csv'))
reader = csv.reader(file)

# data = list(reader)
# print(data)
# print(data[1][0])
# print(data[1][1])
# print(data[1][2])

for row in reader:
    print('Row #' + str(reader.line_num) + ' ' + str(row))