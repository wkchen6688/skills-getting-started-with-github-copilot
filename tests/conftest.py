import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app


@pytest.fixture
def client():
    """Fixture that provides a test client"""
    return TestClient(app)


@pytest.fixture
def sample_activity():
    """Fixture that provides sample activity data"""
    return {
        "name": "Chess Club",
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12
    }


@pytest.fixture
def sample_email():
    """Fixture that provides a sample email"""
    return "test@mergington.edu"
