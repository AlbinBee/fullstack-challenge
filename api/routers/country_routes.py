from fastapi import APIRouter, HTTPException, Depends
from typing import List

from models.Country import Country
from schemas.CountrySchema import CountrySchema
from database import get_db, fetch_countries_data

from sqlalchemy.orm import Session
from sqlalchemy import  func  

country_router = APIRouter()

@country_router.get("/", response_model=List[dict])
async def get_countries_data():
    try:
        countries_data = fetch_countries_data()
        return countries_data
    except Exception as e:
        return {"error": str(e)}

@country_router.get("/from-db", response_model=list[CountrySchema])
async def get_countries_from_db(db: Session = Depends(get_db)):
    with db as session:
        countries = session.query(Country).all()
        return countries

@country_router.get("/{country_name}")
async def get_country_by_name(country_name: str, db: Session = Depends(get_db)):
    country_name = country_name.lower()
    with db as session:
        country = session.query(Country).filter(func.lower(Country.country) == country_name).first()
        if not country:
            raise HTTPException(status_code=404, detail="Country not found")
    return country