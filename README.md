# 🏥 Patient Management API (FastAPI CRUD)

A simple REST API built using **FastAPI** that performs complete **CRUD (Create, Read, Update, Delete)** operations for managing patient records.

This project demonstrates how to build API endpoints using FastAPI and manage patient data efficiently in a single application.

---

## 🚀 Features

- ➕ Create new patient records
- 📋 Read all patient data
- 🔍 Get patient details by ID
- ✏️ Update existing patient information
- ❌ Delete patient records
- ⚡ Fast and lightweight API using FastAPI
- 📦 Automatic API documentation with Swagger UI

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

---

## 📂 Project Structure

```
patient-management-api/
│
├── main.py          # Contains all CRUD endpoints
├── requirements.txt # Project dependencies
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repository-link>
```

### Move into project directory

```bash
cd patient-management-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /patients | Create patient |
| GET | /patients | Get all patients |
| GET | /patients/{id} | Get patient by ID |
| PUT | /patients/{id} | Update patient |
| DELETE | /patients/{id} | Delete patient |

---

## Example Patient JSON

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 28,
  "gender": "Male",
  "disease": "Fever"
}
```

---

## 🎯 Learning Outcomes

- Understanding REST API development
- Implementing CRUD operations
- Working with FastAPI routes
- Request validation using Pydantic
- API testing with Swagger UI

---

## Future Improvements

- Database integration (MySQL/PostgreSQL)
- Authentication & Authorization
- Docker deployment
- Pagination & Filtering

---

## Author

Developed by **Your Name**
