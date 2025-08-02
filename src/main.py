from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from pydantic import RootModel
from typing import Dict 

# Sleeper stuff 
from api.test import generate_user_map

app = FastAPI() 
app.mount("/static", StaticFiles(directory="static"), name="static")

class UserMap(RootModel): 
    root: Dict[str, str]

@app.get("/")
def root(): 
    return {"message" : "Hello World"}


@app.get("/users", response_model=UserMap)
def users(): 
    Mhs_grad_id = 1226686814018879488
    return generate_user_map(Mhs_grad_id)
