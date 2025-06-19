from pydantic import BaseModel

class ProductS(BaseModel):
    title : str
    description : str
    price : int
    image_url : str
