from pydantic import BaseModel

class LocationSchema(BaseModel):
    name: str
    latitude: float
    longitude: float