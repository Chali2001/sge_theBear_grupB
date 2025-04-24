from sqlmodel import SQLModel, Field
from typing import Optional
from models import Factura
from models import Pedido

class Punto_Venta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_pedido: int
    reserva: bool
    id_factura: int


