from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from test1 import model


app = FastAPI()

class inputtext(BaseModel):
    prompt:str
    
@app.post("/Chatbot")
def bot(input:inputtext):
            result = model(input.prompt)
            return f'chatbot : {result}'