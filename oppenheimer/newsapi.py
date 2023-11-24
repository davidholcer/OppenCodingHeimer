import os
import json
import requests
import logging
import pytz
from datetime import datetime,timedelta

logger=logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)

# Get the directory of the current module (newsapi.py)
module_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json relative to the module's directory
config_path = os.path.join(module_dir, '.', 'config.json')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
API_KEY = config['api_key']

# NEWS_QUERY_STRING_TEMPLATE="https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy=popularity&apiKey={}"
NEWS_QUERY_STRING_TEMPLATE="http://api.mediastack.com/v1/news?access_key={}&keywords={}&date={},{}&languages=en&limit=100?sort=popularity&categories=general,entertainment"

OUTPUT_PATH=os.path.join(module_dir,'.',"output.json")

def return_k_words(news_keywords):
    if (len(news_keywords)<1 or news_keywords[0]=='' or not all(x.isalpha() for x in news_keywords) ):
        return False
    else:
        return ", ".join(news_keywords);

def fetch_news(news_keywords, from_date, to_date,api_key=API_KEY):
    # Get the current date
    # current_date = datetime.now()
    # new_date = (current_date - timedelta(days=lookback_days)).astimezone(pytz.utc)
    # Format the new date if needed
    # f_date = new_date.strftime("%Y-%m-%d")

    #join the keywords by AND to pass them into the api
    k_words=return_k_words(news_keywords)

    print(k_words)

    if (not (k_words)):
        return False

    query_string=NEWS_QUERY_STRING_TEMPLATE.format(api_key,k_words,from_date,to_date)

    logger.debug("Fetching news from {}".format(query_string))

    response=requests.get(query_string)
    if response.status_code !=200:
        raise Exception("Unable to fetch news for query {}".format(query_string))
    
    data=response.json()
    # print (data)
    return data

if __name__ == "__main__":
    fetch_news(API_KEY,["oppenheimer","director"],"2023-07-21","2023-08-21")