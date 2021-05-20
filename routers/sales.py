from fastapi import APIRouter, Depends, Request
from db import database, Sale
from utils import auth_helper
from utils.templates import templates

router = APIRouter(prefix="/sales", tags=["Sales"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/")
def get_all(request: Request, user=Depends(auth_helper.get_current_user)):
    sales = database.get_all_sales()
    customers = database.get_all_customers()
    staff = database.get_all_staff()
    products = database.get_all_products()
    return templates.TemplateResponse('sales.html', {
        "request": request,
        "page": "sales",
        "user": user,
        "sales": sales,
        "customers": customers,
        "products": products,
        "staff": staff
    })


@router.post("/")
def save_sale(sale: Sale):
    return database.insert_sale(sale)
