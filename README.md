# Microservices-Based FastAPI Backend

A lightweight **microservices backend** built with **FastAPI**, **Docker**, and **Redis**, orchestrated entirely through a **single Docker Compose file**. The system is split into two independent services: a **Products CRUD service** and a **Checkout service**, demonstrating clean service boundaries and containerized deployment.

This project is designed to reflect **real-world backend architecture practices** while remaining simple, readable, and easy to run locally.

---

## Architecture Overview

The backend follows a **microservices architecture** with the following components:

- **Products Service** – Handles product creation, retrieval, updating, and deletion.
- **Checkout Service** – Manages checkout logic and order processing.
- **Redis** – Used as an in-memory data store for fast access and caching.
- **Docker Compose** – Orchestrates all services from a single configuration file.

Each service runs in its own container and communicates over an internal Docker network.

---

## Tech Stack

- **FastAPI** – High-performance Python web framework
- **Docker & Docker Compose** – Containerization and orchestration
- **Redis** – In-memory data store
- **Uvicorn** – ASGI server
- **Python 3.10+**

---

## Services

### Products Service

Responsible for managing product data.

**Key Features:**

- Create new products
- Retrieve product listings and individual products
- Update existing products
- Delete products

Runs as an independent FastAPI application.

---

### Checkout Service

Handles checkout and order-related logic.

**Key Features:**

- Processes checkout requests
- Communicates with the Products service
- Uses Redis for fast data access

Runs independently from the Products service.

---

## Why This Project

This project demonstrates:

- Practical microservices design
- Containerized backend development
- Service isolation and scalability
- Real-world FastAPI usage
- Clean, reproducible local development using Docker Compose
