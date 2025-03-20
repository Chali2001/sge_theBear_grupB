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
    # Select the user to update
    statement = select(User).where(User.id == user_id)  # Assuming User is your SQLModel class
    results = db.exec(statement)
    user_to_update = results.one()

    # Update the email
    user_to_update.email = email
    db.add(user_to_update)
    db.commit()
    db.refresh(user_to_update)

    return {
        "id": user_to_update.id,
        "name": user_to_update.name,
        "email": user_to_update.email
    }


def delete_user_by_id(user_id: int, db: Session):
    # Select the user to delete
    statement = select(User).where(User.id == user_id)  # Assuming User is your SQLModel class
    results = db.exec(statement)
    user_to_delete = results.one_or_none()

    # Check if user exists
    if user_to_delete is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Delete the user
    db.delete(user_to_delete)
    db.commit()

    # Return confirmation
    return {
        "message": "User deleted successfully",
        "id": user_id
    }