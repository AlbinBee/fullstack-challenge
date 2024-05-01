from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
import requests
from typing import List

from sqlalchemy.orm import Session

from models.Location import Location
from schemas.LocationSchema import LocationSchema
from models.CreateLocationModel import CreateLocationModel
from database import get_db

location_router = APIRouter()

# API endpoints
@location_router.post("/")
async def create_location(location_data: CreateLocationModel, db: Session = Depends(get_db)):
    with db as session:
        existing_location = session.query(Location).filter(Location.name == location_data.name).first()
        if existing_location:
            raise HTTPException(status_code=400, detail="Location with this name already exists")

        db_location = Location(name=location_data.name, capital=location_data.capital, latitude=location_data.latitude, longitude=location_data.longitude)
        session.add(db_location)  
        session.commit() 
        session.refresh(db_location)  
    return db_location

# https://api.open-meteo.com/v1/forecast?latitude=42.666667,41.3275&longitude=21.166667,19.8189&current=temperature_2m&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin
@location_router.get("/", response_model=List[LocationSchema])
async def get_locations(db: Session = Depends(get_db)):
    with db as session:
        locations = session.query(Location).all()

        if not locations:
            return []

        latitudes = [location.latitude for location in locations]
        longitudes = [location.longitude for location in locations]

        latitudes_str = ','.join(map(str, latitudes))
        longitudes_str = ','.join(map(str, longitudes))
        open_meteo_base_url = "https://api.open-meteo.com/v1/forecast"
        timezone = "Europe%2FBerlin"
        open_meteo_parameters = f"{open_meteo_base_url}?latitude={latitudes_str}&longitude={longitudes_str}&current=weather_code,temperature_2m,rain&daily=weather_code,temperature_2m_max,temperature_2m_min,rain_sum&timezone={timezone}"
        
        response = requests.get(open_meteo_parameters)

        if response.status_code == 200:
            response_data = response.json()

            mapped_locations = []
            if isinstance(response_data, list):  # Check if response_data is a list
                for location, weather_data in zip(locations, response_data):
                    mapped_location = create_mapped_location(location, weather_data)
                    mapped_locations.append(mapped_location)
            else:  # If response_data is not a list (only one item)
                mapped_location = create_mapped_location(locations[0], response_data)
                mapped_locations.append(mapped_location)
            
            return mapped_locations
        else:
            return []
        
def create_mapped_location(location, weather_data):
    current_weather = weather_data.get('current', {})
    daily_weather = weather_data.get('daily', {})
    
    return LocationSchema(
        name=location.name,
        capital=location.capital,
        latitude=location.latitude,
        longitude=location.longitude,
        timezone=weather_data.get('timezone', ""),
        current=current_weather,
        daily=daily_weather
    )

@location_router.get("/{location_id}", response_model=LocationSchema)
async def get_location(location_id: int, db: Session = Depends(get_db)):
    with db as session:
        location = session.query(Location).filter(Location.id == location_id).first()
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")

        location_dict = location.__dict__
        location_dict.pop("_sa_instance_state", None)

        return JSONResponse(content=location_dict)


@location_router.delete("/{name}")
async def delete_location_by_name(name: str, db: Session = Depends(get_db)):
    with db as session:
        location = session.query(Location).filter(Location.name == name).first()

        if location is None:
            raise HTTPException(status_code=404, detail="Location not found")

        session.delete(location)
        session.commit()

    return {"message": f"Location '{name}' deleted successfully"}
