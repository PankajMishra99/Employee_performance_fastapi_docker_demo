# Employee_performance_fastapi_docker_demo
This dataset captures daily work-from-home behavioral patterns and their relationship with employee burnout and productivity. It is designed to help analyze how factors such as working hours, screen exposure, meetings, breaks, sleep, and after-hours work collectively influence task completion efficiency and burnout risk.

The dataset consists of ~1800 daily records collected from multiple users, with each row representing a single day of work activity for a given user. Both weekdays and weekends are included to reflect realistic hybrid and flexible work schedules.

By combining objective workload metrics (work hours, screen time, meetings) with well-being indicators (sleep hours, burnout score, burnout risk), the dataset enables:

Burnout risk classification
Productivity vs well-being analysis
Behavioral pattern mining
Early burnout detection modeling


# Employee Performance FastAPI Docker Demo

This is an open-source project built using:
- FastAPI (Backend)
- Streamlit (Frontend)
- Docker

## Features
- REST API using FastAPI
- Streamlit UI
- Dockerized setup

## Run locally
```bash
git clone https://github.com/PankajMishra99/Employee_performance_fastapi_docker_demo.git
cd Employee_performance_fastapi_docker_demo
docker build -t employee-performance-app .
docker run -p 8000:8000 -p 8501:8501 employee-performance-app

