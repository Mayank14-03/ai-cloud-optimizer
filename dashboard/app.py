from flask import Flask, jsonify, render_template
import boto3
import time

app = Flask(__name__)

# AWS clients (IMPORTANT: regions match your setup)
ec2 = boto3.client('ec2', region_name='us-east-1')
ses = boto3.client('ses', region_name='us-east-1')

# Email cooldown tracker (avoid spam)
last_sent = {}

# ---------------- HOME ROUTE ----------------
@app.route('/')
def home():
    return render_template('index.html')


# ---------------- EMAIL FUNCTION ----------------
def send_email(instance_id, message):
    try:
        ses.send_email(
            Source='kordemayank1@gmail.com',
            Destination={
                'ToAddresses': ['kordemayank1@gmail.com']
            },
            Message={
                'Subject': {'Data': '⚠ EC2 Optimization Alert'},
                'Body': {
                    'Text': {
                        'Data': f'Instance {instance_id}: {message}'
                    }
                }
            }
        )
    except Exception as e:
        print("Email Error:", e)


# ---------------- API ROUTE ----------------
@app.route('/instances')
def get_instances():

    response = ec2.describe_instances()

    instances = []
    running = 0

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:

            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            cpu = 0.5  # dummy (later replace with CloudWatch)

            if state == "running":
                running += 1

            # 🔥 EMAIL ALERT LOGIC
            current_time = time.time()

            if cpu < 1:
                if instance_id not in last_sent or current_time - last_sent[instance_id] > 3600:
                    
                    last_sent[instance_id] = current_time

            if cpu > 80:
                if instance_id not in last_sent or current_time - last_sent[instance_id] > 3600:
                    send_email(instance_id, "High CPU usage detected. Consider scaling.")
                    last_sent[instance_id] = current_time

            instances.append({
                "id": instance_id,
                "state": state,
                "cpu": cpu
            })

    cost = running * 6
    waste = 2

    return jsonify({
        "instances": instances,
        "running": running,
        "cost": cost,
        "waste": waste
    })


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
