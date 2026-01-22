"""
Vercel serverless function entry point for FastAPI
This file is required for Vercel to properly handle FastAPI routes
"""
import sys
import os

# Add the backend directory to the Python path
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Import the FastAPI app
from app.main import app

# Export the FastAPI app for Vercel
# Vercel's Python runtime expects 'handler' or 'app' for ASGI applications
handler = app
app = app  # Also export as 'app' for compatibility

