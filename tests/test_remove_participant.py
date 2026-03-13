def test_remove_participant(client):
    """Test removing a participant from an activity"""
    email_to_remove = "michael@mergington.edu"
    
    initial_response = client.get("/activities")
    initial_participants = initial_response.json()["Chess Club"]["participants"].copy()
    
    response = client.delete(
        "/activities/Chess Club/participants/michael@mergington.edu"
    )
    
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]
    
    # Verify participant was removed
    verify_response = client.get("/activities")
    updated_participants = verify_response.json()["Chess Club"]["participants"]
    assert len(updated_participants) == len(initial_participants) - 1
    assert email_to_remove not in updated_participants


def test_remove_nonexistent_participant(client):
    """Test removing a participant not in the activity"""
    response = client.delete(
        "/activities/Chess Club/participants/nonexistent@mergington.edu"
    )
    
    assert response.status_code == 404
    assert "not signed up" in response.json()["detail"]


def test_remove_from_nonexistent_activity(client):
    """Test removing a participant from non-existent activity"""
    response = client.delete(
        "/activities/Nonexistent Club/participants/test@mergington.edu"
    )
    
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
