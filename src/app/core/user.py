from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.entities.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def select_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def select_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_login(db: Session, username: str, password: str):
    return db.query(User).filter(User.username == username).filter(User.password == password).first()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def insert_user(db: Session, user: User):
    db.add(user)
    db.commit()
    return user


def update_user(id: int, db: Session, user: User):
    db.commit()
    return user
