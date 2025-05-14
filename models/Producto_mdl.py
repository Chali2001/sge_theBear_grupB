from sqlmodel import SQLModel, Field

class Producto(SQLModel, table=True):
    __tablename__ = "producto"

    id: int = Field(default=None, primary_key=True)
    name: str
    stock: int
    precio: float