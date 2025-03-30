# Dockerfile

# Use slim Python base image
FROM python:3.11-slim

# Environment settings for production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy entire project
COPY . .

# Collect static files for WhiteNoise
RUN python manage.py collectstatic --noinput

# Run with Gunicorn on port 8000 (Render expects this!)
CMD ["gunicorn", "aithena.wsgi:application", "--bind", "0.0.0.0:8000"]
