from schemas import TriageRequest, TriageResponse
from services.fallback_rules import rule_based_triage

def triage_ticket(request: TriageRequest) -> TriageResponse:
    # Foundation: deterministic fallback only. 
    #Next: try AI inference first, validate, then fallback
    return rule_based_triage(request.ticket_text)