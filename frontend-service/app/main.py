from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import landing
from app.routes import auth
from app.routes import dashboard
from app.routes import modules

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(landing.router)
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(modules.router)