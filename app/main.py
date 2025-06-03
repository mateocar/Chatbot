from fastapi import FastAPI
from app.schemas import MessageRequest, MessageResponse
from app.model import get_response

app = FastAPI()

@app.post("/chatbot",response_model=MessageResponse)
def get_responses(message: MessageRequest):
    response = get_response(message.text)
    
    return {"text": response}


