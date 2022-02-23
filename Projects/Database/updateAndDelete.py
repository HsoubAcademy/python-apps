import sqlite3
from pathlib import Path

# Connect
sqliteConnection = sqlite3.connect(Path.home() / Path('Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print("Connected to the database")

# Updating
crsr.execute('UPDATE employees SET Salary = 600 WHERE id=6')


# Deleting
crsr.execute('DELETE FROM employees WHERE id=3')

sqliteConnection.commit()
sqliteConnection.close()