# src/download_data.py

import os
from kaggle.api.kaggle_api_extended import KaggleApi
from src.config import KAGGLE_USERNAME, KAGGLE_KEY

def download_kaggle_dataset(dataset_path: str, output_dir: str = "data/"):
    # Set environment variables from config
    os.environ["KAGGLE_USERNAME"] = KAGGLE_USERNAME
    os.environ["KAGGLE_KEY"] = KAGGLE_KEY

    # Initialize and authenticate Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Download and unzip dataset
    api.dataset_download_files(dataset_path, path=output_dir, unzip=True)
