
from contextlib import contextmanager
from sqlalchemy import create_engine, MetaData 
from sqlalchemy.orm import sessionmaker

from services.country_fetcher import fetch_countries_data

from models.Country import Country
from models.Location import Location

DATABASE_URL = "postgresql://postgres:123456@localhost/datacose_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_countries_table_if_not_exists():
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if 'countries' not in metadata.tables:
        print("Countries table does not exist. Creating it now...")
        Country.__table__.create(engine)
    if 'locations' not in metadata.tables:
        print("Locations table does not exist. Creating it now...")
        Location.__table__.create(engine)

def populate_countries_table():
    with get_db() as session:
        if not session.query(Country).count():
            countries_data = fetch_countries_data()
            for country in countries_data:
                country_db = Country(**country)
                session.add(country_db)
            session.commit()
            print("Countries data added to the database.")
        else:
            print("Countries table already contains data.")

def initialize_database():
    create_countries_table_if_not_exists()
    populate_countries_table()