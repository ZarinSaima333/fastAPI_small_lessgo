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