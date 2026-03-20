import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-031af92c6e017c084'
        },
    ],
    StartTime='2026-03-13T00:00:00',
    EndTime='2026-03-13T23:59:59',
    Period=300,
    Statistics=['Average'],
)

print(response)
