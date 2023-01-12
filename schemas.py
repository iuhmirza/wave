from pydantic import BaseModel

class MessageBase(BaseModel):
    encrypted_content = str

class MessageCreate(BaseModel):
    pass

class Message(MessageBase):
    id: int
    sender_id: int
    receiver_id: int
    owner_id: int
    
    class Config:
        orm_mode = True

class ConversationBase(BaseModel):
    pass

class ConversationCreate(ConversationBase):
    pass

class Conversation(ConversationBase):
    id: int
    messages: list[Message]

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    conversations: list[Conversation] = []

    class Config:
        orm_mode = True