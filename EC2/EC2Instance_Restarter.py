import boto3
import time

def start_ec2_instance(instance_id):
    try:
        # Configure the EC2 client
        ec2 = boto3.client('ec2')

        # Start the EC2 instance
        response = ec2.start_instances(
            InstanceIds=[instance_id]
        )

        # Check the state of the instance after starting
        instances = response['StartingInstances']
        if instances:
            instance = instances[0]
            current_state = instance['CurrentState']['Name']
            previous_state = instance['PreviousState']['Name']
            print(f"Instance '{instance_id}' is starting...")
            print(f"Previous state: {previous_state}")
            print(f"Current state: {current_state}")

            # Wait for the instance to reach a running state
            print("Waiting for instance to start..........")
            waiter = ec2.get_waiter('instance_running')
            waiter.wait(InstanceIds=[instance_id])
            print("Instance started!")

            # Retrieve the updated information of the instance
            response = ec2.describe_instances(InstanceIds=[instance_id])
            instance = response['Reservations'][0]['Instances'][0]
            public_ip_address = instance.get('PublicIpAddress')
            print(f"New Public IP address: {public_ip_address}")
        else:
            print(f"Instance '{instance_id}' is not found or already running.")

    except Exception as e:
        print(f"Failed to start instance '{instance_id}': {str(e)}")

# Usage
instance_id = 'i-050776e8c89980787'  # Specify the EC2 instance ID
start_ec2_instance(instance_id)
