from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app import db

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )

# REGISTER USER
@router.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):

    for user in db.users_db:
        if user["username"] == username:
            return {"error": "User already exists"}

    db.users_db.append({
        "username": username,
        "password": password
    })

    return RedirectResponse("/login", status_code=302)


# LOGIN USER
@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):

    for user in db.users_db:
        if user["username"] == username and user["password"] == password:
            return RedirectResponse("/dashboard", status_code=302)

    return {"error": "Invalid username or password"}
