# import http.client
# import urllib.parse
import os
import json
import requests
import csv


# Get the directory of the current module (newsapi.py)
module_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json relative to the module's directory
config_path = os.path.join(module_dir, '.', 'config.json')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)

API_KEY = config['worldNews_api_key']

def return_k_words(news_keywords):
    if len(news_keywords) < 1:
        return False
    else:
        return "-".join(news_keywords)

def fetch_news(keywords):
    news_keywords = return_k_words(keywords)
    print(news_keywords)
    # conn = http.client.HTTPConnection('api.worldnewsapi.com')

    url="https://api.worldnewsapi.com/search-news"

    params = {
        'api-key': API_KEY,
        'earliest-publish-date': '2023-06-21',
        'latest-publish-date': '2023-08-21',
        'text': news_keywords,
        'language': 'en',
        'number': 100,
        'offset': 300
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_data = response.json()

       
    else:
        print(f"Error: {response.status_code}")


    with open('news.json','w') as f:
        json.dump(json_data,f,indent=4)


    
# Extract relevant information
    articles = json_data.get('news', [])
    article_list = []

    for article in articles:
        title = article.get('title', '')
        url = article.get('url', '')
        publish_date = article.get('publish_date', '')

        # Append to the list
        article_list.append([title, url, publish_date])

    # Save to CSV file
    csv_filename = 'news_data3.csv'

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title', 'URL', 'Publish Date'])
        csv_writer.writerows(article_list)

    print(f'Data saved to {csv_filename}')


    return json_data

    

# Uncomment the following line to actually fetch news
fetch_news(['oppenheimer', 'christopher-nolan','universal-pictures','cillian-murphy'])
