from fastapi import APIRouter, Depends
from db import db_conn
from utils import auth_helper

router = APIRouter(prefix="/staff", tags=["Staff"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/")
def get_all():
    return {"db_version": db_conn.get_version()}
