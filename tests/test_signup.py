def test_signup_for_activity(client, sample_email):
    """Test successful signup for an activity"""
    initial_response = client.get("/activities")
    initial_participants = initial_response.json()["Chess Club"]["participants"].copy()
    
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": sample_email}
    )
    
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    assert sample_email in response.json()["message"]
    
    # Verify participant was added
    verify_response = client.get("/activities")
    updated_participants = verify_response.json()["Chess Club"]["participants"]
    assert len(updated_participants) == len(initial_participants) + 1
    assert sample_email in updated_participants


def test_signup_duplicate_email(client, sample_email):
    """Test that duplicate signups are rejected"""
    # First signup
    client.post(
        "/activities/Chess Club/signup",
        params={"email": sample_email}
    )
    
    # Try duplicate signup
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": sample_email}
    )
    
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_nonexistent_activity(client, sample_email):
    """Test signup for non-existent activity"""
    response = client.post(
        "/activities/Nonexistent Club/signup",
        params={"email": sample_email}
    )
    
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
