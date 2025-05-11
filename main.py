from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from datetime import date,time
from typing import Optional
from models.Factura import EstadoFactura
from services import Punto_Venta, Factura
import os
from pydantic import BaseModel
from models.Pedido_mdl import EstadoPedido, Pedido
from models.Producto_mdl import Producto
from services import Pedido_srv, Producto_srv
from schema.Producto_sch import productos_schema
from schema.Pedido_sch import pedidos_schema
from models.evento import Assistencia
from services.eventos import get_all_eventos, get_evento, add_new_evento, update_evento, update_evento_fecha_hora, delete_evento


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


class PuntoVentaCreate(BaseModel):
    id_pedido: Optional[int] = None
    reserva: bool = False
    id_factura: Optional[int] = None

class ReservaRequest(BaseModel):
    reserva: bool

# CRUD DE PUNTO DE VENTA

# GET PUNTO DE VENTA
@app.get("/puntoVenta/getAll", response_model=List[dict])
async def read_punto_venta (db:Session = Depends(get_db)):
    result = Punto_Venta.get_all_punts(db)
    return result

@app.get("/puntoVenta/{id}", response_model=dict)
async def read_puntoVenta_id(id: int, db:Session = Depends(get_db)):
    result = Punto_Venta.get_punto(id, db)
    return result

# CREATE PUNTO DE VENTA
@app.post("/puntoVenta/add", response_model=dict)
async def create_punto_venta(punto: PuntoVentaCreate, db: Session = Depends(get_db)):
    result = Punto_Venta.add_new_punto(punto.id_pedido, punto.reserva, punto.id_factura, db)
    return result

# UPDATE PUNTO DE VENTA
@app.put("/puntoVenta/update/{id}", response_model=dict)
async def update_puntoVenta(id: int, id_pedido: Optional[int] = None, reserva: bool = False, id_factura: Optional[int] = None, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto(id, id_pedido, reserva, id_factura, db)
    return result

@app.put("/puntoVenta/update/reserva/{id}", response_model=dict)
async def update_puntoVenta_reserva(id: int, reserva_request: ReservaRequest, db: Session = Depends(get_db)):
    result = Punto_Venta.update_punto_reserva(id, reserva_request.reserva, db)
    return result


@app.put("/puntoVenta/update/id_factura/{id}", response_model=dict)
async def update_puntoVenta_id_factura(id: int, id_factura: int, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto_id_factura(id, id_factura, db)
    return result

@app.put("/puntoVenta/update/id_pedido/{id}", response_model=dict)
async def update_puntoVenta_id_pedido(id: int, id_pedido: int, db:Session = Depends(get_db)):
    result = Punto_Venta.update_punto_id_pedido(id, id_pedido, db)
    return result

# DELETE PUNTO DE VENTA
@app.delete("/puntoVenta/delete/{id}", response_model=dict)
async def delete_punto(id: int, db: Session = Depends(get_db)):
    resultat = Punto_Venta.delete_punto(id, db)
    return resultat


# CRUD DE FACTURA

# GET FACTURA
@app.get("/factura/getAll", response_model=List[dict])
async def read_factura(db:Session = Depends(get_db)):
    result = Factura.get_all_facturas(db)
    return result

@app.get("/factura/{id}", response_model=dict)
async def read_factura_id(id: int, db:Session = Depends(get_db)):
    result = Factura.get_factura(id, db)
    return result




# CREATE FACTURA
class FacturaCreate(BaseModel):
    costo: float
    fecha: date
    estado: EstadoFactura

class EstadoFacturaInput(BaseModel):
    estado: EstadoFactura

@app.post("/factura/add", response_model=dict)
async def add_new_factura(factura: FacturaCreate, db: Session = Depends(get_db)):
    result = Factura.add_new_factura(factura.costo, factura.fecha, factura.estado, db)
    return result

# UPDATE FACTURA
@app.put("/factura/update/{id}", response_model=dict)
async def update_factura(id: int, costo: float, fecha: date, estado: EstadoFactura, db:Session = Depends(get_db)):
    result = Factura.update_factura(id, costo, fecha, estado, db)
    return result

@app.put("/factura/update/costo/{id}", response_model=dict)
async def update_factura_costo(id: int, costo: float, db:Session = Depends(get_db)):
    result = Factura.update_factura_costo(id, costo, db)
    return result

@app.put("/factura/update/fecha/{id}", response_model=dict)
async def update_factura_fecha(id: int, fecha: date, db:Session = Depends(get_db)):
    result = Factura.update_factura_fecha(id, fecha, db)
    return result

@app.put("/factura/update/estado/{id}", response_model=dict)
async def update_factura_estado(id: int, estado_input: EstadoFacturaInput, db: Session = Depends(get_db)):
    result = Factura.update_factura_estado(id, estado_input.estado, db)
    return result

# DELETE FACTURA
@app.delete("/factura/delete/{id}", response_model=dict)
async def delete_factura(id: int, db:Session = Depends(get_db)):
    result = Factura.delete_factura(id, db)
    return result


# PARTE DE IZAN
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

# PARTE DE CHALI
# Ruta GET para obtener todos los eventos
@app.get("/eventos")
def leer_eventos(db: Session = Depends(get_db)):
    #Llama la funcion que muestra todos los eventos
    return get_all_eventos(db)

# Ruta GET para obtener el evento con el id introducido
@app.get("/eventos/{id}")
# Recibe un ID para introducir en la funcion
def leer_evento(id: int, db: Session = Depends(get_db)):
    #Llama la funcion que muestra el evento del id introducido
    return get_evento(id, db)

# Ruta POST para crear un evento con todos los atributos
@app.post("/eventos")
def crear_evento(fecha: date, asiste: Assistencia, hora: time, direccion: str, id_empleado: int, db: Session = Depends(get_db)):
    # Llama la funcion que crea el evento
    return add_new_evento(fecha, asiste, hora, direccion, id_empleado, db)

# Ruta PUT para actualizar los datos del evento del ID introducido
@app.put("/eventos")
def actualizar_evento(id: int, fecha: date, asiste: Assistencia, hora: time, direccion: str, id_empleado: int, db: Session = Depends(get_db)):
    # Llama la funcion que actualiza el evento del id introducido
    return update_evento(id, fecha, asiste, hora, direccion, id_empleado, db)

# Ruta PUT para actualizar la fecha y hora del evento del ID introducido
@app.put("/eventos/{id}")
def actualizar_evento_fecha_hora(id: int, fecha :date, hora: time, db: Session = Depends(get_db)):
    # Llama la funcion que actualiza el evento del id introducido pero solo la fecha y hora
    return update_evento_fecha_hora(id, fecha, hora, db)

# Ruta DELETE para eliminar el evento del id introducido
@app.delete("/eventos/{id}")
def borrar_evento(id: int, db: Session = Depends(get_db)):
    # Llama la funcion que elimina el evento con el id introducido
    return delete_evento(id, db)