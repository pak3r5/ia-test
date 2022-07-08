from sqlalchemy import Column, Integer, String

from app.core.sql_app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, index=True)
    username = Column('username', String, unique=True)
    name = Column('name', String)
    last_name = Column('last_name', String)
    password = Column('password', String)
