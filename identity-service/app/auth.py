from fastapi import APIRouter, HTTPException
from .models import UserRegister, UserLogin

router = APIRouter()

# temporary memory database
users = []


# REGISTER API
@router.post("/register")
def register(user: UserRegister):

    for u in users:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="User already exists")

    users.append({
        "username": user.username,
        "password": user.password
    })

    return {"message": "User registered successfully"}


# LOGIN API
@router.post("/login")
def login(user: UserLogin):

    for u in users:
        if u["username"] == user.username and u["password"] == user.password:
            return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid username or password")