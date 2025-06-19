from pydantic import BaseModel

class LocationS(BaseModel):
    name : str
    address : str