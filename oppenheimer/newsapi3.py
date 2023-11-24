# import http.client
# import urllib.parse
import os
import json
import requests


# Get the directory of the current module (newsapi.py)
module_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json relative to the module's directory
config_path = os.path.join(module_dir, '.', 'config.json')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)

API_KEY = config['worldNews_api_key']

def return_k_words(news_keywords):
    if len(news_keywords) < 1 or news_keywords[0] == '' or not all(x.isalpha() for x in news_keywords):
        return False
    else:
        return "-".join(news_keywords)

def fetch_news(keywords):
    news_keywords = return_k_words(keywords)
    
    # conn = http.client.HTTPConnection('api.worldnewsapi.com')

    url="https://api.worldnewsapi.com/search-news"

    params = {
        'api-key': API_KEY,
        'earliest-publish-date': '2023-06-21',
        'latest-publish-date': '2023-08-21',
        'text': news_keywords,
        'language': 'en',
        'number': 100
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print(f"Error: {response.status_code}")

    

# Uncomment the following line to actually fetch news
# fetch_news(["oppenheimer","director"])
