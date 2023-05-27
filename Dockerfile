FROM python:3.11-slim-buster

WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install Git and Postgres client
RUN apt-get update && apt-get install -y git postgresql-client && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for dbt
ENV DBT_PROFILES_DIR=/app/modeling

# Copy source code and the wait-for-postgres.sh script
COPY . .

RUN chmod +x ./wait-for-postgres.sh
