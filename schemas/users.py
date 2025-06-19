from pydantic import BaseModel

class UserS(BaseModel):
    name : str
    username : str
    email : str
    password : str