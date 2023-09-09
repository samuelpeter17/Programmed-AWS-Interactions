import boto3
import time

def create_ec2_instance(instance_name, security_group_id,region_name):
    try:
        # Configure the EC2 client
        ec2 = boto3.client('ec2',region_name=region_name)

        # Create a new key pair
        key_pair_name = f"{instance_name}-keypair"
        response = ec2.create_key_pair(KeyName=key_pair_name)
        private_key = response['KeyMaterial']

        # Save the private key to a file
        key_pair_path = f"{key_pair_name}.pem"
        with open(key_pair_path, 'w') as key_file:
            key_file.write(private_key)
        # Set appropriate permissions on the key pair file
        import os
        os.chmod(key_pair_path, 0o400)
        print(f"Security key pair '{key_pair_name}' generated and saved as '{key_pair_path}'")

        # Launch the EC2 instance
        instance = ec2.run_instances(
            ImageId='ami-07dfed28fcf95241c',  # Specify the AMI ID
            InstanceType='t2.micro',  # Specify the instance type
            MinCount=1,
            MaxCount=1,
            KeyName=key_pair_name,
            SecurityGroupIds=[security_group_id],  # Add the specified security group
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        }
                    ]
                }
            ]
        )

        instance_id = instance['Instances'][0]['InstanceId']
        print(f"EC2 instance '{instance_id}' with name '{instance_name}' created and added to security group '{security_group_id}'.")

        # Wait for the instance to reach a running state
        print("Waiting for instance to start...")
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        print("Instance started!")

        # Retrieve the public IP address of the instance
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance_public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        print(f"Public IP address: {instance_public_ip}")

    except Exception as e:
        print(f"Failed to create EC2 instance '{instance_name}': {str(e)}")

# Usage
instance_name = 'S3Upload_Instance'  # Specify the desired instance name
security_group_id = 'sg-0db25b4bac0a42208'  # Specify the security group ID, currently SSH_In security group
region_name = 'us-west-2'
create_ec2_instance(instance_name, security_group_id,region_name)