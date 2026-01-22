from enum import Enum

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Intent(str, Enum):
    billing_refund = "billing_refund"
    bug_report = "bug_report"
    feature_request = "feature_request"
    auth_sso_issue = "auth_sso_issue"
    performance_outage = "performance_outage"
    account_access = "account_access"
    how_to_question = "how_to_question"
    internal_issue = "internal_issue"
    unknown = "unknown"

class Urgency(str, Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"

class TicketSource(str, Enum):
    email = "email"
    chat = "chat"
    web = "web"



class BaseCamelModel(BaseModel):
    """Base model for all camel-case models."""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class TriageRequest(BaseCamelModel):
    ticket_text: str = Field(..., description="The raw ticket content to analyze")
    source: TicketSource = TicketSource.web
    ticket_id: str | None = Field(default=None, max_length=100, description="The ID of the ticket")

class TriageMeta(BaseCamelModel):
    model: str = Field(..., description="Model or method used for triage")
    fallback_used: bool = Field(..., description="Whether fallback logic was used")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score (0-1)")

class TriageResponse(BaseCamelModel):
    summary: str = Field(..., description="Brief summary of the ticket")
    intent: str = Field(..., description="Categorized intent of the ticket")
    urgency: str = Field(..., description="Urgency level (P0, P1, P2, P3)")
    next_step: str = Field(..., description="Recommended next action")
    meta: TriageMeta = Field(..., description="Metadata about the triage process")

