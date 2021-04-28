from fastapi import APIRouter, Depends
from db import db_conn
from utils import auth_helper

router = APIRouter(prefix="/sales", tags=["Sales"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/")
def get_all(username: str = Depends(auth_helper.get_current_user)):
    return {"db_version": db_conn.get_version(), "username": username}
