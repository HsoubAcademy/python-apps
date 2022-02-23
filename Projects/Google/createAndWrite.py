import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)

# create new file
# new_file = file.create('A new spreadsheet')
# new_file.share('academyhsoub1@gmail.com', perm_type='user', role='owner')

# open file
new_file = file.open("A new spreadsheet")

# create new sheet
#worksheet = new_file.add_worksheet(title="Sheet2", rows="100", cols="20")

# write to sheet
worksheet = new_file.worksheet("Sheet1")
worksheet.update('B1', 'Hello World!')

worksheet.update_cell(2, 4, 'Hello!')

worksheet.update('A1:c2', [['Hasan', 1000, '14/05/2021'], ['yara', 500, '01/09/2021']])
