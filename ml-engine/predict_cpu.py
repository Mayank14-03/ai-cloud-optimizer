import boto3
import joblib
from datetime import datetime, timedelta

# Load trained model
model = joblib.load("cpu_model.pkl")

# Connect to CloudWatch
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId', 'Value': 'i-031af92c6e017c084'}],
    StartTime=datetime.utcnow() - timedelta(minutes=10),
    EndTime=datetime.utcnow(),
    Period=300,
    Statistics=['Average']
)

datapoints = response['Datapoints']

if datapoints:
    cpu = datapoints[-1]['Average']

    prediction = model.predict([[cpu]])

    print("Current CPU:", cpu)
    print("Predicted CPU:", prediction[0])

    if prediction[0] < 20:
        print("Server underutilized → Consider stopping instance")

    elif prediction[0] > 70:
        print("High load detected → Consider scaling")

    else:
        print("Server running optimally")

else:
    print("No CPU data found")
