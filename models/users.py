from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db import Base

class UsersM(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    token = Column(String(255), nullable=True)

    tickets = relationship("TicketsM", back_populates= "user")

    def __str__(self):
        return self.name