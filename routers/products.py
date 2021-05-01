from fastapi import APIRouter, Depends, Request
from db import db_conn
from utils import auth_helper
from fastapi.responses import HTMLResponse
from utils.templates import templates

router = APIRouter(prefix="/products", tags=["Products"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/", response_class=HTMLResponse)
def get_all(request: Request, user=Depends(auth_helper.get_current_user)):
    products = db_conn.get_all_products()
    return templates.TemplateResponse('products.html', {
        "request": request,
        "page": "products",
        "user": user,
        "products": products
    })
