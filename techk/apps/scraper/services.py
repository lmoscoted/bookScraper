import concurrent.futures
import math
from bs4 import BeautifulSoup
import pandas as pd 
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry