
from schema.empleados_sch import empleados_schema
from sqlmodel import Session, select
from models.Empleado import Empleado
from schema.empleados_sch import empleado_schema
def get_all_empleados(db:Session):
    sql_read = select(Empleado)
    empleados = db.exec(sql_read).all()
    return empleados_schema(empleados)


def get_one_empleado(ID_empleado: int, db:Session):
    sql_read = select(Empleado).where(Empleado.ID_empleado == ID_empleado)
    empleado = db.exec(sql_read).all()
    return  empleado_schema(empleado)

def add_new_empleado(ID_empleado: int, nombre: str, cargo: str, ss: int, sueldo: int, db:Session):
    db_empleado = Empleado(ID_empleado = ID_empleado, nombre = nombre, cargo = cargo, ss = ss, sueldo = sueldo)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return {"msg": "Empleado Creado"}

def update_empleado(ID_empleado: int, nombre: str, cargo: str, ss: int, sueldo: int, db:Session):
    sql_select = select(Empleado).where(Empleado.ID_empleado == ID_empleado)
    empleado_db = db.exec(sql_select).one()

    empleado_db.nombre = nombre
    empleado_db.ID_empleado = ID_empleado
    empleado_db.cargo = cargo
    empleado_db.ss = ss
    empleado_db.sueldo = sueldo
    db.add(empleado_db)
    db.commit()
    return {"msg":"Empleado Actulizado Correctamente"}


def delete_empleado(id:int, db:Session):
    sql_select = select(Empleado).where(Empleado.ID_empleado == id)
    empleado_db = db.exec(sql_select).one()

    db.delete(empleado_db)
    db.commit()
    return {"msg": "Empleado Eliminado"}
