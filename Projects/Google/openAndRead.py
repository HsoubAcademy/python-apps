import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)
#sheet = file.open("example")
sheet = file.open_by_url('https://docs.google.com/spreadsheets/d/1LASqWpgSXrfFElWcoIJjAzHq9jAH_L3JF-GYczcnwgI/edit?usp=sharing')

#worksheet = sheet.get_worksheet(0)
worksheet = sheet.worksheet("Sheet1")
worksheet_list = sheet.worksheets()
print(worksheet_list)

#read from sheet
val = worksheet.acell('B1').value
print(val)

val = worksheet.acell('A5').value
print(val)

val = worksheet.cell(5,1).value
print(val)

values_list = worksheet.row_values(2)
print(values_list)

values_list = worksheet.col_values(1)
print(values_list)

list_of_lists = worksheet.get_all_values()
print(list_of_lists)

list_of_dicts = worksheet.get_all_records()
print(list_of_dicts)