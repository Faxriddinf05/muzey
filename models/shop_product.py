from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base

class ProductM(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    image_url = Column(String(255), nullable=False)