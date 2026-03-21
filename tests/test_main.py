"""
Tests for main application endpoints.
"""

import pytest
from fastapi.testclient import TestClient

from generaltemplate.main import app

client = TestClient(app)


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_root_returns_200(self):
        """Test that root endpoint returns 200 status code."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_html(self):
        """Test that root endpoint returns HTML content."""
        response = client.get("/")
        assert "text/html" in response.headers["content-type"]

    def test_root_contains_title(self):
        """Test that root endpoint contains the application title."""
        response = client.get("/")
        assert "FastAPI Template" in response.text


class TestHealthEndpoint:
    """Tests for health check endpoints."""

    def test_health_check_returns_200(self):
        """Test that health check endpoint returns 200 status code."""
        response = client.get("/api/health")
        assert response.status_code == 200

    def test_health_check_returns_json(self):
        """Test that health check endpoint returns JSON."""
        response = client.get("/api/health")
        assert response.headers["content-type"] == "application/json"

    def test_health_check_response_structure(self):
        """Test that health check response has correct structure."""
        response = client.get("/api/health")
        data = response.json()

        assert "status" in data
        assert "environment" in data
        assert "timestamp" in data
        assert "app_name" in data

        assert data["status"] == "healthy"
        assert data["app_name"] == "generaltemplate"

    def test_readiness_check_returns_200(self):
        """Test that readiness check endpoint returns 200 status code."""
        response = client.get("/api/ready")
        assert response.status_code == 200

    def test_readiness_check_response_structure(self):
        """Test that readiness check response has correct structure."""
        response = client.get("/api/ready")
        data = response.json()

        assert "ready" in data
        assert "checks" in data
        assert data["ready"] is True


class TestAPIDocumentation:
    """Tests for API documentation endpoints."""

    def test_openapi_schema_accessible(self):
        """Test that OpenAPI schema is accessible."""
        response = client.get("/openapi.json")
        assert response.status_code == 200

    def test_swagger_ui_accessible(self):
        """Test that Swagger UI is accessible."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_redoc_accessible(self):
        """Test that ReDoc is accessible."""
        response = client.get("/redoc")
        assert response.status_code == 200
