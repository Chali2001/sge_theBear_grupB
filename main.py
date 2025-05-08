from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from datetime import date, time
from models.evento import Assistencia
from services.eventos import get_all_eventos, get_evento, add_new_evento, update_evento, delete_evento
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

# Para crear una instacia de FastAPI
app = FastAPI()

# Ruta GET para obtener todos los eventos
@app.get("/eventos")
def get_eventos(db: Session = Depends(get_db)):
    #Llama la funcion que muestra todos los eventos
    return get_all_eventos(db)

# Ruta GET para obtener el evento con el id introducido
@app.get("/eventos/{id}")
# Recibe un ID para introducir en la funcion
def read_evento(id: int, db: Session = Depends(get_db)):
    #Llama la funcion que muestra el evento del id introducido
    return get_evento(id, db)

# Ruta POST para crear un evento con todos los atributos
@app.post("/eventos")
def create_evento(fecha: date, asiste: Assistencia, hora: time, direccion: str, id_empleado: int, db: Session = Depends(get_db)):
    # Llama la funcion que crea el evento
    return add_new_evento(fecha, asiste, hora, direccion, id_empleado, db)

# Ruta PUT para actualizar los datos del evento del ID introducido
@app.put("/eventos/{id}")
def update_evento(id: int, fecha: date, asiste: Assistencia, hora: time, direccion: str, id_empleado: int, db: Session = Depends(get_db)):
    # Llama la funcion que actualiza el evento del id introducido
    return update_evento(id, fecha, asiste, hora, direccion, id_empleado, db)

# Ruta DELETE para eliminar el evento del id introducido
@app.delete("/eventos/{id}")
def delete_evento(id: int, db: Session = Depends(get_db)):
    # Llama la funcion que elimina el evento con el id introducido
    return delete_evento(id, db)