from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    grade:float

students = [Student(id=1, name="John Doe", grade=85.5),
            Student(id=2, name="Jane Smith", grade=92.0),]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student:Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    for index,student in enumerate(students):
        if student.id==student_id:
            students[index]=updated_student
            return updated_student
    return {"error":"Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for i,student in enumerate(students):
        if student.id == student_id:
            del students[i]
            return {"message":"Student deleted"}
    return {"error":"Student not found"}