from pydantic import BaseModel


class DepartmentS(BaseModel):
    name : str
    description : str
