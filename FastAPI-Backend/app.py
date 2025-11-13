"""
Simple FastAPI Backend
Run with: uvicorn app:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

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

@app.get("/api/hello")
def hello():
    """Simple API endpoint"""
    return {"message": "Hello from FastAPI!", "status": "success"}

@app.get("/api/greet/{name}")
def greet(name: str):
    """API endpoint with parameter"""
    return {"message": f"Hello, {name}!", "name": name}
