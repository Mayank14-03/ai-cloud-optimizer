import boto3
from datetime import datetime, timedelta

REGION = "us-east-1"

ec2 = boto3.client('ec2', region_name=REGION)
cloudwatch = boto3.client('cloudwatch', region_name=REGION)
ses = boto3.client('ses', region_name=REGION)

CPU_THRESHOLD = 10

SENDER = "kordemayank1@gmail.com"
RECEIVER = "kordemayank1@gmail.com"

def send_email(instance_id, cpu):

    subject = "EC2 Instance Auto-Stopped"

    body = f"""
Instance ID: {instance_id}

CPU Usage: {cpu:.2f}%

Action: Instance automatically stopped by AI Cloud Optimizer.
"""

    try:
        response = ses.send_email(
            Source=SENDER,
            Destination={
                'ToAddresses': [RECEIVER]
            },
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body}
                }
            }
        )

        print("Email sent successfully")
        print(response)

    except Exception as e:
        print("Email sending failed")
        print(e)


def get_cpu(instance_id):

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {'Name': 'InstanceId', 'Value': instance_id}
        ],
        StartTime=datetime.utcnow() - timedelta(minutes=60),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )

    datapoints = response['Datapoints']

    if len(datapoints) == 0:
        return 0

    avg = sum(d['Average'] for d in datapoints) / len(datapoints)

    return avg


def check_instances():

    reservations = ec2.describe_instances()

    for r in reservations['Reservations']:
        for i in r['Instances']:

            instance_id = i['InstanceId']
            state = i['State']['Name']

            if state != "running":
                continue

            cpu = get_cpu(instance_id)

            print(f"Instance {instance_id} CPU: {cpu:.2f}%")

            if cpu < CPU_THRESHOLD:

                print("Low CPU detected → Stopping instance")

                ec2.stop_instances(InstanceIds=[instance_id])

                send_email(instance_id, cpu)


check_instances()
