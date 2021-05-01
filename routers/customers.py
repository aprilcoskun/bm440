from fastapi import APIRouter, Depends, Request
from db import db_conn
from utils import auth_helper
from fastapi.responses import HTMLResponse
from utils.templates import templates

router = APIRouter(prefix="/customers", tags=["Customers"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/", response_class=HTMLResponse)
def get_all(request: Request, user=Depends(auth_helper.get_current_user)):
    customers = db_conn.get_all_customers()
    return templates.TemplateResponse('customers.html', {
        "request": request,
        "page": "customers",
        "user": user,
        "customers": customers
    })
