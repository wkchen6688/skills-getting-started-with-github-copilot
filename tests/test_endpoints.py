def test_root_redirect(client):
    """Test that root endpoint redirects to static index"""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert "/static/index.html" in response.headers.get("location", "")


def test_get_activities(client):
    """Test getting all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_get_activities_structure(client):
    """Test that activities have correct structure"""
    response = client.get("/activities")
    data = response.json()
    
    for activity_name, activity in data.items():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
