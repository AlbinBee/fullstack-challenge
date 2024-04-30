from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String, Float, func  
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from models.Country import Country
from models.Location import Location
from models.CreateLocationModel import CreateLocationModel
from schemas.CountrySchema import CountrySchema
from schemas.LocationSchema import LocationData

from bs4 import BeautifulSoup
from typing import List
from pydantic import BaseModel

# SQLAlchemy setup
DATABASE_URL = "postgresql://postgres:123456@localhost/datacose_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    capital = Column(String)
    latitude = Column(String)
    longitude = Column(String)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

def fetch_countries_data():
    url = "https://gist.githubusercontent.com/ofou/df09a6834a8421b4f376c875194915c9/raw/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    data_lines = response.text.splitlines()
    if len(data_lines) <= 1:
        raise Exception("No data found in the response.")

    countries_data = []
    id_counter = 1
    for line in data_lines[1:]:
        parts = line.split(",")
        if len(parts) != 6:
            continue

        country_data = {
            "id": id_counter,
            "country": parts[0].strip(),
            "capital": parts[1].strip(),
            "latitude": float(parts[2].strip()),
            "longitude": float(parts[3].strip()),
            "population": int(parts[4].strip()),
            "capital_type": parts[5].strip()
        }
        countries_data.append(country_data)
        id_counter += 1

    # I had to add my country :)
    kosovo_data = {
        "id": id_counter,
        "country": "Kosovo",
        "capital": "Pristina",
        "latitude": 42.666667,
        "longitude": 21.166667,
        "population": 1795000,
        "capital_type": "Capital"
    }
    countries_data.append(kosovo_data)

    return countries_data

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to initialize database and populate countries table if empty
def initialize_database():
    Base.metadata.create_all(bind=engine)

    with get_db() as session:
        if not session.query(Country).count():
            countries_data = fetch_countries_data()
            if countries_data:
                for country in countries_data:
                    country_db = Country(**country)
                    session.add(country_db)
                session.commit()
                print("Countries data added to the database.")
            else:
                print("Failed to fetch countries data.")
        else:
            print("Countries table already contains data.")

initialize_database()

# API endpoints
@app.post("/locations")
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

# https://api.open-meteo.com/v1/forecast?latitude=42.666667,41.3275&longitude=21.166667,19.8189&current=temperature_2m&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin@app.get("/locations/{location_id}")
# @app.get("/locations", response_model=list[LocationSchema])
# async def get_locations(db: Session = Depends(get_db)):
#     with db as session:
#         locations = session.query(Location).all()
#         return locations

@app.get("/locations", response_model=List[LocationData])
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
            for location, weather_data in zip(locations, response_data):
                mapped_location = LocationData(
                    name=location.name,
                    capital=location.capital,
                    latitude=location.latitude,
                    longitude=location.longitude,
                    timezone=weather_data.get("timezone", ""),
                    current=weather_data.get("current", {}),
                    daily=weather_data.get("daily", {})
                )
                mapped_locations.append(mapped_location)
            
            return mapped_locations
        else:
            return []

async def get_location(location_id: int, db: Session = Depends(get_db)):
    with db as session:
        location = session.query(Location).filter(Location.id == location_id).first()
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
    return location

@app.delete("/locations/{name}")
async def delete_location_by_name(name: str, db: Session = Depends(get_db)):
    with db as session:
        location = session.query(Location).filter(Location.name == name).first()

        if location is None:
            raise HTTPException(status_code=404, detail="Location not found")

        session.delete(location)
        session.commit()

    return {"message": f"Location '{name}' deleted successfully"}

@app.get("/countries", response_model=List[dict])
async def get_countries_data():
    try:
        countries_data = fetch_countries_data()
        return countries_data
    except Exception as e:
        return {"error": str(e)}

@app.get("/countries-db", response_model=list[CountrySchema])
async def get_countries_from_db(db: Session = Depends(get_db)):
    with db as session:
        countries = session.query(Country).all()
        return countries

@app.get("/country/{country_name}")
async def get_country_by_name(country_name: str, db: Session = Depends(get_db)):
    country_name = country_name.lower()
    with db as session:
        country = session.query(Country).filter(func.lower(Country.country) == country_name).first()
        if not country:
            raise HTTPException(status_code=404, detail="Country not found")
    return country