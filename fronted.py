import streamlit as st
import requests

# API LINK
api_link = "http://127.0.0.1:8000/predict"

# Streamlit page config
st.set_page_config(page_title="Employee Performance Prediction", layout="centered")
st.title("Employee Performance Prediction")

# Input Fields
user_id = st.number_input("Employee ID", min_value=1, step=1)
day_types = st.selectbox("Day Type", ["Weekday", "Weekend"])
work_hours = st.number_input("Work Hours", min_value=0.0, max_value=12.0)
screen_time_hours = st.number_input("Screen Time Hours", min_value=0.0)
meetings_count = st.number_input("Meeting Count", min_value=0)
breaks_taken = st.number_input("Breaks Taken", min_value=0)
after_hours_work = st.number_input("After Hours Work", min_value=0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0)
task_completion_rate = st.number_input("Task Completion Rate (%)", min_value=0.0, max_value=100.0)
burnout_score = st.number_input("Burnout Score (%)", min_value=0.0, max_value=100.0)

# Predict Button
if st.button("Predict"):
    payload = {
        "user_id": int(user_id),
        "day_types": day_types,
        "work_hours": float(work_hours),
        "screen_time_hours": float(screen_time_hours),
        "meetings_count": float(meetings_count),
        "breaks_taken": int(breaks_taken),
        "after_hours_work": int(after_hours_work),
        "sleep_hours": float(sleep_hours),
        "task_completion_rate": float(task_completion_rate),
        "burnout_score": float(burnout_score)
    }

    try:
        response = requests.post(api_link, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Performance Level: **{result['Predicted result']}**")
        else:
            st.error(f"API Error Code: {response.status_code}")

    except Exception as e:
        st.error(f"API connection error: {e}")
