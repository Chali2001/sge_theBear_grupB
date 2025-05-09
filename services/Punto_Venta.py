from schema.puntoVenta_sch import puntos_schema
from sqlmodel import Session, select
from models.Punto_Venta import Punto_Venta
from models.Factura import Factura
from schema.puntoVenta_sch import puntos_schema, punto_schema

# GET PUNTO DE VENTA
def get_all_punts(db:Session):
    sql_read = select(Punto_Venta)
    puntos = db.exec(sql_read).all()
    if not puntos:
        return {"message":"Puntos de venta no creados"}
    return puntos_schema(puntos)

def get_punto(id: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).all()
    if not punto_db:
        return {"message":f"No existe punto de venta con la id {id}"}
    punto_db = db.exec(sql_select).one()
    return punto_schema(punto_db)

# CREATE PUNTO DE VENTA
def add_new_punto(id_pedido: int, reserva: bool, id_factura: int, db:Session):
    if id_pedido is None:
        id_pedido = 0
    # Comprobamos que la id de factura correspond a una factura
    sql_select = select(Factura).where(Factura.id == id_factura)
    factura_db = db.exec(sql_select).all()
    if not factura_db:
        return {"message":f"No existe factura con la id {id_factura}"}

    db_punto = Punto_Venta(id_pedido=id_pedido, reserva=reserva, id_factura=id_factura)
    db.add(db_punto)
    db.commit()
    db.refresh(db_punto)
    return {"message": f"Punto de venta creado con la id: {db_punto.id}"}

# UPDATE PUNTO DE VENTA
def update_punto(id: int, id_pedido: int, reserva: bool, id_factura: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).all()
    if not punto_db:
        return {"message":f"No existe punto de venta con la id {id}"}
    punto_db = db.exec(sql_select).one()

    # Comprobamos que la id de factura correspond a una factura
    sql_select = select(Factura).where(Factura.id == id_factura)
    factura_db = db.exec(sql_select).all()
    if not factura_db:
        return {"message":f"No existe factura con la id {id_factura}"}

    punto_db.id_pedido = id_pedido
    punto_db.reserva = reserva
    punto_db.id_factura = id_factura
    db.add(punto_db)
    db.commit()
    return {"message": "Punto de venta actualizado"}

def update_punto_reserva(id: int, reserva: bool, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).all()
    if not punto_db:
        return {"message":f"No existe punto de venta con la id {id}"}
    punto_db = db.exec(sql_select).one()

    punto_db.reserva = reserva
    db.add(punto_db)
    db.commit()
    return {"message": "Reserva del Punto de venta actualizado"}

def update_punto_id_factura(id: int, id_factura: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).all()
    if not punto_db:
        return {"message":f"No existe punto de venta con la id {id}"}
    punto_db = db.exec(sql_select).one()

    # Comprobamos que la id de factura correspond a una factura
    sql_select = select(Factura).where(Factura.id == id_factura)
    factura_db = db.exec(sql_select).all()
    if not factura_db:
        return {"message":f"No existe factura con la id {id_factura}"}


    punto_db.id_factura = id_factura
    db.add(punto_db)
    db.commit()
    return {"message": "Factura del Punto de venta actualizado"}

def update_punto_id_pedido(id: int, id_pedido: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).all()
    if not punto_db:
        return {"message":f"No existe punto de venta con la id {id}"}
    punto_db = db.exec(sql_select).one()

    punto_db.id_pedido = id_pedido
    db.add(punto_db)
    db.commit()
    return {"message": "Pedido del Punto de venta actualizado"}

# DELETE PUNTO DE VENTA
def delete_punto(id: int, db:Session):
    sql_select = select(Punto_Venta).where(Punto_Venta.id == id)
    punto_db = db.exec(sql_select).one()
    if not punto_db:
        return {"message":f"No existe punto de venta con la id {id}"}

    db.delete(punto_db)
    db.commit()
    return {"Message": "Punto de venta eliminado correctamente"}

