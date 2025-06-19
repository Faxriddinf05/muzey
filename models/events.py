from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

class EventsM(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    description = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    price = Column(Integer, nullable=False)

    location = relationship("LocationsM", back_populates="events")
    tickets = relationship("TicketsM", back_populates="event")

    def __str__(self):
        return self.title