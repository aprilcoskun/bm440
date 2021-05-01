from fastapi import APIRouter, Depends, Request
from db import db_conn
from utils import auth_helper
from fastapi.responses import HTMLResponse
from utils.templates import templates

router = APIRouter(prefix="/sales", tags=["Sales"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/", response_class=HTMLResponse)
def get_all(request: Request, user=Depends(auth_helper.get_current_user)):
    sales = db_conn.get_all_sales()
    return templates.TemplateResponse('sales.html', {
        "request": request,
        "page": "sales",
        "user": user,
        "sales": sales
    })

