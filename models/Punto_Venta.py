from sqlmodel import SQLModel, Field
from typing import Optional
from models import Factura
from models import Pedido

class Punto_Venta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_pedido: Field(default=None, foreign_key="pedido.n_pedido")
    reserva: bool
    id_factura: Optional[int] = Field(default=None, foreign_key="factura.id")


