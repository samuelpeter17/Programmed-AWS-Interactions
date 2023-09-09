import boto3
#Things needed
#1. Instance ID @ Line 30

def stop_ec2_instance(instance_id):
    try:
        # Configure the EC2 client
        ec2 = boto3.client('ec2')

        # Stop the EC2 instance
        response = ec2.stop_instances(
            InstanceIds=[instance_id]
        )

        stopping_instances = response['StoppingInstances']
        if stopping_instances:
            instance = stopping_instances[0]
            current_state = instance['CurrentState']['Name']
            previous_state = instance['PreviousState']['Name']
            print(f"Instance '{instance_id}' is in the process of stopping.")
            print(f"Previous state: {previous_state}")
            print(f"Current state: {current_state}")
        else:
            print(f"Instance '{instance_id}' is not found or already stopped.")
        
    except Exception as e:
        print(f"Failed to stop instance '{instance_id}': {str(e)}")

# Usage
instance_id = 'i-050776e8c89980787'  # Specify the EC2 instance ID
stop_ec2_instance(instance_id)