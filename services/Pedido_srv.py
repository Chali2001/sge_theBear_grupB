from sqlmodel import Session, select
from models.Pedido_mdl import Pedido, EstadoPedido
#from models.Cliente_mdl import Cliente
from models.Producto_mdl import Producto
from datetime import date

# GET TODOS LOS PEDIDOS
def get_all_pedido(db: Session):
    sql_read = select(Pedido)
    pedidos = db.exec(sql_read).all()
    return pedidos

# GET PEDIDO
def get_pedido_by_id(db: Session, pedido_id: int):
    statement = select(Pedido).where(Pedido.id == pedido_id)
    result = db.exec(statement).first()
    return result

# CREATE PEDIDO
def add_new_pedido( id_producto: int, db: Session): # poner id_cliente -----------------------------------------------------
    # Verificar si el cliente existe
    #cliente = db.exec(select(Cliente).where(Cliente.id == id_cliente)).first()
    #if not cliente:
    #    return {"message": "Cliente no encontrado", "success": False}

    # Verificar si el producto existe
    producto = db.exec(select(Producto).where(Producto.id == id_producto)).first()
    if not producto:
        return {"message": "Producto no encontrado", "success": False}

    # Crear el nuevo pedido
    new_pedido = Pedido(id_producto=id_producto) # poner el id_cliente -----------------------------------------------------
    db.add(new_pedido)
    db.commit()
    db.refresh(new_pedido)
    return {"message": "Pedido creado correctamente", "id": new_pedido.id, "success": True}


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
    pedido_db = db.exec(sql_select).one()
    db.delete(pedido_db)
    db.commit()
    return {"message": "Pedido eliminado correctamente"}
