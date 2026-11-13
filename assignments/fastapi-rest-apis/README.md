# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI. Students will create endpoints, define request and response models, and practice handling JSON data in a clean and structured way.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a new FastAPI application and define a root endpoint that confirms the API is running.

#### Requirements
Completed program should:

- Import `FastAPI` from the `fastapi` package
- Create an app instance named `app`
- Define a root route using `@app.get("/")`
- Return a simple welcome message or status message in JSON format

### 🛠️ Create a Resource Model

#### Description
Define a data model for a simple API resource such as a task, book, or item.

#### Requirements
Completed program should:

- Use `BaseModel` from `pydantic`
- Define a resource model with at least three fields
- Include a required field and at least one optional field
- Demonstrate how the model is used in API request handling

### 🛠️ Build CRUD Endpoints

#### Description
Add endpoints to create, read, and list resources through the API.

#### Requirements
Completed program should:

- Create a route to list all resources
- Create a route to retrieve a single resource by ID
- Create a route to add a new resource
- Use an in-memory data store or a simple Python list for storage
- Return JSON data from each endpoint

### 🛠️ Validate Inputs and Return Responses

#### Description
Improve the API by validating input data and making responses more structured and predictable.

#### Requirements
Completed program should:

- Validate request data using the model definition
- Return the created resource in a consistent JSON format
- Handle missing or invalid data gracefully
- Show a clear example response for one endpoint
