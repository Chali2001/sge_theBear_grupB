from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read, user
import os

app = FastAPI()

# 1. Carregar variables de entorno
load_dotenv()

# 2. Configurar la connexió a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL") # obtenir la url de connexió des de .env
engine = create_engine(DATABASE_URL) # crear l'engine de connexió

# 3. Crear les taules a la base de dades
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

@app.get("/users", response_model=list[dict])
def read_user (db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str,db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users/", response_model=dict)
async def update_user(name: str, newName: str, db:Session = Depends(get_db)):
    result = user.update_user(name, newName, db)
    return result

@app.delete("/users/", response_model=dict)
async def update_user(id: int, db:Session = Depends(get_db)):
    result = user.delete_user(id, db)
    return result