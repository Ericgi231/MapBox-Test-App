"""
Simple FastAPI Backend
Run with: uvicorn app:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Allow frontend to call API (React dev server + production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Create React App
        "http://localhost:5173",  # Vite
        "http://localhost:8000",  # When serving HTML from FastAPI
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/geocode/{zipcode}")
def geocode(zipcode: str):
    MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
    if not MAPBOX_TOKEN:
        return {"error": "MAPBOX_TOKEN not configured"}
    
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{zipcode}.json"
    params = {
        "access_token": MAPBOX_TOKEN,
        "types": "postcode",
        "country": "US"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['features']:
        coords = data['features'][0]['center']  # [lng, lat]
        return {
            "longitude": coords[0],
            "latitude": coords[1],
            "place_name": data['features'][0]['place_name']
        }
    return {"error": "Zip code not found"}

@app.get("/api/hello")
def hello():
    """Simple API endpoint"""
    return {"message": "Hello from FastAPI!", "status": "success"}

@app.get("/api/greet/{name}")
def greet(name: str):
    """API endpoint with parameter"""
    return {"message": f"Hello, {name}!", "name": name}
