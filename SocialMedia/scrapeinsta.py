import selenium
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time
import sys

def insta(number):
    
    optionss = webdriver.FirefoxOptions()
    optionss.headless = True
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")

    browser = webdriver.Firefox(options=optionss)
    
    browser.get('https://www.instagram.com/accounts/password/reset/')

    search = browser.find_element_by_css_selector('#feff36e4590dbc')
    search.send_keys(number , Keys.ENTER)

    time.sleep(30)
    
    if browser.current_url != 'https://www.instagram.com/accounts/password/reset/':
	    return "An Instagram account is associated with this number" 
	    browser.quit()
    else:
	    return "There is No Instagram account associated with this number"
	    browser.quit()
