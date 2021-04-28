from fastapi import FastAPI
from routers import router

app = FastAPI(title="veritabani proje", version="1.0.0")

app.include_router(router)
