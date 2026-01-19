"""Tests for the main FastAPI application."""

import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

from app.main import app


@pytest.fixture
async def client():
    """Create a test client."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": True}
