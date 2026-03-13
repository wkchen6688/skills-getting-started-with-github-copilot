import pytest


def test_invalid_activity_name_type(client):
    """Test handling of invalid activity name formats"""
    response = client.post(
        "/activities//signup",
        params={"email": "test@mergington.edu"}
    )
    # Should return 405 Method Not Allowed or 404
    assert response.status_code in [404, 405]


def test_missing_email_parameter(client):
    """Test signup without email parameter"""
    response = client.post("/activities/Chess Club/signup")
    assert response.status_code == 422  # Unprocessable Entity


def test_empty_email_parameter(client):
    """Test signup with empty email"""
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": ""}
    )
    # Should succeed since validation is minimal, but parameter exists
    assert response.status_code == 200


def test_activities_endpoint_cors(client):
    """Test that activities endpoint responds to GET"""
    response = client.get("/activities")
    assert response.status_code == 200
    assert response.headers.get("content-type") is not None
