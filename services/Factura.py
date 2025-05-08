from sqlmodel import Session, select
from models.Factura import Factura, EstadoFactura
from datetime import date
from schema.factura_sch import facturas_schema, factura_schema

# GET DE FACTURAS
def get_all_facturas(db: Session):
    sql_read = select(Factura)
    facturas = db.exec(sql_read).all()
    if not facturas:
        return {"message":"No hay facturas creadas"}
    return facturas_schema(facturas)

def get_factura(id: int, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    if not factura_db:
        return {"message":f"No existe factura con la id {id}"}

    return factura_schema(factura_db)

# CREATE FACTURA
def add_new_factura(costo: float, fecha: date, estado: EstadoFactura, db: Session):
    new_factura = Factura(costo=costo, fecha=fecha, estado=estado)
    db.add(new_factura)
    db.commit()
    db.refresh(new_factura)
    return {"message": f"Factura creada correctamente con id: {new_factura.id}"}

# UPDATE FACTURA
def update_factura(id: int, costo: float, fecha: str, estado: EstadoFactura, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    if not factura_db:
        return {"message":f"No existe factura con la id {id}"}

    factura_db.costo = costo
    factura_db.fecha = fecha
    factura_db.estado = estado
    db.add(factura_db)
    db.commit()
    return {"message": "Factura actualizada correctamente"}

def update_factura_costo(id: int, costo: float, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    if not factura_db:
        return {"message":f"No existe factura con la id {id}"}

    factura_db.costo = costo
    db.add(factura_db)
    db.commit()
    return {"message": "Costo de la factura actualizado"}

def update_factura_fecha(id: int, fecha: str, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    if not factura_db:
        return {"message":f"No existe factura con la id {id}"}

    factura_db.fecha = fecha
    db.add(factura_db)
    db.commit()
    return {"message": "Fecha de la factura actualizada"}

def update_factura_estado(id: int, estado: EstadoFactura, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    if not factura_db:
        return {"message":f"No existe factura con la id {id}"}

    factura_db.estado = estado
    db.add(factura_db)
    db.commit()
    return {"message": "Estado de la factura actualizado"}

# DELETE FaCTURA
def delete_factura(id: int, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    if not factura_db:
        return {"message":f"No existe factura con la id {id}"}
    db.delete(factura_db)
    db.commit()
    return {"message": "Factura eliminada correctamente"}
