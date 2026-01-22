import os
from ..schemas import TriageRequest, TriageResponse, TriageMeta, Intent
from .fallback_rules import rule_based_triage
from .hf_client import hf_generate_triage

HF_MODEL = os.getenv("HF_MODEL", "meta-llama/Meta-Llama-3-8B-Instruct")

def triage_ticket(request: TriageRequest) -> TriageResponse:
    ticket_text = (request.ticket_text or "").strip()

    if not ticket_text:
        return TriageResponse(
            summary="Empty ticket received.",
            intent=Intent.unknown.value,
            urgency="P3",
            next_step="Request ticket details from user.",
            meta=TriageMeta(model="empty_handler", fallback_used=True, confidence=1.0),
        )

    # Try AI inference first
    try:
        ai_result = hf_generate_triage(ticket_text)
        print(f"AI result: {ai_result}")
    except Exception:
        ai_result = None
        print("Error generating AI result")

    if isinstance(ai_result, dict) and ai_result:
        # Pull fields with safe defaults
        summary = (ai_result.get("summary") or ticket_text[:200])[:2000]
        intent = ai_result.get("intent") or Intent.unknown.value
        urgency = ai_result.get("urgency") or "P3"
        next_step = (ai_result.get("next_step") or "Review ticket and route appropriately.")[:1000]

        # Normalize intent to enum
        try:
            intent = Intent(intent).value
        except Exception:
            intent = Intent.unknown.value

        # Normalize urgency
        if urgency not in ["P0", "P1", "P2", "P3"]:
            urgency = "P3"

        return TriageResponse(
            summary=summary,
            intent=intent,
            urgency=urgency,
            next_step=next_step,
            meta=TriageMeta(model=HF_MODEL, fallback_used=False, confidence=0.78),
        )

    # Fallback to rule-based triage (guaranteed valid)
    return rule_based_triage(ticket_text)
