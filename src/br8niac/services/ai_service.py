import requests
import json
from typing import Dict, List, Union
from enum import Enum
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ModelStatus(str, Enum):
    READY = "ready"
    ERROR = "error"
    NOT_AVAILABLE = "not_available"

class AIService:
    def __init__(self, config: dict):
        """
        Initialize AI service with configuration.
        
        Args:
            config: Configuration dictionary
        """
        self.api_url = config.get('OLLAMA_API_URL', 'http://localhost:11434/api')
        self.model = config.get('AI_MODEL', 'mistral')
        self.timeout = config.get('API_TIMEOUT', 30)
    
    def check_model_status(self) -> ModelStatus:
        """Check if the local AI model is available and ready."""
        try:
            response = requests.get(
                f"{self.api_url}/tags",
                timeout=self.timeout
            )
            return ModelStatus.READY if response.status_code == 200 else ModelStatus.ERROR
        except Exception as e:
            logger.error(f"Model status check failed: {str(e)}")
            return ModelStatus.NOT_AVAILABLE
    
    def perform_search(self, query: str) -> Dict[str, Union[List[Dict], str]]:
        """
        Perform a search using the local AI model.
        
        Args:
            query: The search query
            
        Returns:
            Dictionary containing either results or error message
        """
        try:
            # Log search attempt
            logger.info(f"Performing search: {query}")
            
            response = requests.post(
                f"{self.api_url}/generate",
                json={
                    "model": self.model,
                    "prompt": self._create_search_prompt(query)
                },
                timeout=self.timeout
            )
            
            if response.status_code != 200:
                raise Exception(f"API returned status {response.status_code}")
            
            result = response.json()
            
            try:
                # Try to parse the response as JSON
                parsed_results = json.loads(result["response"])
                # Add timestamp to results
                for r in parsed_results:
                    r['timestamp'] = datetime.now().isoformat()
                return {"results": parsed_results}
            except json.JSONDecodeError:
                # If not JSON, return as plain text result
                return {
                    "results": [{
                        "title": "Search Result",
                        "content": result["response"],
                        "url": "#",
                        "timestamp": datetime.now().isoformat()
                    }]
                }
            
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            return {"error": str(e)}
    
    def _create_search_prompt(self, query: str) -> str:
        """
        Create a formatted prompt for the AI model.
        
        Args:
            query: The search query
            
        Returns:
            Formatted prompt string
        """
        return f"""Search query: {query}
        Please provide search results in the following JSON format:
        [
            {{
                "title": "Result title",
                "content": "Detailed content with key information",
                "url": "URL of the result",
                "type": "Type of content (article, news, research, etc.)",
                "relevance_score": "Score between 0-1"
            }}
        ]
        
        Important guidelines:
        - Provide detailed content for each result
        - Ensure URLs are properly formatted
        - Include type and relevance score
        - Limit to 5 most relevant results
        - Focus on accuracy and relevance
        """