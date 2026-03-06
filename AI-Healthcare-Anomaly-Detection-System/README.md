# AI Healthcare Anomaly Detection System

This project is a simple AI-driven healthcare monitoring system that detects abnormal patterns in patient vital signs.

The system allows users to input patient vitals such as heart rate, oxygen saturation (SpO2), body temperature, blood pressure, and respiratory rate. The backend analyzes the data using an anomaly detection model and classifies the patient's condition as NORMAL, MEDIUM RISK, or HIGH RISK.

## Features

- User login system
- Manual patient vital input
- AI-based anomaly detection
- Real-time condition analysis
- Dashboard interface

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Machine Learning (Isolation Forest)

## Project Structure

AI-Healthcare-Anomaly-Detection-System
│
├── app.py
├── anomaly_detector.py
├── requirements.txt
├── README.md
│
├── templates
│   ├── login.html
│   └── dashboard.html
│
└── static
    └── style.css