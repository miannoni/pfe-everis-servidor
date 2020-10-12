from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    bio: Optional[str] = None

app = FastAPI()

users = {}

@app.get("/login")
async def root():
    return users

@app.post("/login", response_description="Data added into the database")
async def create_user_data(user: User):
    if (user.username not in users.keys()):
        users[username] = user
    return user.username + "'s data added into the database"

@app.post("/login", response_description="Data added into the database")
async def add_student_data():
    return users