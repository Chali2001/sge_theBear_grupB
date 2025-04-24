from schema.puntoVenta_sch import puntos_schema
from sqlmodel import Session, select
from models.Punto_Venta import Punto_Venta

# GET PUNTO DE VENTA
def get_all_punts(db:Session):
    sql_read = select(Punto_Venta)
    punts = db.exec(sql_read).all()

def get_punto(id: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()
    return punto_db

# CREATE PUNTO DE VENTA
def add_new_punto(id_pedido: int, reserva: bool, id_factura: int, db:Session):
    db_user = Punto_Venta(id_pedido=id_pedido, reserva=reserva, id_factura=id_factura)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Point of sale created successfully"}

# UPDATE PUNTO DE VENTA
def update_punto(id: int, id_pedido: int, reserva: bool, id_factura: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()

    punto_db.id_pedido = id_pedido
    punto_db.reserva = reserva
    punto_db.id_factura = id_factura
    db.add(punto_db)
    db.commit()
    return {"Message": "Updated Point of sale succesfully"}

def update_punto_reserva(id: int, reserva: bool, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()

    punto_db.reserva = reserva
    db.add(punto_db)
    db.commit()
    return {"Message": "Updated Point of sale succesfully"}

def update_punto_id_factura(id: int, id_factura: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()

    punto_db.id_factura = id_factura
    db.add(punto_db)
    db.commit()
    return {"Message": "Updated Point of sale succesfully"}

def update_punto_id_pedido(id: int, id_pedido: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()

    punto_db.id_pedido = id_pedido
    db.add(punto_db)
    db.commit()
    return {"Message": "Updated Point of sale succesfully"}

# DELETE PUNTO DE VENTA
def delete_punto(id: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()
    db.delete(punto_db)
    db.commit()
    return {"Message": "Deleted Point of sale succesfully"}

