
"""Shared pytest fixtures for testing the Flask application."""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a Flask test client for HTTP request testing."""
    with app.test_client() as test_client:
        yield test_client
