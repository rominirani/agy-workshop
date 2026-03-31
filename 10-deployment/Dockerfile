# BUG (DevOps): This Dockerfile is basic and not optimized for production.
# It uses a large base image and runs as root.
# Attendees should optimize this (e.g., use alpine, add a non-root user, multi-stage build).

FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Insecurely exposing PORT
EXPOSE 5000

CMD ["python", "app.py"]
