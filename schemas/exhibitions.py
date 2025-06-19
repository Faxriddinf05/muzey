from pydantic import BaseModel
from datetime import datetime
class ExhibitionS(BaseModel):

    title : str
    description : str
    start_at : datetime
    end_at : datetime
    type : str
    department_id : int
