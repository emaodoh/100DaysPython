from fastapi import FastAPI, Request
# from typing import Optional
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app =FastAPI()

datas = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
    {"id": 3, "name": "Charlie", "role": "User"},
    {"id": 4, "name": "Diana", "role": "Moderator"},
    {"id": 5, "name": "Ethan", "role": "User"},
    {"id": 6, "name": "Fiona", "role": "User"},
    {"id": 7, "name": "George", "role": "Admin"},
    {"id": 8, "name": "Hannah", "role": "User"},
    {"id": 9, "name": "Ian", "role": "User"},
    {"id": 10, "name": "Julia", "role": "Moderator"}
]


 

@app.get("/get-student-by-id/{id}", include_in_schema=False)

def student_name(request: Request, id: int):
    for student_id in datas:
        if student_id["id"] == id:
            return templates.TemplateResponse(request, "index.html")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"datas":datas})