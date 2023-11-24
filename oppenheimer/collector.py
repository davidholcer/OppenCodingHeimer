from argparse import ArgumentParser
from newsapi import *
import json
import os

parser = ArgumentParser()
parser.add_argument(
    "-keywords", "--keywords", required=True, help="the keywords to search"
)
parser.add_argument(
    "-f", "--from_date", required=True, help="the date to start at"
)
parser.add_argument(
    "-t", "--to_date", required=True, help="the date to go up to"
)
parser.add_argument(
    "-o", "--output", required=True, help="the output json file name"
)

args = parser.parse_args()
print (args)

def fix_path(file_path):
    if not os.path.isabs(file_path):
        # If it's a relative path, convert it to an absolute path
        module_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(module_dir, '', file_path)
    return file_path

# inputPath=fix_path(args.input)
outputPath=fix_path(args.output)
print(outputPath)

articles=fetch_news([args.keywords],args.from_date,args.to_date)

outputF=outputPath
with open(outputF,'w') as f:
    json.dump(articles,f,indent=4)