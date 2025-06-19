from pydantic import BaseModel
from datetime import date


class EventS(BaseModel):
    title : str
    description : str
    date : date
    location_id : int
    price : int
