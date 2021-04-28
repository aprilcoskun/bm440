from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.responses import HTMLResponse
from passlib.context import CryptContext
from pydantic import BaseModel
from utils.templates import templates
from db import db_conn

router = APIRouter(prefix="/auth", tags=["Authentication"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    password: str


@router.get("/", response_class=HTMLResponse)
def auth_page(request: Request):
    return templates.TemplateResponse('auth.html', {"request": request})


@router.post("/")
def login(user: User, response: Response):
    print(user)
    if user.username == "Admin":
        if user.password == "password":
            response.headers["Location"] = "/"
            response.set_cookie(key="username", value=user.username)
            response.status_code = status.HTTP_200_OK
            return response
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong Password")
    employee = db_conn.get_user(username=user.username)
    # TODO: validate employee

    response.headers["Location"] = "/"
    response.set_cookie(key="username", value=employee.username)
    response.status_code = status.HTTP_200_OK
    return response