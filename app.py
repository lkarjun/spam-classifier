from fastapi import FastAPI, Request
from fastapi.param_functions import Form
from fastapi.templating import Jinja2Templates
import uvicorn
from input_processing import columns_names
import re
from nltk.stem import WordNetLemmatizer
import pickle
from nltk.corpus import stopwords
import warnings
warnings.filterwarnings('ignore')


templates = Jinja2Templates(directory='templates')
model = pickle.load(open("spamModel_1.model", "rb"))

main = FastAPI()


def input_process(message: str) -> str:

    wordnet = WordNetLemmatizer()
    capturing_words = re.sub('[^a-zA-Z]', ' ', message)
    lowering_spliting = capturing_words.lower().split()
    rm_unwanted_words = [wordnet.lemmatize(word) for word in lowering_spliting
                            if not word in set(stopwords.words('english'))]
    finalized_word = ' '.join(rm_unwanted_words)

    return finalized_word

  
def process_message(message: str) -> str:
    
    message = input_process(message)
    dummy_list = [0 for _ in range(3000)]
    for i in message.split():
      if i in columns_names:
        temp = columns_names.index(i)
        if dummy_list[temp] >= 1:
          dummy_list[temp] += 1
        else:
          dummy_list[temp] = 1
          
    return dummy_list
    

def model_answer_please(message: str) -> str:
  message = process_message(message)
  return model.predict([message])[0]

@main.get('/')
async def detect_me(request: Request):
    spam = "Please Enter message"
    return templates.TemplateResponse('index.html', context={'request': request, 'Spam': spam, 'color': 'note-danger'})

@main.post('/')
async def detect_me(request: Request, message: str = Form(...)):
    spam = f"It's {model_answer_please(message)}"
    if "spam" in spam:
      return templates.TemplateResponse('index.html', context={'request': request, 
                       'Spam': "It's" + spam, 'msg': message, 'color': 'note-danger'})
    
    return templates.TemplateResponse('index.html', context={'request': request,
                       'Spam': "It's" + spam, 'msg': message, 'color': 'note-success'})

if __name__ == "__main__":
    uvicorn.run(main)
