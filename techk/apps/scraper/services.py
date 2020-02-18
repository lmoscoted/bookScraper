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


def get_categories(url):
    """ Get all categories both id and names  """
    soup= get_content_bs4(url)
    categories_soup = soup.select('ul.nav.nav-list ul li a')
    categories_list = []
    cat_dict = {}
    for c in categories_soup:
        url_category = c['href']
        category_id = get_category_id(url_category)
        category_name = c.get_text(strip=True)
        cat_dict = {'id':category_id ,'name': category_name}
        categories_list.append(cat_dict)
    return categories_list


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


def get_category_id(url_category):
    """ Get the category id from the url category """

    category_part = url_category.split('/')[-2]
    category_id = int(category_part.split('_')[-1]) -1
    return category_id


def get_book_details(url_book,url_base_catalogue):
    '''
    Get the description, upc, stock, category_id
    from the given book's url.
    '''
    book_detail_soup = get_content_bs4(url_book)
    book_details= []
    if book_detail_soup:
        description = book_detail_soup.select('.product_page p')[3].get_text(strip=True)
        stock_ = book_detail_soup.select('.product_page p')[1].get_text()
        stock = int(stock_.strip().split(' ')[2].replace('(',''))
        upc = get_upc(book_detail_soup)
        url_category_ = book_detail_soup.select('.breadcrumb a')[2]['href']
        url_category =  url_category_.replace('../',url_base_catalogue)
        category_id = get_category_id(url_category)
        #return category_id
        #stock = book_detail_soup.select('.')

        book_details = [description,stock,upc,category_id]#[description,upc,stock,category_id]
                        
    return book_details

def get_upc(book_detail_soup):
    """ Get the book's upc from the book detail soup """
    upc = ''
    book_table = book_detail_soup.find('table', { 'class' : 'table table-striped' })
    trs = book_table.find_all('tr')
    #return trs
    for tr in trs:
        if tr.find('th').get_text(strip=True) == 'UPC':
            upc = tr.find('td').get_text(strip=True)
    return upc        