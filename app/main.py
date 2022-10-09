from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("home.html", {
        "request": request,
        "somevar": 2
    })

