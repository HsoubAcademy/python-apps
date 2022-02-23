import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)

new_file = file.open("example")

worksheet = new_file.worksheet("Sheet1")

worksheet.update_cell(8, 2, "=AVERAGE(B2:B7)")

cell = worksheet.acell('B8', value_render_option='FORMULA').value
print(cell)