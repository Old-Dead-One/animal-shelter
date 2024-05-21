from pydantic import BaseModel
from typing import Dict

class Shelter(BaseModel):
    shelter_id: int
    name: str
    address: str
    animals: Dict[str, int]
    