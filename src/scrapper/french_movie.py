import requests
from config import APIKEY
import json, os

# https://www.omdbapi.com/
ENDPOINT = 'http://www.omdbapi.com/'
CACHE_FILE = 'french_movie.db' # Database to store the french Movie List

def check_omdb_api(title, year=None):
    # Build URL
    url = ENDPOINT + '?t=' + title + '&apikey=' + APIKEY
    if year:
        url += '&y=' + str(year)

    # Get Request to OMDB Api
    r = requests.get(url)
    data = r.json()

    # Check if it's a french movie
    if (data["Language"] == "French"):
        return True
    return False

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)

def is_french_film(title, year=None):
    cache = load_cache()

    # Check if the movie is already in the cache
    if title in cache:
        return cache[title]
    
    try:
        is_french = check_omdb_api(title, year)
    except Exception:
        print("Movie unknow")
        return None

    # Save the information
    cache[title] = is_french
    save_cache(cache)

    return is_french