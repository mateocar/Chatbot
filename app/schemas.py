from pydantic import BaseModel

class MessageRequest(BaseModel):
    text:str

class MessageResponse(BaseModel):
    text:str