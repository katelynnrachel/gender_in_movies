# src/config.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")
