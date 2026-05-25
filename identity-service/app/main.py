from fastapi import FastAPI
from .auth import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"service": "identity-service running"}