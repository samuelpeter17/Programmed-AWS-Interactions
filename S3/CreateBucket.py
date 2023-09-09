import boto3

def create_s3_bucket(bucket_name, location):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Create the S3 bucket with bucket versioning enabled
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': location}
    )

    # Enable bucket versioning
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )

    bucket_link = response['Location']
    bucket_arn = f"arn:aws:s3:::{bucket_name}"
    print(f'S3 bucket "{bucket_name}" created with versioning enabled.')
    print(f'Bucket ARN: {bucket_arn}')
    print(f'Bucket Link: {bucket_link}')


# Enter bucket name and location
bucket_name = 'autoec2-upload'      #lowercase, numbers, - and . allowed
location = 'us-west-2'

create_s3_bucket(bucket_name, location)