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
        users[user.username] = user
        return user.username + "'s data added into the database"
    else:
        return "Username already taken"

@app.put("/login", response_description="Data modified in the database")
async def mod_student_data(user: User):
    if (user.username in users.keys()):
        users[user.username] = user
        return user.username + " has been modified"
    else:
        return "User " + user.username + " does not exist in database"

@app.delete("/login", response_description="Data modified in the database")
async def del_student_data(user: User):
    if (user.username in users.keys()):
        del users[user.username]
        return user.username + " has been deleted"
    else:
        return "User " + user.username + " does not exist in database"