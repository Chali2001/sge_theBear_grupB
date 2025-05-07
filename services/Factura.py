from sqlmodel import Session, select
from models.Factura import Factura, EstadoFactura
from datetime import date

# GET DE FACTURAS
def get_all_facturas(db: Session):
    sql_read = select(Factura)
    facturas = db.exec(sql_read).all()
    return facturas

def get_factura(id: int, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    return factura_db

# CREATE FACTURA
def add_new_factura(costo: float, fecha: str, estado: EstadoFactura, db: Session):
    new_factura = Factura(costo=costo, fecha=fecha, estado=estado)
    db.add(new_factura)
    db.commit()
    db.refresh(new_factura)
    return {"message": "Invoice created successfully"}

# UPDATE FACTURA
def update_factura(id: int, costo: float, fecha: str, estado: EstadoFactura, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()

    factura_db.costo = costo
    factura_db.fecha = fecha
    factura_db.estado = estado
    db.add(factura_db)
    db.commit()
    return {"message": "Invoice updated successfully"}

def update_factura_costo(id: int, costo: float, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()

    factura_db.costo = costo
    db.add(factura_db)
    db.commit()
    return {"message": "Invoice cost updated successfully"}

def update_factura_fecha(id: int, fecha: str, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()

    factura_db.fecha = fecha
    db.add(factura_db)
    db.commit()
    return {"message": "Invoice date updated successfully"}

def update_factura_estado(id: int, estado: EstadoFactura, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()

    factura_db.estado = estado
    db.add(factura_db)
    db.commit()
    return {"message": "Invoice status updated successfully"}

# DELETE FaCTURA
def delete_factura(id: int, db: Session):
    sql_select = select(Factura).where(Factura.id == id)
    factura_db = db.exec(sql_select).one()
    db.delete(factura_db)
    db.commit()
    return {"message": "Invoice deleted successfully"}
