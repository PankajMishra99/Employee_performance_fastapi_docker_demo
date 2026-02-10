# Base Image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Run FastAPI & Streamlit together
CMD uvicorn main:app --host 0.0.0.0 --port 8000 & \
    streamlit run fronted.py --server.port 8501 --server.address 0.0.0.0
