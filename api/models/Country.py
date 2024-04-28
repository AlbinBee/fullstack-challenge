from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    capital = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    population = Column(Integer)
    capital_type = Column(String)