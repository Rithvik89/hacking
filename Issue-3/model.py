from pydantic import BaseModel

class Message(BaseModel):
    sender: str
    recipient: str
    content: str
