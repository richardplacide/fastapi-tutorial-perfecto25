from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="./tutorial/static"), name='static')
templates = Jinja2Templates(directory="./tutorial/templates")


@app.get("/")
async def index():
    return {"message":"Hello Tutorial!"}

@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

from tutorial.views.next import next


