from fastapi import FastAPI
from routers import router

app = FastAPI(title="BM 440", version="1.0.0")

app.include_router(router)
