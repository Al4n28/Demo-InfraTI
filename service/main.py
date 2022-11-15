import uvicorn
from fastapi import FastAPI
import api_data
from models.Character_Model import Character_Model as model

app= FastAPI()

@app.get("/")
def index():
    return{
        "message":"Hola Titi"
    }

@app.get("/photo/{id}", response_model=model)
async def personajeGetter(id:int):
    personaje = await api_data.get_personajeByID(id)
    return personaje.dict()

if __name__ == "__main__":
    uvicorn.run(app)