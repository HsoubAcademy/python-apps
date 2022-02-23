import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)
file = gspread.authorize(credentials)
sheet = file.open("test").sheet1

sheet.update_cell(2, 1, "Hello World!")