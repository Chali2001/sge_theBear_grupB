from sqlmodel import Session, select
from models.Evento import Evento, EstadoEvento
from datetime import date

# GET DE EVENTOS
def get_all_eventos(db: Session):
    sql_read = select(Evento)
    eventos = db.exec(sql_read).all()
    return eventos

def get_evento(id: int, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()
    return evento_db

# CREATE EVENTO
def add_new_evento(nombre: str, fecha: date, lugar: str, estado: EstadoEvento, db: Session):
    new_evento = Evento(nombre=nombre, fecha=fecha, lugar=lugar, estado=estado)
    db.add(new_evento)
    db.commit()
    db.refresh(new_evento)
    return {"message": "Event created successfully"}

# UPDATE EVENTO
def update_evento(id: int, nombre: str, fecha: date, lugar: str, estado: EstadoEvento, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()

    evento_db.nombre = nombre
    evento_db.fecha = fecha
    evento_db.lugar = lugar
    evento_db.estado = estado
    db.add(evento_db)
    db.commit()
    return {"message": "Event updated successfully"}

def update_evento_nombre(id: int, nombre: str, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()

    evento_db.nombre = nombre
    db.add(evento_db)
    db.commit()
    return {"message": "Event name updated successfully"}

def update_evento_fecha(id: int, fecha: date, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()

    evento_db.fecha = fecha
    db.add(evento_db)
    db.commit()
    return {"message": "Event date updated successfully"}

def update_evento_lugar(id: int, lugar: str, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()

    evento_db.lugar = lugar
    db.add(evento_db)
    db.commit()
    return {"message": "Event location updated successfully"}

def update_evento_estado(id: int, estado: EstadoEvento, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()

    evento_db.estado = estado
    db.add(evento_db)
    db.commit()
    return {"message": "Event status updated successfully"}

# DELETE EVENTO
def delete_evento(id: int, db: Session):
    sql_select = select(Evento).where(Evento.id == id)
    evento_db = db.exec(sql_select).one()
    db.delete(evento_db)
    db.commit()
    return {"message": "Event deleted successfully"}
