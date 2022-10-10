from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
import models
from models import CounterTable, Addition, Substraction
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import configparser

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


config = configparser.ConfigParser()
config.read('config.ini')
count_str = config['variables']['count']
count = int(count_str)


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

def add_to_counter():
    global count
    count += 1

def substract_from_counter():
    global count
    count -= 1

def update_config(count):
    global config 
    config['variables']['count'] = str(count)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

@app.post("/add")
async def add(request: Request, background_tasks: BackgroundTasks):


    add_to_counter()
    background_tasks.add_task(update_config, count)

    return templates.TemplateResponse("home.html", {
        "request": request,
        "data": count
    })

@app.post("/substract")
async def substract(request: Request, background_tasks: BackgroundTasks):

    #background_tasks.add_task(add)

    #global count
    #count -= 1

    substract_from_counter()
    background_tasks.add_task(update_config, count)

    return templates.TemplateResponse("home.html", {
        "request": request,
        "data": count
    })

