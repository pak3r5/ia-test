from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.user import select_user_by_id, insert_user, select_user_by_username, update_user
from app.models.entities.user import User
from app.schemas.user_schema import UserSchema


def get_user_id(db: Session, id: int):
    get = select_user_by_id(db, id)
    if get:
        return transform_model_to_schema(get)
    raise HTTPException(status_code=404, detail="User not found")


def create_user(db: Session, user: UserSchema):
    get_product = select_user_by_username(db, user.username)
    if get_product:
        raise HTTPException(status_code=409, detail="User already registered")
    new_user = User(name=user.name, last_name=user.last_name, username=user.username, password=user.password)
    return transform_model_to_schema(insert_user(db, new_user))


def get_user_by_username(db: Session, username: str):
    get = select_user_by_username(db, username)
    if get:
        return transform_model_to_schema(get)
    raise HTTPException(status_code=404, detail="User not found")


def change_user(id: int, db: Session, user: UserSchema):
    get_user = select_user_by_id(db, id)
    if get_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    get_user.name = user.name
    get_user.last_name = user.last_name
    # get_user.username = user.username
    get_user.password = user.password
    return transform_model_to_schema(update_user(db, get_user))


def transform_model_to_schema(get: User):
    return UserSchema(name=get.name, last_name=get.last_name, username=get.username, password=get.password)