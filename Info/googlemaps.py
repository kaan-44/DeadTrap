import urllib
import requests
from bs4 import BeautifulSoup

def maps(location):
    URL = f"https://www.google.com/maps?q={location}"
    return URL
