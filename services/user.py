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


def update_user_email(user_id: int, email: str, db: Session):
    # Select the user to modify
    query = db.select(User).where(User.id == user_id)
    result = db.exec(query)
    user_to_update = result.one()

    # Update the email
    user_to_update.email = email
    db.add(user_to_update)
    db.commit()
    db.refresh(user_to_update)

    return {"id": user_to_update.id, "name": user_to_update.name, "email": user_to_update.email}