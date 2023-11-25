from gnews import GNews
from argparse import ArgumentParser
import json
import csv

parser = ArgumentParser()
parser.add_argument('-k', '--keywords', required=True, help='Keywords to search, include quotation around multiple keywords')
parser.add_argument('-o', '--output',   required=True, help='Output file')
args = parser.parse_args()
keywords = args.keywords
output_filename = args.output

def googlenews():
    google_news = GNews()
    google_news.language = 'english'
    google_news.start_date = (2023, 6, 21)
    google_news.end_date = (2023, 8, 21)
    oppenheimer_news = google_news.get_news(keywords)
    
    # print(len(oppenheimer_news))
    # print(oppenheimer_news[0])
    # with open(output_filename, 'w') as file:
    #         json.dump(oppenheimer_news, file, indent=4)
    
    file = csv.writer(open(output_filename, 'w', encoding='utf-8_sig'))
    file.writerow(['Publish Date', 'Title', 'Description', 'Text', 'URL'])
    
    for i in range(len(oppenheimer_news)):
        article = google_news.get_full_article(oppenheimer_news[i]['url'])
        if article is None:
            continue
        file.writerow([article.publish_date, article.title, article.meta_description, article.text, article.url])
        
if __name__ == '__main__':
    googlenews()