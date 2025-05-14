from sqlmodel import Session, select
from models.Producto_mdl import Producto


# GET DE PRODUCTOS
def get_producto(db: Session):
    sql_read = select(Producto)
    producto = db.exec(sql_read).all()
    if not producto:
        return {"message":"No hay productos creados"}
    return producto

def get_producto_by_id(id: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).first()
    if not producto_db:
        return {"message":f"No existe producto con la id {id}"}
    return producto_db

# CREATE PRODUCTO
def add_new_producto(precio: float, stock: int, name: str, db: Session):
    new_Producto = Producto(name=name, stock=stock, precio=precio)
    db.add(new_Producto)
    db.commit()
    db.refresh(new_Producto)
    return {"message": "Producto creado correctamente", "id": new_Producto.id}

# UPDATE PRODUCTO
def update_producto(id: int, precio: float, stock: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()

    producto_db.precio = precio
    producto_db.stock = stock
    db.add(producto_db)
    db.commit()
    return {"message": "Producto actualizado correctamente"}

# UPDATE PRODUCTO -- PRECIO
def update_producto_precio(id: int, precio: float, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()

    producto_db.precio = precio
    db.add(producto_db)
    db.commit()
    return {"message": "Precio del producto actualizado correctamente"}

# UPDATE PRODUCTO -- STOCK
def update_producto_stock(id: int, stock: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()
    producto_db.stock = stock
    db.add(producto_db)
    db.commit()
    return {"message": "Stock del producto actualizado correctamente"}

# DELETE PRODUCTO
def delete_producto(id: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).all()
    if not producto_db:
        return {"message":f"No existe producto con la id {id}"}
    producto_db = db.exec(sql_select).one()

    db.delete(producto_db)
    db.commit()
    return {"message": "Producto eliminado correctamente"}