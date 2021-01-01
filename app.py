from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from input_processing import model_answer_please

templates = Jinja2Templates(directory='templates')

app = FastAPI()

@app.get('/')
async def serve_home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/detect-me')
async def detect_me(message: str):
    return {"answer is": model_answer_please(message)}

if __name__ == "__main__":
    uvicorn.run(app)