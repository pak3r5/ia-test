from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.sql_app.database import get_db
from app.schemas.user_schema import UserSchema
from app.services.user_service import get_user_id, create_user, get_user_by_username, change_user

router = APIRouter()


@router.post("/", response_model=UserSchema, status_code=201)
def new_user(body: UserSchema, db: Session = Depends(get_db)):
    """
        API Endpoint for Create new user
    """
    return create_user(db, body)


@router.get("/{user_id}", response_model=UserSchema, status_code=200)
def search_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
        API Endpoint for Get user by id
    """
    return get_user_id(db, user_id)


@router.get("", response_model=UserSchema, status_code=200)
def search_user_by_username(username: str, db: Session = Depends(get_db)):
    """
        API Endpoint for Get user by username
    """
    return get_user_by_username(db, username)


@router.put("/{user_id}", response_model=UserSchema, status_code=200)
def edit_user(user_id: int, body: UserSchema, db: Session = Depends(get_db)):
    """
        API Endpoint for Update user
    """
    return change_user(user_id, db, body)