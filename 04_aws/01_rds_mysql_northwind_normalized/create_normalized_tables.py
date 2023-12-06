import os
import mysql.connector
from time import sleep

#getting local variables
db_config = {
    'host': os.environ['rds_host'],
    'user': os.environ['rds_user'],
    'password': os.environ['rds_password'],
    'database': os.environ['rds_database']
}

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        
        sql_statement = file.read()
        cursor.execute(sql_statement)
        sleep(1)

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

sql_directory = r'04_aws\01_rds_mysql_northwind_normalized\sql_files'

execute_sql_files_in_directory(sql_directory)

