from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
import models
from models import CounterTable, CountChangeRequest
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("home.html", {
        "request": request,
        "somevar": 2
    })



@app.post("/change")
def change(change_request: CountChangeRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    countertable = CounterTable()
    countertable.count = change_request.change

    db.add(countertable)
    db.commit()
    

    return templates.TemplateResponse("home.html", {
        "request": change_request,
        "somevar": 2
    })
