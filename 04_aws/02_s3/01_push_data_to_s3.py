import boto3 
import os

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

try:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    print("Connected to AWS")

    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
    except:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
        )
        print(f'Bucket {BUCKET_NAME} created')
    else:
        print(f'bucket {BUCKET_NAME} already exists')
    
except Exception as e:
    print(f'Failed to create bucket: {e}')


