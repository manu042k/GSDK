# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the Docker container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY . /app/

# Expose port 8000
EXPOSE 8080

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
