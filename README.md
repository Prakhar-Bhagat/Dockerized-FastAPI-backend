# 🚀 FastAPI Backend: Production-Ready API

A high-performance, robust REST API built with **FastAPI** and **PostgreSQL**. This project demonstrates a complete backend architecture including JWT authentication, SQLAlchemy ORM relationships, Docker containerization, and automated testing.

# 🚀 FastAPI Backend: Production-Ready API

[![](https://img.shields.io/badge/🔴_Live_Demo-Click_Here-red?style=for-the-badge)](https://dockerized-fastapi-backend.onrender.com/docs)

A high-performance, robust REST API built with **FastAPI** and **PostgreSQL**.
...

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🌟 Features

* **Authentication:** Secure User Signup & Login using **JWT (JSON Web Tokens)** and `bcrypt` password hashing.
* **CRUD Operations:** Create, Read, Update, and Delete capabilities for Blog Posts.
* **Database Relationships:** One-to-Many relationship (User $\rightarrow$ Posts) implementation using **SQLAlchemy**.
* **Data Validation:** Robust input validation using **Pydantic** schemas.
* **Containerization:** Fully Dockerized application (API + Database) using **Docker Compose**.
* **Testing:** Automated unit/integration tests using **Pytest**.
* **Documentation:** Interactive API documentation via **Swagger UI** and **ReDoc**.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Auth:** Python-Jose (JWT), Passlib (Bcrypt)
* **Validation:** Pydantic
* **Testing:** Pytest, HTTPX
* **DevOps:** Docker, Docker Compose

---

## ⚡ Quick Start (Docker)

The easiest way to run the project is using Docker.

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Prakhar-Bhagat/Dockerized-FastAPI-backend.git](https://github.com/Prakhar-Bhagat/Dockerized-FastAPI-backend.git)
    cd Dockerized-FastAPI-backend
    ```

2.  **Run with Docker Compose**
    ```bash
    docker-compose up --build
    ```

3.  **Access the API**
    * API Root: `http://localhost:8000`
    * **Interactive Docs (Swagger):** `http://localhost:8000/docs`

---

## 🏃‍♂️ Manual Setup (Local)

If you prefer running it without Docker:

1.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up the Database**
    * Ensure PostgreSQL is running locally.
    * Create a database named `testdb`.
    * Update the `DATABASE_URL` in `.env` (or set it manually in your environment).

4.  **Run the Server**
    ```bash
    uvicorn app.main:app --reload
    ```

---

## 🧪 Running Tests

This project uses `pytest` and an in-memory SQLite database to run isolated tests.

```bash
pytest -v

---

## 📚 API Endpoints

### Auth
* `POST /signup`: Register a new user.
* `POST /login`: Authenticate and receive an access token.

### Posts
* `GET /posts/`: Retrieve all posts.
* `POST /posts/`: Create a new post (Auth required).
* `GET /my-posts/`: Retrieve posts for the current logged-in user.

# --------------------------------------------->

## 🛡️ License
This project is licensed under the MIT License.