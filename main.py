from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user, read
import os
app = FastAPI()

# Carrega variables d'entorn
load_dotenv()

#Configurar la connexió a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL") #obtenim la URL de connexió des de .env
engine = create_engine(DATABASE_URL) #crear l'engine de connexió a la BD

#Crear les taules a la base de dades
SQLModel.metadata.create_all(engine)

# Proporcina la sessió a l'endpoint
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model= List[dict])
async def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name:str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result



