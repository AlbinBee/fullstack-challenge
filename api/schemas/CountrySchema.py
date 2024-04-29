from pydantic import BaseModel

class CountrySchema(BaseModel):
    id: int
    country: str
    capital: str
    latitude: float
    longitude: float
    population: int