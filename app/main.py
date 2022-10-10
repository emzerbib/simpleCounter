from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
import models
from models import CounterTable, Addition, Substraction
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


count = 0


@app.get("/")
def home(request: Request):
    global count
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("home.html", {
        "request": request,
        "data": count
    })

@app.post("/add")
async def add(request: Request):
    global count
    count += 1
    return templates.TemplateResponse("home.html", {
        "request": request,
        "data": count
    })

@app.post("/substract")
async def substract(request: Request):
    global count
    count -= 1
    return templates.TemplateResponse("home.html", {
        "request": request,
        "data": count
    })

