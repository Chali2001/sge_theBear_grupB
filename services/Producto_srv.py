from sqlmodel import Session, select
from models.Producto_mdl import Producto

# GET DE PRODUCTOS
def get_all_productos(db: Session):
    sql_read = select(Producto)
    producto = db.exec(sql_read).all()
    return producto

def get_producto_by_id(db: Session, producto_id: int):
    statement = select(Producto).where(Producto.id == producto_id)
    result = db.exec(statement).first()
    return result

# CREATE PRODUCTO
def add_new_producto(precio: float, stock: int, name: str, db: Session):
    new_Producto = Producto(name=name, stock=stock, precio=precio)
    db.add(new_Producto)
    db.commit()
    db.refresh(new_Producto)
    return {"message": "Product created successfully"}

# UPDATE PRODUCTO
def update_producto(id: int, precio: float, stock: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()

    producto_db.precio = precio
    producto_db.stock = stock
    db.add(producto_db)
    db.commit()
    return {"message": "Product updated successfully"}

# UPDATE PRODUCTO -- PRECIO
def update_producto_precio(id: int, precio: float, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()

    producto_db.precio = precio
    db.add(producto_db)
    db.commit()
    return {"message": "Product cost updated successfully"}

# UPDATE PRODUCTO -- STOCK
def update_producto_stock(id: int, stock: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()
    producto_db.stock = stock
    db.add(producto_db)
    db.commit()
    return {"message": "Product stock updated successfully"}

# DELETE PRODUCTO
def delete_producto(id: int, db: Session):
    sql_select = select(Producto).where(Producto.id == id)
    producto_db = db.exec(sql_select).one()
    db.delete(producto_db)
    db.commit()
    return {"message": "Product deleted successfully"}