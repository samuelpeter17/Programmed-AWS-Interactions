import os
import boto3
from botocore.exceptions import ClientError

def upload_directory_to_s3(local_path, bucket_name):
    s3_client = boto3.client('s3')

    for root, dirs, files in os.walk(local_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_file_path, local_path)
            s3_object_key = os.path.join(bucket_name, s3_key)

            try:
                s3_client.upload_file(local_file_path, bucket_name, s3_key)
                print(f'Uploaded {local_file_path} to S3 object key: {s3_object_key}')
            except ClientError as e:
                print(f'Error uploading {local_file_path} to S3: {e}')

# Example usage:
local_directory = '/home/ec2-user/toS3'
s3_bucket_name = 'ec2-s3interactions-bucket'

upload_directory_to_s3(local_directory, s3_bucket_name)