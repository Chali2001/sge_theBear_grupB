from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

from models.Pedido_mdl import EstadoPedido, Pedido
from models.Producto_mdl import Producto
from services import Pedido_srv, Producto_srv
from schema.Producto_sch import productos_schema
from schema.Pedido_sch import pedidos_schema

import os

app = FastAPI()

# Carrega variables d'entorn des del fitxer .env
load_dotenv()

# S’obté la URL de la connexió a la BD de les variables d’entorn.
DATABASE_URL = os.getenv("DATABASE_URL")

# Es crea un objecte engine per gestionar la connexió a la BD
engine = create_engine(DATABASE_URL)

# Es creen automàticament les taules a la Base de dades
SQLModel.metadata.create_all(engine)

# Crear funcio "get_db()" que retorna una sessió de base de dades
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


# GET PRODUCTO
@app.get("/Producto_srv", response_model=List[dict])
async def get_producto(db: Session = Depends(get_db)):
    producto = Producto_srv.get_producto(db)
    return productos_schema(producto)

# GET PRODUCTO -- ID
@app.get("/Producto_srv/{producto_id}", response_model=Producto)
async def get_producto_by_id(producto_id: int, db: Session = Depends(get_db)):
    producto = Producto_srv.get_producto_by_id(producto_id, db)
    return producto

# CREATE PRODUCTO
@app.post("/Producto_srv", response_model=dict)
async def create_producto(name: str, precio: float, stock: int, db: Session = Depends(get_db)):
    result = Producto_srv.add_new_producto(precio, stock, name, db)
    return result

# UPDATE PRODUCTO
@app.put("/Producto_srv/{producto_id}", response_model=dict)
async def update_producto(producto_id: int, precio: float, stock: int, db: Session = Depends(get_db)):
    result = Producto_srv.update_producto(producto_id, precio, stock, db)
    return result

# UPDATE PRODUCTO -- PRECIO
@app.put("/Producto_srv/precio/{producto_id}", response_model=dict)
async def update_producto_precio(producto_id: int, precio: float, db: Session = Depends(get_db)):
    result = Producto_srv.update_producto_precio(producto_id, precio, db)
    return result

# UPDATE PRODUCTO -- STOCK
@app.put("/Producto_srv/stock/{producto_id}", response_model=dict)
async def update_producto_stock(producto_id: int, stock: int, db: Session = Depends(get_db)):
    result = Producto_srv.update_producto_stock(producto_id, stock, db)
    return result

# DELETE PRODUCTO
@app.delete("/Producto_srv/{producto_id}", response_model=dict)
async def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    result = Producto_srv.delete_producto(producto_id, db)
    return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# GET PEDIDO
@app.get("/Pedido_srv", response_model=List[Pedido])
async def get_pedido(db: Session = Depends(get_db)):
    pedido = Pedido_srv.get_pedido(db)
    return pedido
# GET PEDIDO -- ID
@app.get("/Pedido_srv/{pedido_id}", response_model=Pedido)
async def get_pedido_by_id(pedido_id: int, db: Session = Depends(get_db)):
    pedido = Pedido_srv.get_pedido_by_id(pedido_id, db)
    if not pedido:
        return {"message": f"No existe pedido con la id {pedido_id}"}
    return pedido

# CREATE PEDIDO
@app.post("/Pedido_srv", response_model=dict)
async def create_pedido(id_cliente: int,id_producto: int, db: Session = Depends(get_db)):
    result = Pedido_srv.add_new_pedido(id_cliente=id_cliente, id_producto=id_producto, db=db)
    return result

# UPDATE PEDIDO -- ESTADO
@app.put("/Pedido_srv/estado/{pedido_id}", response_model=dict)
async def update_pedido_estado(pedido_id: int, estado: EstadoPedido, db: Session = Depends(get_db)):
    result = Pedido_srv.update_pedido_estado(pedido_id, estado, db)
    return result

# DELETE PEDIDO
@app.delete("/Pedido_srv/{pedido_id}", response_model=dict)
async def delete_pedido(pedido_id: int, db: Session = Depends(get_db)):
    result = Pedido_srv.delete_pedido(pedido_id, db)
    return result