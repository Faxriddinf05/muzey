from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

class ExhibitionsM(Base):
    __tablename__ = "exhibitions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    description = Column(String(50), nullable=False)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    type = Column(String(20), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    collection = relationship("CollectionsM", back_populates="exhibition")
    department = relationship("DepartmentsM", back_populates="exhibition")
    tickets = relationship("TicketsM", back_populates="exhibition")

    def __str__(self):
        return self.title