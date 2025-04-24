from schema.puntoVenta_sch import puntos_schema
from sqlmodel import Session, select
from models.Punto_Venta import Punto_Venta

def get_all_punts(db:Session):
    sql_read = select(Punto_Venta)
    punts = db.exec(sql_read).all()