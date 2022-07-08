from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.sql_app.database import Base


class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column('id', Integer, primary_key=True, index=True)
    order_id = Column('order_id', Integer, ForeignKey("orders.id"))
    status = Column('status', Integer)
    quantity = Column('quantity', Integer)
    product_id = Column('product_id', Integer, ForeignKey("products.id"))
    product = relationship("Product")
