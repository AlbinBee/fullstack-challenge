from pydantic import BaseModel

class CreateLocationModel(BaseModel):
    name: str
    latitude: float
    longitude: float