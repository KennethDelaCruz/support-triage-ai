"""Tests for Pydantic schemas."""

import pytest
from pydantic import ValidationError

from app.schemas import TriageMeta, TriageRequest, TriageResponse


def test_triage_request_valid():
    """Test valid TriageRequest."""
    request = TriageRequest(ticket_text="Test ticket")
    assert request.ticket_text == "Test ticket"


def test_triage_request_missing_field():
    """Test TriageRequest with missing required field."""
    with pytest.raises(ValidationError):
        TriageRequest()


def test_triage_meta_valid():
    """Test valid TriageMeta."""
    meta = TriageMeta(
        model="test_model",
        fallback_used=False,
        confidence=0.85,
    )
    assert meta.model == "test_model"
    assert meta.fallback_used is False
    assert meta.confidence == 0.85


def test_triage_meta_invalid_confidence():
    """Test TriageMeta with invalid confidence value."""
    with pytest.raises(ValidationError):
        TriageMeta(
            model="test",
            fallback_used=False,
            confidence=1.5,  # Should be between 0 and 1
        )


def test_triage_response_valid():
    """Test valid TriageResponse."""
    response = TriageResponse(
        summary="Test summary",
        intent="test_intent",
        urgency="P1",
        next_step="Test next step",
        meta=TriageMeta(
            model="test_model",
            fallback_used=False,
            confidence=0.9,
        ),
    )
    assert response.summary == "Test summary"
    assert response.intent == "test_intent"
    assert response.urgency == "P1"
