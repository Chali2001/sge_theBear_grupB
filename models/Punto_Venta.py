from sqlmodel import SQLModel, Field
from typing import Optional
from models import Factura
from models import Pedido
from typing import Optional

class Punto_Venta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_pedido: int
    reserva: bool
    id_factura: Optional[int] = Field(default=None, foreign_key="factura.id")

