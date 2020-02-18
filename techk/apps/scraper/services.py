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



def get_urls_publicacion(url):
    '''
    Get all the page url with 20 books/page
    http://books.toscrape.com/catalogue/page-1.html  input 
    '''
    try:
        browser = get_content_bs4(url)
        libros_por_pagina = int(len(browser.select('.col-xs-6.col-sm-4.col-md-3.col-lg-3')))
        numero_publicaciones = int(browser.select('.form-horizontal strong')[0].get_text()) 
        total_paginas = math.ceil(numero_publicaciones/libros_por_pagina)
        url_category_base = 'http://books.toscrape.com/catalogue/page-1.html'
        url_paginas = [url_category_base.replace('page-1','page-'+str(pag)) 
                        for pag in range(1,total_paginas+1)]
    except Exception as e:
        print(e)
        url_paginas = []
    finally:
        return url_paginas        