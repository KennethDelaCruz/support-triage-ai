import re
from ..schemas import TriageResponse, TriageMeta, Intent, Urgency

def _containts_any(text: str, keywords: list[str]) -> bool:
    """Check if any keyword is contained in the text."""
    return any(keyword in text for keyword in keywords)

def rule_based_triage(ticket_text: str) -> TriageResponse:
    t = ticket_text.lower()
    urgencies = {
        "P0": ["outage", "down", "sev", "p0", "production", "revenue", "all users", "asap", "urgent"],
        "P1": ["broken", "failed", "error", "blocked", "cannot", "can't", "cant"],
        "P2": ["intermittent", "slow", "degraded", "sometimes"]
    }

    intents = {
        "billing_refund": ["refund", "charge", "billing", "payment", "invoice", "chargeback", "chargeback refund", "chargeback charge"],
        "auth_sso_issue": ["login", "logout", "sso", "single sign-on", "auth", "authentication", "authorization", "permission", "role", "user", "account"],
        "performance_outage": ["outage", "down", "sev", "p0", "production", "revenue", "all users", "asap", "urgent"],
        "integration_issue": ["integration", "api", "connect", "sync", "connectivity", "connectivity issue", "connectivity error", "connectivity failure"],
        "feature_request": ["feature", "request", "enhancement", "improvement", "suggestion", "suggestion request", "suggestion enhancement", "suggestion improvement"],
        "bug_report": ["bug", "error", "issue", "problem", "defect", "defect report", "defect issue", "defect problem"],
    }

    # urgency heuristics
    if _containts_any(t, urgencies["P0"]):
        urgency = "P0"
    elif _containts_any(t, urgencies["P1"]):
        urgency = "P1"
    elif _containts_any(t, urgencies["P2"]):
        urgency = "P2"
    else:
        urgency = "P3"

    # intent heuristics
    if _containts_any(t, intents["billing_refund"]):
        intent = Intent.billing_refund
        next_step = "Request invoice/charge ID and confirm refund policy: rout to Billing queue."
    elif _containts_any(t, intents["auth_sso_issue"]):
        intent = Intent.auth_sso_issue
        next_step = "Collect IdP config (audience/client ID, redirect URI, timestamps) and escalate if production is impacted."
    elif _containts_any(t, intents["performance_outage"]):
        intent = Intent.performance_outage
        next_step = "Check status dashboards/logs and escalate to incident response; gather request IDs and timestamps."
    elif _containts_any(t, intents["integration_issue"]):
        intent = Intent.integration_issue
        next_step = "Request failing endpoint, request/response samples, and correlation/request IDs; route to Integrations."
    elif _containts_any(t, intents["feature_request"]):
        intent = Intent.feature_request
        next_step = "Confirm use case and business impact; tag as feature request and route to Product feedback."
    elif _containts_any(t, intents["bug_report"]):
        intent = Intent.bug_report
        next_step = "Request reproduction steps, environment, and logs; route to Engineering triage."
    elif re.search(r'\b(?:how|what|why|when|where|who|which|whose|whom)\s+to\s+', t):
        intent = Intent.how_to_question
        next_step = "Provide documentation or guide user through the process."
    else:
        intent = Intent.unknown
        next_step = "Review ticket and route appropriately."

    lines = [ln.strip() for ln in ticket_text.splitlines() if ln.strip()]
    summary = lines[0] if lines else "Ticket received. Auto-triaged applied via fallback rules."

    return TriageResponse(
        summary=summary[:2000],
        intent=intent,
        urgency=urgency,
        next_step=next_step,
        meta=TriageMeta(model="fallback_rules_v1", fallback_used=True, confidence=0.55),
    )