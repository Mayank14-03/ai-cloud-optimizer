import boto3
import pandas as pd
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

INSTANCE_ID = "i-031af92c6e017c084"

end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=6)

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {'Name': 'InstanceId', 'Value': INSTANCE_ID}
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=['Average']
)

data = []

for point in response['Datapoints']:
    data.append({
        "timestamp": point['Timestamp'],
        "cpu_usage": point['Average']
    })

df = pd.DataFrame(data)

df = df.sort_values("timestamp")

df.to_csv("cpu_dataset.csv", index=False)

print("Dataset saved as cpu_dataset.csv")
