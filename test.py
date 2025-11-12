from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# HTML frontend
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI Frontend</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        #result {
            margin-top: 20px;
            padding: 15px;
            background-color: #f0f0f0;
            border-radius: 5px;
            min-height: 50px;
        }
        input {
            padding: 10px;
            width: 300px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>FastAPI Web Application</h1>
        <p>Welcome to your FastAPI backend with a simple frontend!</p>
        
        <h2>Test API Endpoints</h2>
        
        <div style="margin: 20px 0;">
            <button onclick="fetchHello()">Get Hello Message</button>
        </div>
        
        <div style="margin: 20px 0;">
            <input type="text" id="nameInput" placeholder="Enter your name">
            <button onclick="fetchGreeting()">Get Personalized Greeting</button>
        </div>
        
        <div id="result"></div>
    </div>

    <script>
        async function fetchHello() {
            const result = document.getElementById('result');
            result.textContent = 'Loading...';
            
            try {
                const response = await fetch('/api/hello');
                const data = await response.json();
                result.textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                result.textContent = 'Error: ' + error.message;
            }
        }

        async function fetchGreeting() {
            const name = document.getElementById('nameInput').value;
            const result = document.getElementById('result');
            
            if (!name) {
                result.textContent = 'Please enter a name';
                return;
            }
            
            result.textContent = 'Loading...';
            
            try {
                const response = await fetch(`/api/greet/${name}`);
                const data = await response.json();
                result.textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                result.textContent = 'Error: ' + error.message;
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the frontend HTML"""
    return html_content

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
    uvicorn.run(app, host="127.0.0.1", port=8000)
