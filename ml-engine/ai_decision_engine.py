import boto3
import joblib
from datetime import datetime, timedelta

INSTANCE_ID = "i-031af92c6e017c084"

# Load AI model
model = joblib.load("cpu_model.pkl")

cloudwatch = boto3.client("cloudwatch", region_name="us-east-1")
ec2 = boto3.client("ec2", region_name="us-east-1")

response = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[{"Name": "InstanceId", "Value": INSTANCE_ID}],
    StartTime=datetime.utcnow() - timedelta(minutes=10),
    EndTime=datetime.utcnow(),
    Period=300,
    Statistics=["Average"]
)

datapoints = response["Datapoints"]

if datapoints:

    cpu = datapoints[-1]["Average"]
    prediction = model.predict([[cpu]])

    print("Current CPU:", cpu)
    print("Predicted CPU:", prediction[0])

    if prediction[0] < 20:

        print("Low usage detected → stopping instance")

        ec2.stop_instances(
            InstanceIds=[INSTANCE_ID]
        )

        print("Instance stopped to save cost")

    elif prediction[0] > 70:

        print("High load detected → scaling required")

    else:

        print("Server running normally")

else:
    print("No CPU data found")
