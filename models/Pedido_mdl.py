from sqlmodel import SQLModel, Field
from datetime import date
from enum import Enum
from typing import Optional

class EstadoPedido(str, Enum):
    pendiente = "pendiente"
    entregado = "entregado"
    cancelada = "cancelada"
    enProceso = "enProceso"

class Pedido(SQLModel, table=True):
    __tablename__ = "pedido"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_cliente: Optional[int] = Field(default=None, foreign_key="cliente.ID_cliente")
    id_producto: Optional[int] = Field(default=None, foreign_key="producto.id")
    estado: EstadoPedido = Field(default=EstadoPedido.enProceso)
    fecha: date = Field(default_factory=date.today)