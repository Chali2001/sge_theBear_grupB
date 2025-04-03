import fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os

#Carrega variables d'entorn des del fitxer .env
load_dotenv()

#S’obté la URL de la connexió a la BD de les variables d’entorn.
DATABASE_URL = os.getenv("DATABASE_URL")

#Es crea un objecte engine per gestionar la connexió a la BD
engine = create_engine(DATABASE_URL)

#Es creen automàticament les taules a la Base de dades
SQLModel.metadata.create_all(engine)

#Crear funcio "get_db()" que retorna una sessió de base de dades
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

