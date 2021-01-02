from fastapi import FastAPI, Request
from fastapi.param_functions import Form
from fastapi.templating import Jinja2Templates
import uvicorn
from input_processing import model_answer_please

templates = Jinja2Templates(directory='templates')

main = FastAPI()

@main.get('/')
async def detect_me(request: Request):
    spam = "Please Enter message"
    return templates.TemplateResponse('index.html', context={'request': request, 'Spam': spam})

@main.post('/')
async def detect_me(request: Request, message: str = Form(...)):
    spam = f"It's {model_answer_please(message)}."
    return templates.TemplateResponse('index.html', context={'request': request, 'Spam': spam, 'msg': message})

if __name__ == "__main__":
    uvicorn.run(main)
