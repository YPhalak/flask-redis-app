# Use an official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Expose the Flask default port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

