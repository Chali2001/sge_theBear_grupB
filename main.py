from typing import List
from services import empleado, cliente
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

import os

app = FastAPI()
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


#TODOS LOS EMPLEADOS GET CORRECTE
@app.get("/empleados", response_model= list[dict])
def read_empleat(db:Session = Depends(get_db)):
    result = empleado.get_all_empleados(db)
    return result


#EMPLEADO POR ID
@app.get("/empleados/{id}")
def read_empleadoid(id: int, db:Session = Depends(get_db)):
    result = empleado.get_one_empleado(id, db)
    return result



#CREAR EMPLEADO CORRECTE
@app.post("/empleado/")
def create_empleado(ID_empleado: int, nombre: str, cargo: str, ss:int, sueldo: int, db:Session = Depends(get_db)):
    result = empleado.add_new_empleado(ID_empleado, nombre, cargo,ss,sueldo,db)
    return result


#UPDATE EMPLEADO CORRECTE
@app.put("/empleado/actualitzar/{id}", response_model= dict)
async def update_empleado(id:int, nombre: str, cargo:str, ss: int, sueldo: int, db:Session = Depends(get_db)):
    result = empleado.update_empleado(id,nombre,cargo,ss,sueldo,db)
    return result

#DELETE EMPLEADO CORRECTE
@app.delete("/empleado/delete/{id}", response_model=dict)
async def delete_empleado(id:int, db:Session = Depends(get_db)):
    result = empleado.delete_empleado(id,db)
    return result


#CLIENTE CRUD


#TODOS LOS CLIENTE GET CORRECTE
@app.get("/clientes", response_model= list[dict])
def read_cliente(db:Session = Depends(get_db)):
    result = cliente.get_all_clientes(db)
    return result


#EMPLEADO POR ID
@app.get("/clientes/{id}")
def read_clienteid(id: int, db:Session = Depends(get_db)):
    result = cliente.get_one_cliente(id, db)
    return result



#CREAR EMPLEADO CORRECTE
@app.post("/cliente/")
def create_cliente(ID_cliente: int, nombre: str, telefono: str, db:Session = Depends(get_db)):
    result = cliente.add_new_cliente(ID_cliente, nombre, telefono,db)
    return result


#UPDATE EMPLEADO CORRECTE
@app.put("/cliente/actualitzar/{id}", response_model= dict)
async def update_cliente(id:int, nombre: str,telefono: str, db:Session = Depends(get_db)):
    result = cliente.update_cliente(id,nombre,telefono,db)
    return result

#DELETE EMPLEADO CORRECTE
@app.delete("/cliente/delete/{id}", response_model=dict)
async def delete_cliente(id:int, db:Session = Depends(get_db)):
    result = cliente.delete_cliente(id,db)
    return result



