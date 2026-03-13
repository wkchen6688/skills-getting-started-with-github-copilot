# FastAPI Tests

This directory contains comprehensive tests for the Mergington High School Activities API.

## Test Structure

- `conftest.py` - Pytest fixtures and configuration
- `test_endpoints.py` - Tests for basic endpoints (GET /activities, root redirect)
- `test_signup.py` - Tests for signup functionality (POST /activities/{name}/signup)
- `test_remove_participant.py` - Tests for participant removal (DELETE /activities/{name}/participants/{email})
- `test_error_handling.py` - Additional error handling and edge case tests

## Running Tests

Run all tests:
```bash
pytest
```

Run with verbose output:
```bash
pytest -v
```

Run specific test file:
```bash
pytest tests/test_signup.py
```

Run with coverage:
```bash
pytest --cov=src
```

## Test Coverage

The tests cover:
- ✅ All API endpoints (GET, POST, DELETE)
- ✅ Success scenarios and error cases
- ✅ Data validation and structure verification
- ✅ State changes (participants being added/removed)
- ✅ Edge cases and error handling
- ✅ HTTP status codes and response formats

## Fixtures

- `client` - FastAPI TestClient instance
- `sample_activity` - Sample activity data for testing
- `sample_email` - Sample email for testing signups

