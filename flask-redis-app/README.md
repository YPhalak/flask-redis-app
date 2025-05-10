# Flask Redis App with Docker Compose

This project demonstrates a simple Flask application that interacts with Redis. The application is containerized using Docker and orchestrated using Docker Compose.

---

## 📦 Project Structure

flask-redis-app/
├── app.py
│── requirements.txt
├── .env
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
└── README.md


---

## 🚀 Features

- Flask API with endpoints to set and get key-value pairs in Redis
- Redis container with named volume for data persistence
- Environment variables configured via `.env` file
- Healthchecks for both Flask and Redis services
- Clean and optimized Dockerfile

---

## 🔧 Prerequisites

- Docker installed
- Docker Compose installed

---

## ⚙️ Setup Instructions

1. **Clone the repository**

git clone https://github.com/your-username/flask-redis-app.git
cd flask-redis-app

2.Create .env file

FLASK_ENV=development
REDIS_HOST=redis

3.Build and run containers

docker-compose up -d --build

🧪 API Usage (Sample cURL Commands)
Set a key:
curl -X POST -H "Content-Type: application/json" \
-d '{"key":"language", "value":"python"}' \
http://localhost:5000/set

Get a key:
curl http://localhost:5000/get/language

🩺 Health Check (Optional)
You can check the health status of the containers:

docker inspect --format='{{json .State.Health}}' flask-redis-app_flask-app_1
docker inspect --format='{{json .State.Health}}' flask-redis-app_redis_1

📁 Named Volume
Redis uses a named volume redis_data for persistence:

docker volume ls

📌 Environment Variables:

| Variable    | Default     | Description        |
| ----------- | ----------- | ------------------ |
| FLASK\_ENV  | development | Flask environment  |
| REDIS\_HOST | redis       | Redis service host |

🧹 Clean Up:

docker-compose down -v

This will stop containers and remove the named volume.


