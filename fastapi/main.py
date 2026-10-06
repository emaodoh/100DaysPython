from fastapi import FastAPI, Path
from typing import Optional

app =FastAPI()

@app.get("/")
def index():
    return {"name": "fast api"} 

students = {
    1: {
        "name": "samuel",
        "age": 20,
        "class": 7,
    }
}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):

    return students[student_id] 

@app.get("/get-student-by-name")

def student_name(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

        
    return "Name not found"