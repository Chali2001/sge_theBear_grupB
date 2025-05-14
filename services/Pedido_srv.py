from sqlmodel import Session, select
from models.Pedido_mdl import Pedido, EstadoPedido
from models.Cliente import Cliente
from models.Producto_mdl import Producto


# GET TODOS LOS PEDIDOS
def get_pedido(db: Session):
    sql_read = select(Pedido)
    pedido = db.exec(sql_read).all()
    if not pedido:
        return {"message":"No hay pedidos creados"}
    return pedido

def get_pedido_by_id(id: int, db: Session):
    sql_select = select(Pedido).where(Pedido.id == id)
    pedido_db = db.exec(sql_select).first()
    if not pedido_db or pedido_db.id is None:
        return None
    return pedido_db

# CREATE PEDIDO
def add_new_pedido(id_cliente: int, id_producto: int, db: Session):
    # Verificar si el cliente existe
    cliente = db.exec(select(Cliente).where(Cliente.ID_cliente == id_cliente)).first()
    if not cliente:
       return {"message": "Cliente no encontrado"}

    # Verificar si el producto existe
    producto = db.exec(select(Producto).where(Producto.id == id_producto)).first()
    if not producto:
        return {"message": "Producto no encontrado"}

    # Crear el nuevo pedido
    new_pedido = Pedido(id_cliente=id_cliente,id_producto=id_producto)
    db.add(new_pedido)
    db.commit()
    db.refresh(new_pedido)
    return {"message": "Pedido creado correctamente", "id": new_pedido.id}


# UPDATE PEDIDO -- ESTADO
def update_pedido_estado(pedido_id: int, estado: EstadoPedido, db: Session):
    sql_select = select(Pedido).where(Pedido.id == pedido_id)
    pedido_db = db.exec(sql_select).one()
    pedido_db.estado = estado
    db.add(pedido_db)
    db.commit()
    return {"message": "Estado actualizado correctamente"}

# DELETE PEDIDO
def delete_pedido(id: int, db: Session):
    sql_select = select(Pedido).where(Pedido.id == id)
    pedido_db = db.exec(sql_select).all()
    if not pedido_db:
        return {"message":f"No existe pedido con la id {id}"}
    pedido_db = db.exec(sql_select).one()

    db.delete(pedido_db)
    db.commit()
    return {"message": "pedido eliminado correctamente"}