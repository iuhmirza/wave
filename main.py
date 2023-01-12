from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class User(BaseModel):
    id: int = None
    username: str
    views: int

user_list: list[User] = []
test_user = User(**{
    "id": 0,
    "username": "tester",
    "views": 0
})

user_list.append(test_user)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/users")
def read_users():
    return {"users": user_list}

@app.post("/api/users")
def add_user(user: User):
    print(user)
    user.id = len(user_list)
    user_list.append(user)
    return user


@app.put("/api/users/{user_id}")
def update_user(user_id: int):
    user = user_list[user_id]
    user.views += 1
    return user

