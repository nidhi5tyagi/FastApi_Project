# FastApi_Project

# FastAPI Project Documentation

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Deployment](#deployment)

---

## Introduction
This project demonstrates how to create a simple API using **FastAPI**. The API includes routes to handle GET and POST requests, as well as logic to process and validate input data.

## Requirements
The project includes the following features:

1. **GET Route**: Returns a welcome message.
2. **POST Route**: Accepts and echoes data.
3. **Double Route**: Accepts a number and returns it multiplied by 2.
4. **Salary Calculation Route**:
   - Accepts a JSON input containing `salary`, `bonus`, and `taxes`.
   - Returns the computation: `salary + bonus - taxes`.
   - Handles errors for missing fields or invalid input types.

## Installation
To set up the project:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## API Endpoints

### 1. GET `/`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
      "message": "Welcome to FastAPI!"
  }
  ```

### 2. POST `/post-example`
- **Description**: Accepts and echoes back JSON data.
- **Request Body**:
  ```json
  {
      "key": "value"
  }
  ```
- **Response**:
  ```json
  {
      "received_data": {"key": "value"}
  }
  ```

### 3. GET `/double/{number}`
- **Description**: Returns the input number multiplied by 2.
- **Path Parameter**:
  - `number` (int): The number to be doubled.
- **Response**:
  ```json
  {
      "result": <number * 2>
  }
  ```

### 4. POST `/calculate-salary`
- **Description**: Computes `salary + bonus - taxes`.
- **Request Body**:
  ```json
  {
      "salary": 2500,
      "bonus": 200,
      "taxes": 400
  }
  ```
- **Response**:
  - **Valid Input**:
    ```json
    {
        "result": 2300
    }
    ```
  - **Missing Fields**:
    ```json
    {
        "error": "3 fields expected (salary, bonus, taxes). You forgot: {missing_field}"
    }
    ```
  - **Invalid Input**:
    ```json
    {
        "error": "expected numbers, got strings."
    }
    ```

## Error Handling
- **Missing Fields**: Returns an error specifying the missing field(s).
- **Invalid Types**: Returns an error if non-numeric values are provided for `salary`, `bonus`, or `taxes`.

## Testing
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
3. Use tools like **Postman** or `curl` to test endpoints.

Example `curl` commands:
- Test GET route:
  ```bash
  curl http://127.0.0.1:8000/
  ```
- Test POST route:
  ```bash
  curl -X POST "http://127.0.0.1:8000/calculate-salary" -H "Content-Type: application/json" -d '{"salary": 2500, "bonus": 200, "taxes": 400}'
  ```

## Deployment
For deployment:
- Use **Docker**, **Gunicorn**, or platforms like **Heroku** or **AWS**.
- Refer to the [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/) for more information.
