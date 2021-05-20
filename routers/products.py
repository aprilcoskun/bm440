from fastapi import APIRouter, Depends, Request, Query
from db import database, Product
from typing import Optional
from utils import auth_helper
from utils.templates import templates

router = APIRouter(prefix="/products", tags=["Products"], dependencies=[Depends(auth_helper.check_user)])


@router.get("/")
def get_all(request: Request, user=Depends(auth_helper.get_current_user),
            search_type: Optional[str] = Query(None), search: Optional[str] = Query(None)):
    products = []

    if search_type is not None and search is not None:
        if search_type == "barcode":
            products = database.get_products_by_barcode(search)
        elif search_type == "name":
            products = database.get_products_by_name(search)
    else:
        products = database.get_all_products()

    return templates.TemplateResponse('products.html', {
        "request": request,
        "page": "products",
        "user": user,
        "products": products
    })


@router.post("/")
def save_product(product: Product):
    return database.insert_product(product)


@router.put("/")
def update_product(product: Product):
    return database.update_product(product)


@router.delete("/")
def delete_product(barcode: str):
    return database.delete_product(barcode)
