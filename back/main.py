from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter, FastAPI
from src.prisma import prisma


app = FastAPI()
router = APIRouter()

class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    enrollment: bool
    number: int
    course: str


@router.get("/Student/viewStudent/")
async def view(item: Student):
    
@router.post("/Student/addStudent/")
async def create_item(item: Student):
    created = await Student.prisma().create(
        {
            "email": item.email,
            "first_name": item.first_name,
            "last_name": item.last_name,
            "number": item.number,
            "course": item.course,
        }
    )
    return created



@router.put("/Student/EditStudent/")
async def edit_item(item_id: int, item: Student):
    updated = await Student.prisma().update(
        {
            "email": item.email,
            "first_name": item.first_name,
            "last_name": item.last_name,
            "number": item.number,
            "course": item.course,
        }
    )
    return updated


# @router.delete("/Student/DeleteStudent/")
# async def delete_item(item_id: int):
    
#     student = await Student.prisma().delete(
#         data={

#         },
#     )



app.include_router(router)