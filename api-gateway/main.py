from fastapi import FastAPI
import requests

app = FastAPI()


IDENTITY_SERVICE = "http://identity-service:5000"


@app.post("/login")
def login(data: dict):

    res = requests.post(f"{IDENTITY_SERVICE}/login", json=data)

    return res.json()


@app.post("/register")
def register(data: dict):

    res = requests.post(f"{IDENTITY_SERVICE}/register", json=data)

    return res.json()