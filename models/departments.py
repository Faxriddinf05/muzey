from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db import Base

class DepartmentsM(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    description = Column(String(100), nullable=False)

    collection = relationship("CollectionsM", back_populates='department')
    exhibition = relationship("ExhibitionsM", back_populates="department")

    def __str__(self):
        return self.name
