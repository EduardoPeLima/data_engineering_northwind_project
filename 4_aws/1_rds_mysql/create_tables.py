import os
import mysql.connector

db_config = {
    'host': 'your_mysql_host',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'your_database_name',
}

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_statements = file.read().split(';')

        for statement in sql_statements:
            if statement.strip():
                cursor.execute(statement)

def execute_sql_files_in_directory(directory_path):
    connection = mysql.connector.connect(**db_config)

    try:
        cursor = connection.cursor()

        for filename in os.listdir(directory_path):
            if filename.endswith(".sql"):
                file_path = os.path.join(directory_path, filename)
                print(f"Executing SQL statements from: {file_path}")
                execute_sql_file(cursor, file_path)

        connection.commit()
        print("All SQL files executed successfully!")

    finally:
        connection.close()

sql_directory = 'sql_files'

execute_sql_files_in_directory(sql_directory)
