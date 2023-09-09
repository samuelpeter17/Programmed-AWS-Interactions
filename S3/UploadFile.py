import boto3
import botocore.exceptions

def upload_file_to_s3(file_path, bucket_arn):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Extract the bucket name from the bucket ARN
    bucket_name = bucket_arn.split(':::')[-1]

    try:
       # Upload the file to the S3 bucket
        parts = file_path.split('\\')
        file_name = parts[len(parts)-1]
        s3.upload_file(file_path, bucket_name, file_name)

        print(f'File "{file_path}" uploaded to S3 bucket "{bucket_name}".')
    except botocore.exceptions.ClientError as e:
        error_message = e.response['Error']['Message']
        print(f'Error uploading file to S3 bucket: {error_message}')


# Prompt the user for the file path and bucket ARN
file_path = r"C:\Users\samue\OneDrive\Pictures\Saved Pictures\FoY7zYoWIAkFCEG.png"
bucket_arn = 'arn:aws:s3:::sam-programmed-bucket'

upload_file_to_s3(file_path, bucket_arn)