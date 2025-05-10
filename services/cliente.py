from schema.clientes_sch import clientes_schema
from sqlmodel import Session, select
from models.Cliente import Cliente
from schema.empleados_sch import empleado_schema
def get_all_clientes(db:Session):
    sql_read = select(Cliente)
    clientes = db.exec(sql_read).all()
    return clientes_schema(clientes)


def get_one_cliente(ID_cliente: int, db:Session):
    sql_read = select(Cliente).where(Cliente.ID_cliente == ID_cliente)
    cliente = db.exec(sql_read).all()
    return  clientes_schema(cliente)

def add_new_cliente(ID_cliente: int, nombre: str, telefono: str, db:Session):
    db_cliente = Cliente(ID_cliente = ID_cliente, nombre = nombre, telefono = telefono)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return {"msg": "Cliente Creado"}

def update_cliente(ID_cliente: int, nombre: str, telefono: str, db:Session):
    sql_select = select(Cliente).where(Cliente.ID_cliente == ID_cliente)
    cliente_db = db.exec(sql_select).one()

    cliente_db.nombre = nombre
    cliente_db.ID_cliente = ID_cliente
    cliente_db.telefono = telefono
    db.add(cliente_db)
    db.commit()
    return {"msg":"Cliente Actulizado Correctamente"}


def delete_cliente(id:int, db:Session):
    sql_select = select(Cliente).where(Cliente.ID_cliente == id)
    cliente_db = db.exec(sql_select).one()

    db.delete(cliente_db)
    db.commit()
    return {"msg": "Cliente Eliminado"}


