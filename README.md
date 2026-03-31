# 🚀 AI Cloud Cost Optimizer

AI Cloud Cost Optimizer is an intelligent cloud automation platform that monitors AWS infrastructure in real-time and automatically optimizes EC2 resources to reduce unnecessary cloud costs.

---

## 📌 Project Overview

This system integrates AWS CloudWatch, Machine Learning, and Automation to monitor EC2 CPU utilization and take intelligent actions such as stopping underutilized instances or sending alerts.

The goal is to minimize cloud waste and improve cost efficiency.

---

## 🧠 Key Features

- 📊 Real-time AWS EC2 monitoring using CloudWatch
- 🤖 Intelligent decision-making using ML models
- ⚡ Automatic stopping of underutilized EC2 instances
- 📧 Email alerts using AWS SES
- 🌐 Interactive dashboard using Flask
- ☁️ Fully integrated with AWS services

---

## 🏗️ System Architecture

User → Flask Dashboard
↓
Backend (Boto3)
↓
AWS CloudWatch Metrics
↓
ML Engine (Prediction)
↓
Automation Engine
↓
EC2 Stop / Email Alert


---

## 🛠️ Tech Stack

- **Programming:** Python  
- **Framework:** Flask  
- **Cloud Services:** AWS EC2, CloudWatch, SES  
- **Libraries:** Boto3, Scikit-learn  
- **Frontend:** HTML, CSS  


User → Flask Dashboard
↓
Backend (Boto3)
↓
AWS CloudWatch Metrics
↓
ML Engine (Prediction)
↓
Automation Engine
↓
EC2 Stop / Email Alert


---

## 🛠️ Tech Stack

- **Programming:** Python  
- **Framework:** Flask  
- **Cloud Services:** AWS EC2, CloudWatch, SES  
- **Libraries:** Boto3, Scikit-learn  
- **Frontend:** HTML, CSS  

---


## 📂 Project Structure

ai-cloud-optimizer/
│
├── dashboard/
│ ├── app.py
│ └── templates/
│ └── index.html
│
├── backend/
├── ml-engine/
├── automation/
│
├── README.md
├── requirements.txt



---

## ⚙️ How It Works

1️⃣ CloudWatch collects EC2 CPU utilization  
2️⃣ Python backend fetches metrics using Boto3  
3️⃣ ML model predicts usage patterns  
4️⃣ If usage is below threshold → automation triggers  
5️⃣ EC2 instance is stopped or alert is sent  

---

## ▶️ Run the Project

```bash
git clone https://github.com/Mayank14-03/ai-cloud-optimizer.git
cd ai-cloud-optimizer/dashboard
pip install -r ../requirements.txt
python3 app.py


Open in browser:
http://<your-ec2-ip>:5000

## 📸 Screenshots

<img width="1919" height="1028" alt="dashboard" src="https://github.com/user-attachments/assets/e6bfc52f-2d8b-426f-a4ed-c6d9cf881dde" />

<img width="1919" height="970" alt="cloudwatch" src="https://github.com/user-attachments/assets/278fe733-5719-45ac-ae40-f03a16188c92" />

<img width="1919" height="953" alt="email-alert" src="https://github.com/user-attachments/assets/2f73e097-a708-407d-98bc-6cb9d9478af2" />

<img width="1919" height="971" alt="automation-log" src="https://github.com/user-attachments/assets/8184efb5-368f-4ca9-8409-e5935c0e6d10" />

<img width="1919" height="925" alt="terminal-output" src="https://github.com/user-attachments/assets/76a3e9cf-23a5-4fd2-84e8-5d26a060a985" />

🚀 Future Enhancements
Multi-cloud support (AWS, Azure, GCP)
Advanced ML-based cost prediction
Auto-scaling instead of stopping instances
Authentication & user roles

💼 Resume Impact
This project demonstrates:

Real-world AWS cloud experience
Automation & DevOps skills
Machine Learning integration
Full-stack development capability

👨‍💻 Author
Mayank Korde

GitHub: https://github.com/Mayank14-03

