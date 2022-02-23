import csv, os
from pathlib import Path

os.makedirs(Path.home() / Path('Desktop', 'CSV files'), exist_ok=True)

for csvFilename in os.listdir(Path.home() / Path('Desktop', 'CSV files')):
     if not csvFilename.endswith('.csv'):
         continue

     print('Removing header from ' + csvFilename + '...')
     csvRows = []
     csvFileObj = open(Path.home() / Path('Desktop', 'CSV files', csvFilename))
     readerObj = csv.reader(csvFileObj)

     for row in readerObj:
         if readerObj.line_num == 1:
             continue  # تخطى السطر الأول
         csvRows.append(row)
     csvFileObj.close()

     csvFileObj = open(Path.home() / Path('Desktop', 'CSV files', csvFilename), 'w', newline='')
     csvWriter = csv.writer(csvFileObj)
     for row in csvRows:
         csvWriter.writerow(row)
     csvFileObj.close()