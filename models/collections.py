from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base

class CollectionsM(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    description = Column(String(100), nullable=False)
    artist = Column(String(50), nullable=False)
    year = Column(Date, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    image = Column(String(255), nullable=False)
    inventory_num = Column(String(15), nullable=False)
    exhibition_id = Column(Integer,ForeignKey("exhibitions.id"), nullable=False)

    department = relationship("DepartmentsM", back_populates='collection')
    exhibition = relationship("ExhibitionsM", back_populates='collection')

    def __str__(self):
        return self.title