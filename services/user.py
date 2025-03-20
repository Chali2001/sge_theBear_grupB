from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name: str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message":"Created user succesfully"}

def update_user(user_id: int, name: str, email: str, db: Session):
    db_user = db.exec(select(User).where(User.id == user_id)).first()
    db_user.name = name
    db_user.email = email
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message":"User update succesfully"}


def delete_user(user_id: int, db: Session):
    db_user = db.exec(select(User).where(User.id == user_id)).first()
    db.delete(db_user)
    db.commit()
    return {"message":"User delete succesfully"}