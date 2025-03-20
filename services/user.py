from requests import session
from sqlalchemy import Engine

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
    return {"Message":"Created user Succesfully"}

async def update_user():
        with Session(Engine) as session:
            statement = select(User).where(User.name == "Spider-Boy")
            results = session.exec(statement)
            return {"Message": "Updated Succesfully"}

            session.add(user)
            session.commit()