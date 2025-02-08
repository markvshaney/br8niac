"""Application-wide constants."""

from enum import Enum

class ModelStatus(str, Enum):
    """Status of the AI model."""
    
    READY = "ready"
    ERROR = "error"
    NOT_AVAILABLE = "not_available"

class SearchResultType(str, Enum):
    """Types of search results."""
    
    WEB = "web"
    LOCAL = "local"
    ERROR = "error"

# API endpoints
OLLAMA_GENERATE_ENDPOINT = "/generate"
OLLAMA_TAGS_ENDPOINT = "/tags"

# UI Constants
MAX_SEARCH_HISTORY = 5
DEFAULT_PAGE_TITLE = "Local AI Search"
DEFAULT_PAGE_ICON = "🔍"