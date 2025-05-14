from sqlmodel import SQLModel, Field
from datetime import date, time
from enum import Enum

# Creamos un desplegable con enum para el atributo asiste
class Assistencia(str, Enum):
    Si = "Si"
    Pendiente = "Pendiente"
    No = "No"
# Creamos la classe evento con sus atributos de id como primary_key
class Evento(SQLModel, table=True):
    id_evento: int = Field(default=None, primary_key=True)
    fecha: date
    asiste: Assistencia
    hora: time
    direccion: str
    id_empleado: int