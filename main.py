from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model for salary computation input
class SalaryInput(BaseModel):
    salary: float
    bonus: float
    taxes: float

# Route 1: Handle GET requests
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Route 2: Handle POST requests
@app.post("/post-example")
def post_example(data: dict):
    return {"received_data": data}

# Route 3: Multiply a number by 2
@app.get("/double/{number}")
def double_number(number: int):
    return {"result": number * 2}

# Route 4: Compute salary + bonus - taxes
@app.post("/calculate-salary")
def calculate_salary(data: SalaryInput):
    try:
        result = data.salary + data.bonus - data.taxes
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Expected numbers.")

# Extended Route: Validate input fields
@app.post("/calculate-salary-validate")
def calculate_salary_validate(data: dict):
    required_fields = {"salary", "bonus", "taxes"}
    missing_fields = required_fields - data.keys()

    if missing_fields:
        raise HTTPException(
            status_code=400,
            detail=f"3 fields expected (salary, bonus, taxes). You forgot: {', '.join(missing_fields)}"
        )

    try:
        salary = float(data["salary"])
        bonus = float(data["bonus"])
        taxes = float(data["taxes"])
        result = salary + bonus - taxes
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Expected numbers, got strings.")
