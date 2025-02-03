import json
import pandas as pd
from google_play_scraper import app

result = app(
    'com.youtube',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

print(json.dumps(result, indent=4))