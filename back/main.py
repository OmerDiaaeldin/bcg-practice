from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

class Item(BaseModel):
    name: str
    email: str
    enrollment: bool
    number: int
    course: str


@router.post("/Students/addStudents/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.enrollment :
        name= item.name
        email= item.email
        number= item.number
        course=item.course
        item_dict.update({"name": name}, {"email": email}, {"number": number}, {"course": course})
    return item_dict



@router.put("/Students/EditStudents/")
async def edit_item(item_id: int, item: Item):
    for student in Students:
        if item.enrollment :
            name= item.name
            email= item.email
            number= item.number
            course=item.course
            item_dict.update({"name": name}, {"email": email}, {"number": number}, {"course": course})
        return item_dict


app.include_router(router)