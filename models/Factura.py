from sqlmodel import SQLModel, Field
from datetime import date
from enum import Enum

class EstadoFactura(str, Enum):
    pendiente = "pendiente"
    pagada = "pagada"
    cancelada = "cancelada"


class Factura(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    costo: float
    fecha: str
    estado: EstadoFactura


