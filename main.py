from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Sales Agent")

app.include_router(router)

