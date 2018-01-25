import urllib.request
import json
from .models import Sources, Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']