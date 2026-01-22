import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import TriageRequest, TriageResponse
from .services.triage_service import triage_ticket

app = FastAPI(title="Support Triage API", version="0.1.0")

# CORS configuration
# Allow Vercel preview and production deployments
vercel_origins = os.getenv("VERCEL_ORIGINS", "").split(",") if os.getenv("VERCEL_ORIGINS") else []
cors_origins = [
    "http://localhost:3000",
    "http://localhost:5173",  # Vite default port
    *[origin.strip() for origin in vercel_origins if origin.strip()],
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_origin_regex=r"https://.*\.vercel\.app",  # Allow all Vercel deployments
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/triage", response_model=TriageResponse)
def triage(req: TriageRequest) -> TriageResponse:
    return triage_ticket(req)
