import concurrent.futures
import math

from bs4 import BeautifulSoup
import pandas as pd 
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


# The url to be scrapped
url = 'http://books.toscrape.com/catalogue/page-1.html'


def get_content_bs4(url):
    '''
    Get the soup from a given url
    '''
    try:
        # Get a resquest session in order to
        # handle retry for unsuccessful connections
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        page = session.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        return soup
    except Exception as e:
        print(e)
        return None 