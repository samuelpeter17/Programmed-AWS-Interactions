import boto3

def terminate_ec2_instance(instance_id):
    try:
        # Configure the EC2 client
        ec2 = boto3.client('ec2')

        # Terminate the EC2 instance
        response = ec2.terminate_instances(
            InstanceIds=[instance_id]
        )

        # Check the state of the instance after termination
        instances = response['TerminatingInstances']
        if instances:
            instance = instances[0]
            current_state = instance['CurrentState']['Name']
            previous_state = instance['PreviousState']['Name']
            print(f"Instance '{instance_id}' is terminating...")
            print(f"Previous state: {previous_state}")
            print(f"Current state: {current_state}")

            # Wait for the instance to be terminated
            waiter = ec2.get_waiter('instance_terminated')
            waiter.wait(InstanceIds=[instance_id])
            print("Instance terminated!")
            send_termination_notification(instance_id)  # Send termination notification
        else:
            print(f"Instance '{instance_id}' is not found or already terminated.")

    except Exception as e:
        print(f"Failed to terminate instance '{instance_id}': {str(e)}")

def send_termination_notification(instance_id):
    # TODO: Implement your code to send a termination notification, such as an email or notification to a messaging service
    print(f"''I'll be back''-Terminator")

# Usage
instance_id = 'i-0e768b4eb6a4c16c3'  # Specify the EC2 instance ID
terminate_ec2_instance(instance_id)
