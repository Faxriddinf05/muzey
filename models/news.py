from sqlalchemy import Column, String, Integer, Date
from db import Base

class NewsM(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(255), nullable=False)
    publication_date = Column(Date, nullable=False)
    image = Column(String(255), nullable=False)
    video = Column(String(255), nullable=False)