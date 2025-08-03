# Sales Agent Microservice (FastAPI)

A production-grade FastAPI application with SOLID principles and modular architecture for querying product search and pricing information.

## 🏗️ Tech Stack

- FastAPI  
- PostgreSQL (Async via asyncpg)  
- SQLAlchemy  
- Docker  
- Kubernetes-ready  

## 🚀 Run Locally

```bash
docker build -t sales-agent .
docker run -p 8000:8000 sales-agent

Visit `http://localhost:8000/docs` for interactive Swagger UI.

## 🧪 Endpoints

- `POST /search` – Search products by keyword  
- `GET /price/{product_id}` – Fetch product price

## 🐳 Kubernetes Ready

This app is built for containerization and GKE deployment.
