from pydantic import BaseModel
class Character_Model(BaseModel):
    id:str
    title:str
    url:str
