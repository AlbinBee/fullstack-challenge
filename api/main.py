from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.location_routes import location_router
from routers.country_routes import country_router
from database import initialize_database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

initialize_database()

# Routers
app.include_router(location_router, prefix="/locations", tags=["Locations"])
app.include_router(country_router, prefix="/countries", tags=["Countries"])