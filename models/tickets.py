from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db import Base

class TicketsM(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    exhibition_id = Column(Integer, ForeignKey('exhibitions.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    visit_date = Column(DateTime, nullable=False)

    event = relationship("EventsM", back_populates="tickets")
    exhibition = relationship("ExhibitionsM", back_populates="tickets")
    user = relationship("UsersM", back_populates="tickets")

    def __str__(self):
        return self.status