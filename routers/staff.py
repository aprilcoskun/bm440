from fastapi import APIRouter, Depends, Request
from passlib.context import CryptContext
from db import database, Employee
from utils import auth_helper
from utils.templates import templates

router = APIRouter(prefix="/staff", tags=["Staff"], dependencies=[Depends(auth_helper.check_user)])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/")
def get_all(request: Request, user=Depends(auth_helper.get_current_user)):
    staff = database.get_all_staff()
    return templates.TemplateResponse('staff.html', {
        "request": request,
        "page": "staff",
        "user": user,
        "staff": staff
    })


@router.post("/")
def save_employee(employee: Employee):
    # hash password
    employee.password = pwd_context.hash(employee.password)
    return database.insert_employee(employee)



@router.put("/")
def update_employee(employee: Employee):
    return database.update_employee(employee)


@router.delete("/")
def delete_employee(tc: str):
    return database.delete_employee(tc)
