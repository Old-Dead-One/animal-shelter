# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from fastapi import FastAPI, HTTPException
from backend.models import Shelter

app = FastAPI()

shelters = [
    Shelter(
        shelter_id = 1,
        name = "St. George Animal Shelter",
        address = "605 Waterworks Dr, St. George, UT 84770",
        animals = {"cats": 13, "dogs": 15,}
    ),
    Shelter(
        shelter_id = 2,
        name = "St. George Paws",
        address = "1125 W 1130 N, St. George, UT 84770",
        animals = {"cats": 12, "dogs": 9,}
    ),
    Shelter(
        shelter_id = 3,
        name = "Animal Rescue Team",
        address = "1838 W 1020 N Ste. B, St. George, UT 84770",
        animals = {"cats": 4, "dogs": 7,}
    )
]

@app.get("/shelters")
async def list_shelters() -> list[Shelter]:
    return shelters

@app.post("/shelters")
async def create_shelter(shelter_request: Shelter) -> Shelter:
    shelters.append(shelter_request)
    return shelter_request

@app.put("/shelter/{shelter_id}")
async def update_shelter(shelter_id: int, update_request: Shelter) -> Shelter:
    for shelter in shelters:
        if shelter.shelter_id == shelter_id:
            shelter.name = update_request.name
            shelter.address = update_request.address
            shelter.animals = update_request.animals
            return shelter
    raise HTTPException(status_code=404, detail="Shelter not found")

@app.delete("/shelter/{shelter_id}")
async def delete_shelter(shelter_id: int):
    for shelter in shelters:
        if shelter.shelter_id == shelter_id:
            shelters.remove(shelter)
            return
    raise HTTPException(status_code=404, detail="Shelter not found")
