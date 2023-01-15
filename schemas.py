from pydantic import BaseModel

class MessageBase(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    encrypted_content: str
    time_stamp: str

    class Config:
        orm_mode = True


class ConversationBase(BaseModel):
    id: int
    messages: list(MessageBase)

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    id: int
    email: str
    username: str
    hashed_password: str
    public_key: str

    class Config:
        orm_mode = True

class UserSchema(UserBase):
    conversations: list[ConversationBase]

class ConversationSchema(ConversationBase):
    users: list[UserBase]
    messages: list(MessageBase)