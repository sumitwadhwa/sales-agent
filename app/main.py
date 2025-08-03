from fastapi import FastAPI
from .api import router

app = FastAPI(title="Sales Agent Microservice")

app.include_router(router)
