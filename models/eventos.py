from sqlmodel import SQLModel, Field
from datetime import date
from enum import Enum

class EstadoEvento(str, Enum):
    activo = "activo"
    finalizado = "finalizado"
    cancelado = "cancelado"

class Evento(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    fecha: date
    lugar: str
    estado: EstadoEvento