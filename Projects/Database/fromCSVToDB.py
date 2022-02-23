import sqlite3
import csv
from pathlib import Path

# Connect
sqliteConnection = sqlite3.connect(Path.home() / Path('Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print("Connected to the database")

# Create Table
sql_command = """CREATE TABLE if not exists employees ( 
id INTEGER,
Name VARCHAR(20), 
Salary INTEGER, 
dateOfEmployment TEXT)"""

crsr.execute(sql_command)

# read file
file = open(Path.home() / Path('Desktop', 'employees.csv'))
rows = csv.reader(file)

# add data to table
crsr.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", rows)

sqliteConnection.commit()
sqliteConnection.close()