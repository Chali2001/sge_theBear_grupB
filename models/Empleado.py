from sqlmodel import SQLModel, Field

class Empleado(SQLModel, table = True):
    ID_empleado: int = Field(default=None, primary_key=True)
    nombre: str
    cargo: str
    ss: int
    sueldo: int