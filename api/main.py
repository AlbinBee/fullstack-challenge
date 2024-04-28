from fastapi import FastAPI, HTTPException, Depends, Query
import requests

from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String, Float, func  
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from models.Country import Country
from models.Location import Location
from schemas.CountrySchema import CountrySchema

from bs4 import BeautifulSoup
from typing import List
from pydantic import BaseModel

# SQLAlchemy setup
DATABASE_URL = "postgresql://postgres:123456@localhost/datacose_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()


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
            continue  # Skip invalid data

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

    # Use get_db to obtain a database session
    with get_db() as session:
        # Check if countries table is empty
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


# Call initialize_database function when the application starts
initialize_database()

# API endpoints

@app.get("/countries", response_model=List[dict])
async def get_countries_data():
    try:
        countries_data = fetch_countries_data()
        return countries_data
    except Exception as e:
        return {"error": str(e)}

@app.post("/locations")
async def create_location(name: str, latitude: str, longitude: str, db: Session = Depends(get_db)):
    db_location = Location(name=name, latitude=latitude, longitude=longitude)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@app.get("/locations/{location_id}")
async def get_location(location_id: int, db: Session = Depends(get_db)):
    with db as session:
        location = session.query(Location).filter(Location.id == location_id).first()
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
    return location

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