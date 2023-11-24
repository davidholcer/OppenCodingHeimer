#newsapi2.py
import http.client, urllib.parse
import os
import json
import logging

# logger=logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)

# Get the directory of the current module (newsapi.py)
module_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json relative to the module's directory
config_path = os.path.join(module_dir, '.', 'config.json')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
API_KEY = config['api_key']

def return_k_words(news_keywords):
    if (len(news_keywords)<1 or news_keywords[0]=='' or not all(x.isalpha() for x in news_keywords) ):
        return False
    else:
        return " ".join(news_keywords);


def fetch_news(keywords):
    news_keywords=return_k_words(keywords)
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': API_KEY,
        'categories': 'general,entertainment',
        'sort': 'popularity',
        'date': '2023-06-21,2023-08-21',
        'keywords': news_keywords,
        'languages': 'en',
        'limit': 100
        })

    print(params)

#     if 'keywords' in params:
#         params['keywords'] = ','.join(params['keywords'].split(','))

    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    


    json_data = json.loads(data.decode('utf-8'))

    return(json_data)



# fetch_news("oppenheimer directors")