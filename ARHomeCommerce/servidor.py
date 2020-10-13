from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    _id: int

class Pedido(BaseModel):
    _id: int
    data: str
    produto: Produto
    detalhes: Optional[str] = None
    entregue: Optional[int] = 0

class Cartao(BaseModel):
    numero: str
    dono: str
    validade: str
    codigo: str

class User(BaseModel):
    username: str
    password: str
    bio: Optional[str] = None
    pedidos: Optional[dict] = None
    cartoes: Optional[dict] = None
    enderecos: Optional[dict] = None

app = FastAPI()

produtos = {
                1 : { 
                    "nome" : "Cocacola",
                    "preco" : "2,99"
                    },
                2 : { 
                    "nome" : "Pepsi",
                    "preco" : "2,29"
                    }
            }

users = { 
            "Matt" : {
                    "username" : "Matt",
                    "password" : "12345",
                    "bio" : "Hello World"
                    }
        }

@app.get("/")
async def root():
    return 404

################### LOGIN ###################

@app.get("/login")
async def login():
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

################### CARTAO ###################

@app.get("/login/cartao")
async def cartoes():
    if (user.username in users.keys()):
        if (user.password == users[user.username]["password"]):
            return users[user.username]["cartoes"]

@app.post("/login/cartao", response_description="Data added into the database")
async def create_user_data(user: User):
    if (user.username in users.keys()):
        if (user.password == users[user.username]["password"]):
            users[user.username]["cartoes"][] = user.cartoes

# @app.put("/login/cartao", response_description="Data modified in the database")
# async def mod_student_data(user: User):
    # if (user.username in users.keys()):
    #     users[user.username] = user
    #     return user.username + " has been modified"
    # else:
    #     return "User " + user.username + " does not exist in database"

# @app.delete("/login/cartao", response_description="Data modified in the database")
# async def del_student_data(user: User):

#     if (user.username in users.keys()):
#         del users[user.username]
#         return user.username + " has been deleted"
#     else:
#         return "User " + user.username + " does not exist in database"

################### ENDERECO ###################
@app.get("/login/endereco")
async def cartoes():
    if (user.username in users.keys()):
        if (user.password == users[user.username]["password"]):
            return users[user.username]["cartoes"]

@app.post("/login/endereco", response_description="Data added into the database")
async def create_user_data(user: User):
    if (user.username in users.keys()):
        if (user.password == users[user.username]["password"]):
            users[user.username]["cartoes"] = user.cartoes

################### PEDIDO ###################

################### PRODUTO ###################