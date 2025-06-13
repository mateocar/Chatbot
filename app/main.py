from fastapi import FastAPI
from app.schemas import MessageRequest, MessageResponse
from app.model import get_response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chatbot",response_model=MessageResponse)
def get_responses(message: MessageRequest):
    response = get_response(message.text)
    
    return {"text": response}



