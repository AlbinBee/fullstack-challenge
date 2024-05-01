from typing import List
from pydantic import BaseModel

class CurrentData(BaseModel):
    time: str
    weather_code: int
    interval: int
    temperature_2m: float
    rain: float

class DailyData(BaseModel):
    time: List[str]
    weather_code: List[int]
    temperature_2m_max: List[float]
    temperature_2m_min: List[float]
    rain_sum: List[float]

class LocationSchema(BaseModel):
    name: str
    capital: str
    latitude: float
    longitude: float
    timezone: str
    current: CurrentData
    daily: DailyData