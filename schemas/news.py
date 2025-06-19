from pydantic import BaseModel
from datetime import date

class NewS(BaseModel):
    title : str
    content : str
    publication_date : date
    image : str
    video : str
