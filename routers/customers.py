from fastapi import APIRouter, Depends
from db import db_conn
from utils import auth_helper

router = APIRouter(prefix="/customers", tags=["Customers"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/")
def get_all():
    return {"db_version": db_conn.get_version()}
