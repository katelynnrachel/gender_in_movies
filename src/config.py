from dotenv import load_dotenv
import os

load_dotenv()

KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")
GENDERIZE_API_KEY = os.getenv("GENDERIZE_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
