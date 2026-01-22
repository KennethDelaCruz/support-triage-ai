"""
Vercel serverless function entry point for FastAPI
This file is required for Vercel to properly handle FastAPI routes
"""
import sys
import os
from pathlib import Path

# Try multiple path resolution strategies for different deployment environments
def find_backend_path():
    """Find the backend directory using multiple strategies."""
    current_file = Path(__file__).resolve()
    
    # Strategy 1: Relative to current file (api/index.py -> ../backend)
    strategy1 = current_file.parent.parent / "backend"
    if strategy1.exists() and (strategy1 / "app").exists():
        return str(strategy1)
    
    # Strategy 2: Current working directory + backend
    cwd_backend = Path.cwd() / "backend"
    if cwd_backend.exists() and (cwd_backend / "app").exists():
        return str(cwd_backend)
    
    # Strategy 3: Look for backend in parent directories
    for parent in current_file.parents:
        backend_candidate = parent / "backend"
        if backend_candidate.exists() and (backend_candidate / "app").exists():
            return str(backend_candidate)
    
    # Strategy 4: Try absolute path from project root
    # In Vercel, the working directory might be different
    if os.getenv("VERCEL"):
        # In Vercel, try common locations
        for possible_root in ["/var/task", "/tmp", os.getcwd()]:
            vercel_backend = Path(possible_root) / "backend"
            if vercel_backend.exists() and (vercel_backend / "app").exists():
                return str(vercel_backend)
    
    # Fallback: use relative path
    return str(current_file.parent.parent / "backend")

# Add backend to Python path
backend_path_str = find_backend_path()
if backend_path_str not in sys.path:
    sys.path.insert(0, backend_path_str)

# Import the FastAPI app with detailed error reporting
try:
    from app.main import app
except ImportError as e:
    # Better error message for debugging in Vercel logs
    import traceback
    error_details = {
        "error": str(e),
        "python_path": sys.path[:5],  # First 5 entries
        "backend_path": backend_path_str,
        "backend_exists": os.path.exists(backend_path_str),
        "cwd": os.getcwd(),
        "file_location": __file__,
    }
    print("=" * 50)
    print("IMPORT ERROR DETAILS:")
    for key, value in error_details.items():
        print(f"  {key}: {value}")
    print("=" * 50)
    traceback.print_exc()
    raise

# Export the FastAPI app for Vercel
# Vercel's Python runtime expects 'handler' or 'app' for ASGI applications
handler = app

