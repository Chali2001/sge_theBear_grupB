from sqlmodel import SQLModel, Field

class Cliente(SQLModel, table = True):
    ID_cliente: int = Field(default=None, primary_key=True)
    nombre: str
    telefono: str


