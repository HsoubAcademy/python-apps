import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)

sheet = file.open("example").sheet1

# find
cell = sheet.findall("Hadi")
print(cell)
#print("Found something at Row: %s and Column: %s" % (cell.row, cell.col))

employess = re.compile(r'(Anas|Sara)')
cell = sheet.findall(employess)
print(cell)

# clear
sheet.batch_clear(["A8:C8"])

sheet.clear()
