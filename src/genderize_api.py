# CALLING GENDERIZE API

import requests
import pickle
import os
from src.config import GENDERIZE_API_KEY

# Using a caching method to save results of Genderize API so that the API doesnt have to be run more than once
def get_gender_mapping(names_list, save_path="data/gender_mapping.pkl"):
   
    # If the mapping is already saved then load it,  otherwise, make API calls
    if os.path.exists(save_path):
        with open(save_path, "rb") as f:
            gender_dict = pickle.load(f)
        print("Loaded cached gender mapping.")
        return gender_dict
   
    gender_dict = {}
    for name in names_list:
        if name:
            url = f"https://api.genderize.io/?name={name}&apikey={GENDERIZE_API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                gender = data.get('gender')
                gender_dict[name] = gender
            else:
                gender_dict[name] = None

    # Save results to pickle file
    with open(save_path, "wb") as f:
        pickle.dump(gender_dict, f)

    print("Saved new gender mapping to file.")
    return gender_dict

# Calling API
def call_genderize_api(name):
 
    url = f"https://api.genderize.io/?name={name}&apikey={GENDERIZE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('gender')
    else:
        return None
