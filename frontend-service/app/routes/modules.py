from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from app import db

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# ---------------- HEARINGS PAGE ----------------
@router.get("/hearings", response_class=HTMLResponse)
async def hearings(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="modules/hearings.html",
        context={
            "hearings": db.hearings_db,
            "cases": db.cases_db
        }
    )

@router.post("/add-hearing")
async def add_hearing(
    case_id: int = Form(...),
    hearing_date: str = Form(...),
    court: str = Form(...)
):

    db.hearings_db.append({
        "case_id": case_id,
        "hearing_date": hearing_date,
        "court": court
    })

    return RedirectResponse("/hearings", status_code=303)


# ---------------- DOCUMENTS PAGE ----------------

@router.get("/documents", response_class=HTMLResponse)
async def documents(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="modules/documents.html",
        context={
            "documents": db.documents_db,
            "cases": db.cases_db
        }
    )

@router.post("/add-document")
async def add_document(
    case_id: int = Form(...),
    document_name: str = Form(...)
):

    db.documents_db.append({
        "case_id": case_id,
        "document_name": document_name
    })

    return RedirectResponse("/documents", status_code=303)


# CLIENT PAGE
@router.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="modules/clients.html",
        context={
            "clients": db.clients_db
        }
    )

# ADD CLIENT
@router.post("/add-client")
async def add_client(name: str = Form(...), phone: str = Form(...)):

    client_id = len(db.clients_db) + 1

    db.clients_db.append({
        "id": client_id,
        "name": name,
        "phone": phone
    })

    return RedirectResponse("/clients", status_code=303)


# CASE PAGE
@router.get("/cases", response_class=HTMLResponse)
async def cases(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="modules/cases.html",
        context={
            "cases": db.cases_db,
            "clients": db.clients_db
        }
    )

# ADD CASE
@router.post("/add-case")
async def add_case(
    client_id: int = Form(...),
    case_title: str = Form(...),
    court: str = Form(...)
):

    db.cases_db.append({
        "client_id": client_id,
        "case_title": case_title,
        "court": court
    })

    return RedirectResponse("/cases", status_code=303)
