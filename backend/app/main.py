from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import TriageMeta, TriageRequest, TriageResponse
from .services.triage_service import triage_ticket



app = FastAPI(title="Support Triage API", version="0.1.0")

# CORS configuration - update with your Vercel frontend URL when deployed
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",  # Vite default port
        # Add your Vercel frontend URL here after deployment
        # "https://your-frontend.vercel.app"
    ],
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
