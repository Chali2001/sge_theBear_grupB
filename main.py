from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from datetime import date
from typing import Optional
from models.Factura import EstadoFactura
from services import Punto_Venta, Factura
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

# CRUD DE PUNTO DE VENTA

# GET PUNTO DE VENTA
@app.get("/puntoVenta", response_model=List[dict])
async def read_puntoVenta (db:Session = Depends(get_db)):
    result = Punto_Venta.get_all_punts(db)
    return result

@app.get("/puntoVenta/{id}", response_model=dict)
async def read_puntoVenta_id(id: int, db:Session = Depends(get_db)):
    result = Punto_Venta.get_punto(id, db)
    return result

# CREATE PUNTO DE VENTA
@app.post("/puntoVenta", response_model=dict)
async def create_puntoVenta(id_pedido: Optional[int] = None, reserva: bool = False, id_factura: Optional[int] = None, db:Session = Depends(get_db)):
    result = Punto_Venta.add_new_punto(id_pedido, reserva, id_factura, db)
    return result

# UPDATE PUNTO DE VENTA
@app.put("/puntoVenta/{id}", response_model=dict)
async def update_puntoVenta(id: int, id_pedido: Optional[int] = None, reserva: bool = False, id_factura: Optional[int] = None, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto(id, id_pedido, reserva, id_factura, db)
    return result

@app.put("/puntoVenta/reserva/{id}", response_model=dict)
async def update_puntoVenta_reserva(id: int, reserva: bool, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto_reserva(id, reserva, db)
    return result

@app.put("/puntoVenta/id_factura/{id}", response_model=dict)
async def update_puntoVenta_id_factura(id: int, id_factura: int, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto_id_factura(id, id_factura, db)
    return result
@app.put("/puntoVenta/id_pedido/{id}", response_model=dict)
async def update_puntoVenta_id_pedido(id: int, id_pedido: int, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto_id_pedido(id, id_pedido, db)
    return result

# DELETE PUNTO DE VENTA
@app.delete("/puntoVenta/{id}", response_model=dict)
async def delete_puntoVenta(id: int, db:Session = Depends(get_db)):
    result = Punto_Venta.delete_punto(id, db)
    return result


# CRUD DE FACTURA
# GET FACTURA
@app.get("/factura", response_model=List[dict])
async def read_factura(db:Session = Depends(get_db)):
    result = Factura.get_all_facturas(db)
    return result

@app.get("/factura/{id}", response_model=dict)
async def read_factura_id(id: int, db:Session = Depends(get_db)):
    result = Factura.get_factura(id, db)
    return result

# CREATE FACTURA
@app.post("/factura", response_model=dict)
async def create_factura(costo: float, fecha: date ,estado: EstadoFactura, db:Session = Depends(get_db)):
    result = Factura.add_new_factura(costo, fecha, estado, db)
    return result

# UPDATE FACTURA
@app.put("/factura/{id}", response_model=dict)
async def update_factura(id: int, costo: float, fecha: date, estado: EstadoFactura, db:Session = Depends(get_db)):
    result = Factura.update_factura(id, costo, fecha, estado, db)
    return result

@app.put("/factura/costo/{id}", response_model=dict)
async def update_factura_costo(id: int, costo: float, db:Session = Depends(get_db)):
    result = Factura.update_factura_costo(id, costo, db)
    return result

@app.put("/factura/fecha/{id}", response_model=dict)
async def update_factura_fecha(id: int, fecha: date, db:Session = Depends(get_db)):
    result = Factura.update_factura_fecha(id, fecha, db)
    return result

@app.put("/factura/estado/{id}", response_model=dict)
async def update_factura_estado(id: int, estado: EstadoFactura, db:Session = Depends(get_db)):
    result = Factura.update_factura_estado(id, estado, db)
    return result

# DELETE FACTURA
@app.delete("/factura/{id}", response_model=dict)
async def delete_factura(id: int, db:Session = Depends(get_db)):
    result = Factura.delete_factura(id, db)
    return result

