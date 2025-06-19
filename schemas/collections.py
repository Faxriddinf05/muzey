from pydantic import BaseModel


class CollectionS(BaseModel):
    title : str
    description : str
    artist : str
    year : str
    department_id : int
    image : str
    inventory_num : int
    exhibition_id : int





