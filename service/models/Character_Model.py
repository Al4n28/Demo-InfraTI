from pydantic import BaseModel
class Character_Model(BaseModel):
    name:str
    status:str
    species:str
    gender:str