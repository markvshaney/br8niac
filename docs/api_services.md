# Services API Documentation

## AI Service

The `AIService` class handles all interactions with the local AI model.

### Methods

#### check_model_status()
Checks if the local AI model is available and ready.

```python
def check_model_status() -> str:
    """
    Returns:
        str: Model status ('ready', 'error', or 'not_available')
    """
```

#### perform_search(query: str)
Performs a search using the local AI model.

```python
def perform_search(query: str) -> Dict[str, Union[List[Dict], str]]:
    """
    Args:
        query (str): The search query

    Returns:
        Dict[str, Union[List[Dict], str]]: Search results or error message
        
    Example:
        {
            "results": [
                {
                    "title": "Result title",
                    "content": "Result content",
                    "url": "Result URL"
                }
            ]
        }
    """
```

## Component API

### SearchBox

Renders the search input interface.

```python
def render_search_box() -> Optional[str]:
    """
    Returns:
        Optional[str]: The search query if submitted, None otherwise
    """
```

### ResultsDisplay

Displays search results or error messages.

```python
def render_results(results: Dict[str, Union[List[Dict], str]]) -> None:
    """
    Args:
        results: Dictionary containing either results list or error message
    """
```

## Configuration

### Config Class

Manages application configuration.

```python
@dataclass
class Config:
    """
    Attributes:
        OLLAMA_API_URL (str): URL for Ollama API
        AI_MODEL (str): Name of the AI model to use
        DEBUG (bool): Debug mode flag
        LOG_LEVEL (str): Logging level
    """
```

## Constants

### ModelStatus

Enum for model status values.

```python
class ModelStatus(str, Enum):
    READY = "ready"
    ERROR = "error"
    NOT_AVAILABLE = "not_available"
```

### SearchResultType

Enum for search result types.

```python
class SearchResultType(str, Enum):
    WEB = "web"
    LOCAL = "local"
    ERROR = "error"
```

## Usage Examples

### Basic Search Implementation

```python
from local_ai_search.services.ai_service import AIService
from local_ai_search.config import Config

# Initialize service
config = Config()
ai_service = AIService(config)

# Perform search
results = ai_service.perform_search("python programming")

# Handle results
if "error" in results:
    print(f"Error: {results['error']}")
else:
    for result in results["results"]:
        print(f"Title: {result['title']}")
        print(f"Content: {result['content']}")
        print(f"URL: {result['url']}")
```

### Component Usage

```python
import streamlit as st
from local_ai_search.components.search_box import render_search_box
from local_ai_search.components.results_display import render_results

# Render search box
query = render_search_box()

if query:
    # Perform search
    results = ai_service.perform_search(query)
    
    # Display results
    render_results(results)
```