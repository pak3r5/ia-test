from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.sql_app.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column('id', Integer, primary_key=True, index=True)
    status = Column('status', Integer, unique=True)
    products = relationship("OrderDetail")

