# Use an official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy local project files to the container
COPY . /app

# Install dependencies (if any)
RUN pip install flask

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]

