"""Pytest configuration and fixtures."""

import pytest
from br8niac.config import Config

@pytest.fixture
def mock_config():
    """Provide a test configuration."""
    return Config(
        OLLAMA_API_URL="http://test-api:11434",
        AI_MODEL="test-model",
        DEBUG=True,
    )

@pytest.fixture
def sample_search_results():
    """Provide sample search results for testing."""
    return {
        "results": [
            {
                "title": "Test Result 1",
                "content": "Test content 1",
                "url": "http://example.com/1"
            },
            {
                "title": "Test Result 2",
                "content": "Test content 2",
                "url": "http://example.com/2"
            }
        ]
    }

@pytest.fixture
def mock_streamlit(mocker):
    """Mock streamlit functions for testing."""
    mock = mocker.patch("streamlit")
    return mock