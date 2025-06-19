from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db import Base

class LocationsM(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    address = Column(String(50), nullable=False)

    events = relationship("EventsM", back_populates="location")

    def __str__(self):
        return self.name