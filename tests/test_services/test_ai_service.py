"""Tests for the AI service module."""

import pytest
from br8niac.services.ai_service import AIService
from br8niac.constants import ModelStatus

def test_check_model_status(mock_config, requests_mock):
    """Test model status checking."""
    service = AIService(config=mock_config)
    
    # Test ready status
    requests_mock.get(
        f"{mock_config.OLLAMA_API_URL}/tags",
        status_code=200
    )
    assert service.check_model_status() == ModelStatus.READY
    
    # Test error status
    requests_mock.get(
        f"{mock_config.OLLAMA_API_URL}/tags",
        status_code=500
    )
    assert service.check_model_status() == ModelStatus.ERROR

def test_perform_search(mock_config, requests_mock, sample_search_results):
    """Test search functionality."""
    service = AIService(config=mock_config)
    query = "test query"
    
    # Mock successful search
    requests_mock.post(
        f"{mock_config.OLLAMA_API_URL}/generate",
        json={"response": '{"results": [{"title": "Test", "content": "Content", "url": "#"}]}'}
    )
    
    results = service.perform_search(query)
    assert "results" in results
    assert len(results["results"]) > 0
    
    # Test error handling
    requests_mock.post(
        f"{mock_config.OLLAMA_API_URL}/generate",
        status_code=500
    )
    
    results = service.perform_search(query)
    assert "error" in results