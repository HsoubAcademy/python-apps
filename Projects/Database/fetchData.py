import sqlite3
from pathlib import Path

# Connect
sqliteConnection = sqlite3.connect(Path.home() / Path('Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print("Connected to the database")

crsr.execute("SELECT name,salary,dateOfEmployment FROM employees where salary > 850")
#print(crsr.fetchall())
#print(crsr.fetchone())
#print(crsr.fetchmany(3))

answer = crsr.fetchall()
for i in answer:
    print(i)
