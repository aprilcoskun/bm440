from fastapi import APIRouter
from routers import auth, customers, staff, sales, products, index, backup

router = APIRouter()

router.include_router(auth.router)
router.include_router(index.router)
router.include_router(staff.router)
router.include_router(sales.router)
router.include_router(backup.router)
router.include_router(products.router)
router.include_router(customers.router)
