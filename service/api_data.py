from typing import Optional
from urllib import response
from typing import Optional
import httpx
from models.Character_Model import Character_Model as model

async def get_personajeByID(characterID:int) -> Optional[model]:
    url= f"https://jsonplaceholder.typicode.com/photos/{characterID}"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        character =model(**data)
        return character
