import os
import json
import unittest
from datetime import datetime,timedelta
from .. import newsapi
import pytz
# Construct the path to config.json relative to the module's directory
config_path = os.path.join(newsapi.module_dir, '.', 'config.json')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
API_KEY = config['api_key']

def parse_iso8601_time(time_string):
    try:
        # Remove the 'Z' character and split the date and time
        date_str, time_str = time_string.strip('Z').split('T')

        # Parse the date and time components
        date = datetime.strptime(date_str, '%Y-%m-%d')
        time = datetime.strptime(time_str, '%H:%M:%S')

        # Combine the date and time to create a datetime object
        datetime_object = datetime(
            date.year, date.month, date.day,
            time.hour, time.minute, time.second
        )

        return pytz.utc.localize(datetime_object)
    except ValueError:
        return None

def check_dates(articles,lookback_days):
    # return False
    current_date = datetime.now()
    new_date = (current_date - timedelta(days=lookback_days)).astimezone(pytz.utc)
    for a in articles:
        # print(str(a["publishedAt"]))
        good_time=parse_iso8601_time(a["publishedAt"])
        if good_time.date()<new_date.date():
            return False
    return True


class TestCase(unittest.TestCase):
    def test_keyword_empty(self):
        self.assertFalse(newsapi.fetch_latest_news(API_KEY,[""],5))

    def test_keyword_nonalpha(self):
        self.assertFalse(newsapi.fetch_latest_news(API_KEY,["hello8"],5))
    
    def test_lookback_days_works(self):
        self.assertTrue(check_dates(newsapi.fetch_latest_news(API_KEY,["youtube"],2),2) )

if __name__=="__main__":
    unittest.main()