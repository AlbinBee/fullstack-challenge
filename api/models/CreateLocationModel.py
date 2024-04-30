from pydantic import BaseModel

class CreateLocationModel(BaseModel):
    name: str
    capital: str
    latitude: float
    longitude: float