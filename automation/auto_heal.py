import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

INSTANCE_ID = "i-031af92c6e017c084"

def restart_instance():
    print("Restarting EC2 instance...")

    response = ec2.reboot_instances(
        InstanceIds=[INSTANCE_ID]
    )

    print("Instance reboot command sent.")

restart_instance()
