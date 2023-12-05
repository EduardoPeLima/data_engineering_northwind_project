import boto3
import os
import csv
import mysql.connector
import re
from datetime import datetime

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_CODE')
SECRET_KEY = os.getenv('AWS_SECRET_KEY_CODE')
BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

db_config = {
    'host': os.environ['rds_host'],
    'user': os.environ['rds_user'],
    'password': os.environ['rds_password'],
    'database': os.environ['rds_database']
}

def lambda_handler(event, context):
    
    key = None
    
    for record in event['Records']:
        key = record['s3']['object']['key']
        
    connection = mysql.connector.connect(**db_config)
    
    rds_target_table = re.sub(r'[^a-zA-Z]', '', key).replace('csv','').capitalize()
    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    def get_s3_client():
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
        )
        print("Connected to AWS")
        return s3_client
    
    def get_csv_key_data_body(s3_client):
        object = s3_client.get_object(Bucket=BUCKET_NAME, Key=key)
        return object['Body']
    
    def insert_object_to_rds_target(keyDataBody):
        dataContent = keyDataBody.read().decode('utf-8').splitlines()
        csvContent = csv.reader(dataContent)
        next(csvContent) #skip csv head
    
    
        try:
            cursor = connection.cursor()
    
            for line in csvContent:
                placeholders = ', '.join(['%s' for _ in range(len(line)+2)]) #adding columns na_file_name and dt_extract_data
                sql = f"INSERT INTO {rds_target_table} VALUES ({placeholders})"
                val = []
                for i in line:
                    val.append(i)
                
                val.append(current_date)
                val.append(key)
                cursor.execute(sql, val)
            connection.commit()
            print(f'All rows from s3 object "{key}" were inserted into rds table: {rds_target_table}')
        except Exception as e:
            print('Error in insert process: ' + e)
        finally:
            connection.close()
        
    
    s3_client = get_s3_client()
    keyDataBody = get_csv_key_data_body(s3_client)
    insert_object_to_rds_target(keyDataBody)

    return 'Success'