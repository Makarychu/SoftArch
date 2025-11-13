Video Platform Microservices
Overview

This project is a FastAPI microservices platform for video management.
It consists of three services:

Video Service – CRUD operations for videos.

Transcoder Service – Video processing and transcoding.

Moderation Service – Content moderation for videos.

The services use MongoDB Atlas as the database and are fully containerized using Docker.
The project is designed to be deployed on Render cloud platform.

Features

REST API endpoints for each service under /api.

Health check endpoints:

/video/api/health/db – checks MongoDB connectivity.

Dockerized for easy deployment.

Supports environment variables for configuration.

SSL/TLS secured connection to MongoDB Atlas.

Prerequisites

Python 3.11+ (for local testing)

Docker installed

Free Render
 account

Free MongoDB Atlas
 cluster

GitHub repository with project code

Environment Variables

Create the following environment variables in Render (do not commit .env to GitHub):

Variable	Description
MONGO_URI	MongoDB Atlas connection string
DB_NAME	Name of your database
JWT_SECRET	Secret key for authentication (random)

Example MONGO_URI:

mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority

Local Setup

Clone the repository:

git clone https://github.com/yourusername/video-platform.git
cd video-platform


Build Docker containers:

docker-compose build


Run containers locally:

docker-compose up


Test endpoints via Swagger UI:

http://localhost:8080/docs


Test database health:

GET http://localhost:8080/video/api/health/db


Expected response:

{
  "status": "ok",
  "db": "reachable"
}

Deployment on Render

Push your repository to GitHub.

Create a new Web Service on Render:

Connect to GitHub repo

Select Docker deployment

Set environment variables in Render dashboard

Deploy the project.

After deployment, test endpoints at:

https://your-app-name.onrender.com/video/api/health/db

Dockerfile Notes

Based on python:3.11-slim

Installs ca-certificates and openssl for SSL/TLS connection to MongoDB Atlas:

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

Health Checks

Each service exposes a /health/db endpoint to verify MongoDB connectivity.
Example:

curl https://your-app-name.onrender.com/video/api/health/db


Response:

{
  "status": "ok",
  "db": "reachable"
}

License

This project is for academic purposes only.
