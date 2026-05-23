from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel, Field

client = MongoClient("mongodb://localhost:27017/")
db = client["tutorial"]
collection = db["users"]

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=10)
    email: str = Field(..., min_length=3, max_length=10)
    age: int = Field(..., gt=0, lt=100)
    is_active: bool = True

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    user_dict = user.dict()
    collection.insert_one(user_dict)
    return user

@app.get("/users/")
def get_all_users():
    users = []
    for user in collection.find():
        users.append(User(**user))
    return users