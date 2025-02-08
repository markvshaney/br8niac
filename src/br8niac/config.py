"""Configuration management for the application."""

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    """Application configuration."""
    
    OLLAMA_API_URL: str = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api")
    AI_MODEL: str = os.getenv("AI_MODEL", "mistral")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        return cls()