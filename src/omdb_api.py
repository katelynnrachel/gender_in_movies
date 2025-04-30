# CALLING OMDB API
import requests
import pickle 
import os
from src.config import OMDB_API_KEY

# Using a caching method to save results of OMDB API so that the API doesnt have to be run more than once
def get_movie_info(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_all_movie_data(titles, save_path="data/omdb_data.pkl"):
    # If the mapping is already saved then load it,  otherwise, make API calls
    if os.path.exists(save_path):
        with open(save_path, "rb") as f:
            movie_data = pickle.load(f)
        print("Loaded cached OMDb movie data.")
        return movie_data

    movie_data = {}
    for title in titles:
        if title:
            data = get_movie_info(title)
            movie_data[title] = data

    with open(save_path, "wb") as f:
        pickle.dump(movie_data, f)

    return movie_data


# RETREIVING ROTTEN TOMATOES SCORE AND ADDING TO DF 
import pandas as pd

def add_rotten_tomatoes_score(df, omdb_data):
    normalized_omdb_data = {title.strip().lower(): data for title, data in omdb_data.items()}

    rt_scores = []

    for title in df['Series_Title']:
        normalized_title = title.strip().lower()
        movie_data = normalized_omdb_data.get(normalized_title)

        rt_score = None

        if movie_data and 'Ratings' in movie_data:
            for rating_source in movie_data['Ratings']:
                if rating_source['Source'] == 'Rotten Tomatoes':
                    rt_score = rating_source['Value']
                    break

        rt_scores.append(rt_score)

    # Add Rotten Tomatoes Score to DataFrame
    df['Rotten_Tomatoes_Score'] = rt_scores

    # Clean Rotten Tomatoes Score (remove '%', convert to float)
    df['Rotten_Tomatoes_Score'] = df['Rotten_Tomatoes_Score'].str.replace('%', '')
    df['Rotten_Tomatoes_Score'] = pd.to_numeric(df['Rotten_Tomatoes_Score'], errors='coerce')

    # Drop movies where Rotten Tomatoes Score is missing
    df = df.dropna(subset=['Rotten_Tomatoes_Score'])

    return df
