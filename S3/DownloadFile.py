import boto3
import os

def download_file_from_s3(uri, directory):
    # Parse the S3 URI
    bucket_name, object_key = parse_s3_uri(uri)

    # Create an S3 client
    s3_client = boto3.client('s3')

    # Download the file from S3
    file_name = os.path.basename(object_key)
    file_path = os.path.join(directory, file_name)
    s3_client.download_file(bucket_name, object_key, file_path)

    print(f'S3 file "{uri}" downloaded to local path: {file_path}')

def parse_s3_uri(uri):
    # Remove the 's3://' prefix from the S3 URI
    uri_without_prefix = uri[5:]

    # Split the URI into bucket name and object key
    parts = uri_without_prefix.split('/', 1)
    bucket_name = parts[0]
    object_key = parts[1] if len(parts) > 1 else ''

    return bucket_name, object_key

# Prompt the user for the S3 URI and directory
s3_uri = r"s3://sam-programmed-bucket/521476.jpg"
directory = r"C:\Users\samue\OneDrive\Desktop\Vokamancy\S3\S3_Downloads"

# Run the download function
download_file_from_s3(s3_uri, directory)
