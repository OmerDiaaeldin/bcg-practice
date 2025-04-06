from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    enrollment: bool
    number: int
    course: str


@router.post("/Students/addStudents/")
async def create_item(item: Student):
    Student_dict = item.dict()
    if item.enrollment :
        first_name= item.first_name
        last_name= item.last_name
        email= item.email
        number= item.number
        course=item.course
        Student_dict.append({"first_name": first_name}, {"last_name": last_name}, {"email": email}, {"number": number}, {"course": course})
    return Student_dict



@router.put("/Students/EditStudents/")
async def edit_item(item_id: int, item: Student):
    StudentOnCourse = []
    for student in StudentOnCourse:
        if item.enrollment :
            name= item.name
            email= item.email
            number= item.number
            course=item.course
            student.update({"name": name}, {"email": email}, {"number": number}, {"course": course})
        return student





app.include_router(router)