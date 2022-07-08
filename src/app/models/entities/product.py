from sqlalchemy import Column, Integer, String

from app.core.sql_app.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column('id', Integer, primary_key=True, index=True)
    sku = Column('sku', String, unique=True)
    name = Column('name', String)
    stock = Column('stock', Integer)
