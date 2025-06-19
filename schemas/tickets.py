from pydantic import BaseModel
from datetime import datetime


class TicketS(BaseModel):
    event_id : int
    exhibition_id : int
    user_id : int
    status : str
    price : int
    visit_date : datetime