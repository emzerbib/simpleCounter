from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
#from simpleCounter.app.utils import add_to_counter, substract_from_counter, update_config
import configparser
import uvicorn

import os 
print(os.listdir('.'))

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
config = configparser.ConfigParser()
config.read('app/config.ini')
count_str = config['variables']['count']
count = int(count_str)


def add_to_counter():
    global count
    count += 1

def substract_from_counter():
    global count
    count -= 1

def update_config(count):
    global config 
    config['variables']['count'] = str(count)
    with open('app/config.ini', 'w') as configfile:
        config.write(configfile)

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


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")