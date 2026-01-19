from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import TriageMeta, TriageRequest, TriageResponse

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
    # Mock logic for foundation: deterministic output
    text = req.ticket_text.lower()

    if "refund" in text or "charge" in text:
        intent = "billing_refund"
        urgency = "P2"
        next_step = "Request invoice ID and confirm refund eligibility; route to Billing queue."
    elif "can't log in" in text or "cannot log in" in text or "sso" in text:
        intent = "auth_sso_issue"
        urgency = "P0"
        next_step = "Collect IdP config (audience/client ID, redirect URI) and escalate to on-call."
    elif "down" in text or "outage" in text or "500" in text:
        intent = "performance_outage"
        urgency = "P0"
        next_step = "Check status dashboards/logs and escalate to incident response."
    else:
        intent = "how_to_question"
        urgency = "P3"
        next_step = "Send relevant help doc and ask for clarification if needed."

    summary = (
        "Auto-triage (mock): extracted key issue from the ticket and prepared routing details."
    )

    return TriageResponse(
        summary=summary,
        intent=intent,
        urgency=urgency,
        next_step=next_step,
        meta=TriageMeta(model="mock_rules_v1", fallback_used=True, confidence=0.55),
    )
