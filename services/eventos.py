from sqlmodel import Session, select
from models.evento import Evento, Assistencia
from datetime import date, time
from schema.eventos import eventos_schema

# GET DE EVENTOS
def get_all_eventos(db: Session):
    #Realiza una consulta a la base de datos
    sql_read = select(Evento)
    #Ejecuta la consulta y recupera los eventos
    eventos = db.exec(sql_read).all()
    #Si no hay eventos sale "Sin Eventos"
    if not eventos:
        return {"message": "Sin Eventos"}
    #Si hay eventos se muestra con la adaptacion de schema
    return eventos_schema(eventos)

def get_evento(id: int, db: Session):
    # Verificamos si el ID es valido
    if id <= 0:
        return {"message": "Valor introducido incorrecto"}
    # Buscamos el evento en la base de datos que coincida el id introduucido con el id del evento
    sql_select = select(Evento).where(Evento.id_evento == id)
    evento_db = db.exec(sql_select).all()
    # Si no se encuentra el evento, sale que no existe
    if not evento_db:
        return {"message": "ID de Evento inexistente"}
    # Si se encuentra el evento, lo mostramos
    return eventos_schema(evento_db)

# CREA UN EVENTO
def add_new_evento(fecha: date, asiste: Assistencia, hora: time, direccion: str, id_empleado: int, db: Session):
    # Crear un nuevo evento con los parámetros introducidos
    new_evento = Evento(fecha=fecha, asiste=asiste, hora=hora, direccion=direccion, id_empleado=id_empleado)
    # Añadir el evento a la base de datos
    db.add(new_evento)
    # Guarda el cambio en la base de datos
    db.commit()
    # Actualiza los datos
    db.refresh(new_evento)
    # Sale un mensaje de confirmación
    return {"message": "Evento creado correctamente", "id_evento": new_evento.id_evento}


# UPDATE EVENTO
def update_evento(id: int, fecha: date, asiste: Assistencia, hora: time, direccion: str, id_empleado: int, db: Session):
    # Seleccionamos el evento por su id
    sql_select = select(Evento).where(Evento.id_evento == id)
    evento_db = db.exec(sql_select).one()
    if evento_db:  # Verificamos que el evento exista
        # Actualizamos los campos del evento
        evento_db.fecha = fecha
        evento_db.asiste = asiste
        evento_db.hora = hora
        evento_db.direccion = direccion
        evento_db.id_empleado = id_empleado
        # Guardamos los cambios
        db.add(evento_db)
        db.commit()
        # Ponemos mensaje de confirmación
        return {"message": "Evento actualizado correctamente"}
    #En caso de que no exista el id
    else:
        return {"message": "Evento no encontrado"}

# UPDATE EVENTO DE FECHA Y HORA
def update_evento_fecha_hora(id: int, fecha: date, hora:time, db: Session):
    # Seleccionamos el evento por su id
    sql_select = select(Evento).where(Evento.id_evento == id)
    evento_db = db.exec(sql_select).one()
    if evento_db:
        # Actualizamos solos los campos descritos
        evento_db.fecha = fecha
        evento_db.hora = hora
        db.add(evento_db)
        db.commit()
        return {"message": "Fecha y hora del Evento actualizado"}
    else:
        return {"message": "Evento no encontrado"}


# DELETE EVENTO
def delete_evento(id: int, db: Session):
    # Seleccionamos el evento por su id_evento
    sql_select = select(Evento).where(Evento.id_evento == id)
    evento_db = db.exec(sql_select).first()
    if evento_db:  # Verificamos que el evento exista
        # Eliminamos el evento
        db.delete(evento_db)
        db.commit()
        # Mensaje de confirmación
        return {"message": "Evento eliminado correctamente"}
    # En caso de que el evento no exista
    else:
        return {"message": "Evento no encontrado"}