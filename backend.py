"""
FastAPI Backend
Provides API endpoints for the Reflex frontend
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for Reflex frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def hello():
    """Simple API endpoint"""
    return {"message": "Hello from FastAPI!", "status": "success"}

@app.get("/api/greet/{name}")
async def greet(name: str):
    """API endpoint with path parameter"""
    return {"message": f"Hello, {name}!", "name": name, "status": "success"}

@app.get("/api/items")
async def get_items():
    """API endpoint returning a list of items"""
    return {
        "items": [
            {"id": 1, "name": "Item 1", "description": "First item"},
            {"id": 2, "name": "Item 2", "description": "Second item"},
            {"id": 3, "name": "Item 3", "description": "Third item"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
