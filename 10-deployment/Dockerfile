# --- STAGE 1: Build & Dependencies ---
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

# Use a virtualenv to isolate dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# --- STAGE 2: Optimized Production Image ---
FROM python:3.12-alpine

WORKDIR /app

# Create a non-privileged user for security
RUN adduser -D workshop-user
USER workshop-user

# Copy virtualenv from builder stage
COPY --from=builder /opt/venv /opt/venv

# Ensure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy source code
COPY --chown=workshop-user:workshop-user . .

# Set dynamic port via environment variable (default 8080)
ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]
