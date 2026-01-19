"""
Vercel serverless function entry point for FastAPI
This file is required for Vercel to properly handle FastAPI routes
"""
import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.main import app

# Export the FastAPI app for Vercel
handler = app

