from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory='templates')

app = FastAPI()

@app.get('/')
async def serve_home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
