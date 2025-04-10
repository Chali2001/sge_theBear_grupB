from schema.empleados_sch import empleados_schema
from sqlmodel import Session, select
from models.Empleado import Empleado

def get_all_empleados(db:Session):
    sql_read = select(Empleado)
    empleados = db.exec(sql_read).all()
    return empleados_schema(empleados)