from fastapi import APIRouter, Depends, Request, Query
from db import database, Customer
from typing import Optional
from utils import auth_helper
from utils.templates import templates

router = APIRouter(prefix="/customers", tags=["Customers"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/")
def get_all(request: Request, user=Depends(auth_helper.get_current_user),
            search_type: Optional[str] = Query(None), search: Optional[str] = Query(None)):

    customers = database.get_all_customers()

    if search_type is not None and search is not None:
        customers = [c for c in customers if search in c[search_type]]

    return templates.TemplateResponse('customers.html', {
        "request": request,
        "page": "customers",
        "user": user,
        "customers": customers
    })


@router.post("/")
def save_customer(customer: Customer):
    return database.insert_customer(customer)


@router.put("/")
def update_customer(customer: Customer):
    return database.update_customer(customer)


@router.delete("/")
def delete_customer(tc: str):
    return database.delete_customer(tc)

