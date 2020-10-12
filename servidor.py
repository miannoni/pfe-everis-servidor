from fastapi import FastAPI

app = FastAPI()

users = {}

@app.get("/login")
async def root():
    return users