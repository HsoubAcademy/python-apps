import sqlite3
from pathlib import Path

message = """
"a" => Add New Task
"d" => Delete A Task
"s" => Show All Task
"u" => Update A Task
"q" => Quit The App
Please choose an option:
"""

user_input = input(message).strip().lower()

# Command List
commands_list = ["a", "d", "s", "u", "q"]

user_id = 2

try:
  # Connect to DB
  sqliteConnection = sqlite3.connect(Path.home() / Path('Desktop', 'todoAPP.db'))
  crsr = sqliteConnection.cursor()

except:
  print("connection error")

finally:
    if (sqliteConnection):
        # Create Table
        sql_command = """CREATE TABLE if not exists tasks ( 
        user_id INTEGER, 
        task_name VARCHAR(20), 
        description TEXT)"""
        crsr.execute(sql_command)


        def show_tasks():
            crsr.execute(f"SELECT * FROM tasks WHERE user_id = '{user_id}'")

            results = crsr.fetchall()

            print(f"You have {len(results)} tasks")

            if len(results) > 0:
                for task in results:
                    print(f"Task Name: {task[1]} AND", end=" ")
                    print(f"Task Description: {task[2]}")

            sqliteConnection.commit()


        def add_task():
            task_name = input("Write Task Name: ").strip()
            des = input("Write The Task Description: ").strip()

            crsr.execute(f"INSERT INTO tasks (user_id, task_name, description) VALUES ('{user_id}', '{task_name}', '{des}')")

            sqliteConnection.commit()


        def delete_task():
            task_name = input("Write The Task Name You Want To Delete: ").strip()

            crsr.execute(f"DELETE FROM tasks where task_name='{task_name}' and user_id='{user_id}'")
            sqliteConnection.commit()


        def update_task():
            task_name = input("Write The Name Of The Task You Want To Modify: ").strip()
            crsr.execute(f"SELECT * FROM tasks WHERE task_name = '{task_name}' AND user_id='{user_id}'")
            results = crsr.fetchall()

            if not results:
                print("There is no task with this name")

            else:
                des = input("Write The New Task Description: ").strip()
                crsr.execute(
                    f"UPDATE tasks SET description = '{des}' WHERE task_name = '{task_name}' AND user_id = '{user_id}'")

                sqliteConnection.commit()

                print("The task has been successfully modified")


        def end_app():
            print("Program closed")
            exit()


        if user_input in commands_list:

            if user_input == "s":
                show_tasks()

            elif user_input == "a":
                add_task()

            elif user_input == "d":
                delete_task()

            elif user_input == "u":
                update_task()

            else:
                end_app()

        else:
            print("Sorry This Command Is Not Found")

    sqliteConnection.close()
