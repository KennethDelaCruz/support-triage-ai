from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class TriageRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    ticket_text: str = Field(..., description="The raw ticket content to analyze")

class TriageMeta(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    model: str = Field(..., description="Model or method used for triage")
    fallback_used: bool = Field(..., description="Whether fallback logic was used")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score (0-1)")

class TriageResponse(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


    summary: str = Field(..., description="Brief summary of the ticket")
    intent: str = Field(..., description="Categorized intent of the ticket")
    urgency: str = Field(..., description="Urgency level (P0, P1, P2, P3)")
    next_step: str = Field(..., description="Recommended next action")
    meta: TriageMeta = Field(..., description="Metadata about the triage process")

