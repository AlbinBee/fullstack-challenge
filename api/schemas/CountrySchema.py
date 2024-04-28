from pydantic import BaseModel

class CountrySchema(BaseModel):
    country: str
    capital: str
    latitude: float
    longitude: float
    population: int