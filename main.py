"""
Main application file
Runs both FastAPI backend and Reflex frontend
"""
import subprocess
import sys
import time
from pathlib import Path

def run_backend():
    """Run the FastAPI backend server"""
    print("🚀 Starting FastAPI backend on http://127.0.0.1:8000")
    backend_path = Path(__file__).parent / "backend.py"
    subprocess.Popen([sys.executable, str(backend_path)])

def run_frontend():
    """Run the Reflex frontend"""
    print("🎨 Starting Reflex frontend...")
    print("⏳ Please wait for Reflex to compile (first run may take a moment)...")
    frontend_path = Path(__file__).parent / "frontend.py"
    subprocess.run([sys.executable, str(frontend_path)])

if __name__ == "__main__":
    print("=" * 60)
    print("FastAPI + Reflex Application")
    print("=" * 60)
    
    # Start backend
    run_backend()
    
    # Give backend time to start
    time.sleep(2)
    
    # Start frontend (this will block and show the UI)
    run_frontend()
