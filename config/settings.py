"""
Centralized configuration loader for The Healer's Scribe.
Loads environment variables and provides safe access to secrets.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
    # Add more config as needed

settings = Settings()
