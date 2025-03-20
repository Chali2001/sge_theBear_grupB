from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name: str, email: str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Created user successfully"}

def update_user(name: str, newName: str,db:Session):
    statement = select(User).where(User.name == name)
    results = db.exec(statement)
    user = results.first()
    if user is None:
        return {"Message": "No encontrado"}
    user.name = newName
    db.add(user)
    db.commit()
    return {"Message": "user updated"}

def delete_user(id: int, db:Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.first()
    if user is None:
        return {"Message": "No encontrado"}
    db.delete(user)
    db.commit()
    return {"Message": "User deleted"}