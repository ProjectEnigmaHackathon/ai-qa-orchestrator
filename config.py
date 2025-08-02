"""
Configuration management for AI QA Orchestration Framework
Handles environment variables and application settings
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for the AI QA Orchestration Framework"""
    
    # API Keys
    ANTHROPIC_API_KEY: Optional[str] = os.getenv('ANTHROPIC_API_KEY', 'demo-key-for-development')
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    
    # Application Ports
    REAL_APP_PORT: int = int(os.getenv('REAL_APP_PORT', '8501'))
    DEMO_APP_PORT: int = int(os.getenv('DEMO_APP_PORT', '8502'))
    
    # Application Settings
    DEBUG: bool = os.getenv('DEBUG', 'False').lower() == 'true'
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
    
    @classmethod
    def validate_keys(cls) -> bool:
        """Validate that required API keys are present"""
        if not cls.ANTHROPIC_API_KEY or cls.ANTHROPIC_API_KEY == 'demo-key-for-development':
            print("⚠️  Warning: ANTHROPIC_API_KEY not found or using demo key")
            print("   Create a .env file with your actual API key for full functionality")
            return False
        return True
    
    @classmethod
    def get_anthropic_key(cls) -> str:
        """Get Anthropic API key with fallback"""
        return cls.ANTHROPIC_API_KEY or 'demo-key-for-development'

# Create global config instance
config = Config()