from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from utils import add_to_counter, substract_from_counter, update_config
import configparser

app = FastAPI()

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
    substract_from_counter()
    background_tasks.add_task(update_config, count)

    return templates.TemplateResponse("home.html", {
        "request": request,
        "data": count
    })
