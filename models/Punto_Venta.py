from sqlmodel import SQLModel, Field
from typing import Optional
from models import Factura
from typing import Optional

class Punto_Venta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_pedido: Optional[int] = Field(default=None)
    reserva: bool = Field(default=False)
    id_factura: Optional[int] = Field(default=None, foreign_key="factura.id")



