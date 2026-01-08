# fastAPI_small_lessgo

# Project 1

This project covers the fundamentals of building APIs with FastAPI, including:

- **GET Requests** – Create endpoints to fetch data from the server.
- **Path Parameters** – Pass dynamic values through URL paths.
- **Query Parameters** – Handle optional or filtered inputs via URL queries.
- **POST Requests** – Add new data to the server using request bodies.
- **PUT Requests** – Update existing data on the server.
- **DELETE Requests** – Remove data from the server.

# Project 2

This project builds on Project 1 and introduces **data validation and advanced FastAPI features**:

- **Pydantic v1 vs v2** – Understand the differences and improvements in Pydantic for data modeling.
- **POST Requests with Validation** – Use Pydantic models to validate incoming request data.
- **Fields and Data Validation** – Apply constraints like min/max length, greater/less than, and optional fields.
- **Pydantic Configurations** – Customize request models, example values, and schema generation.
- **GET Requests** – Fetch all books, or filter by rating.
- **PUT Requests** – Update existing book entries.
- **DELETE Requests** – Remove book entries from the server.
- **Path & Query Parameter Validation** – Validate incoming parameters dynamically.
- **Status Codes & HTTP Exceptions** – Handle responses explicitly with proper HTTP status codes.

### HTTP Status Codes - Key Takeaways

| Status Code | Meaning                   | Typical Usage               |
|------------|---------------------------|----------------------------|
| 200 OK     | Request successful        | GET, PUT, DELETE           |
| 201 Created| Resource created          | POST                       |
| 204 No Content | Success, no data       | DELETE, PUT (sometimes)    |
| 400 Bad Request | Invalid request       | POST, PUT                  |
| 404 Not Found | Resource not found      | GET, PUT, DELETE           |
| 500 Internal Server Error | Server failed | Any request               |

# Project 3: 📝 Todo Application (FastAPI)

A **production-ready Todo Application** built using **FastAPI**, designed to demonstrate real-world backend development concepts including **authentication, authorization, database integration, migrations, and role-based access control**.

This project evolves step-by-step from a simple CRUD-based Todo app to a **secure, scalable API** using modern backend tools and best practices.

---

## 🚀 Project Overview

This Todo application allows users to:

- Register and authenticate securely
- Create, update, delete, and view their own todos
- Use JWT-based authentication for protected routes
- Enable admin-level operations
- Work with multiple database systems
- Apply schema migrations using Alembic

The project is fully documented using **Swagger UI (OpenAPI 3.1)**.

---

## 🧠 Concepts & Technologies Covered

### 🔹 FastAPI Core
- FastAPI project structure & best practices
- Request lifecycle and dependency injection
- Path & query parameters
- Status codes (`200`, `201`, `400`, `401`, `403`, `404`, `500`)
- Interactive API docs using Swagger UI

### 🔹 Pydantic
- Pydantic v1 vs Pydantic v2
- Request validation
- Response models
- Data serialization & type enforcement

### 🔹 Database & ORM
- SQL fundamentals
- SQLite3 (local development)
- PostgreSQL (production-ready DB)
- MySQL integration
- SQLAlchemy ORM
- One-to-Many relationships
- Foreign keys
- Database session handling

### 🔹 Authentication & Authorization
- User registration & login
- Password hashing (Passlib)
- OAuth2 password flow
- JSON Web Tokens (JWT)
- Token encoding & decoding
- Securing routes using dependencies
- Role-based access (Admin vs User)

### 🔹 API Architecture
- Router-based modular design
- Separation of concerns
- Auth router
- Todo router
- Admin router
- User router

### 🔹 Database Migration
- Alembic setup & configuration
- Revision creation
- Upgrade & downgrade migrations
- Schema versioning
- Safe DB evolution

# 🧪 Testing (Todo Application)

This project includes a comprehensive **automated testing suite** to ensure reliability, correctness, and production readiness of the API.

Testing is implemented using **Pytest** and **FastAPI’s TestClient**, covering authentication, authorization, database operations, and role-based access control.
 

### 🔹 Test Structure

Todo_app/
├── test/
│ ├── test_admin.py # Admin-only routes
│ ├── test_todo.py # Todo CRUD operations
│ ├── test_example.py # Basic sanity tests
│ ├── user_test.py # User-related endpoints
│ └── utils.py # Test DB & dependency overrides

## 🔹 Running Tests

Run all tests using:

```bash
pytest
