import selenium
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time

def linked(number):
    
    optionss = webdriver.FirefoxOptions()
    optionss.headless = True
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")

    browser = webdriver.Firefox(options=optionss)
    
    browser.get('https://www.linkedin.com/checkpoint/rp/request-password-reset')

    search = browser.find_element_by_css_selector('#username')
    search.send_keys(number , Keys.ENTER)

    time.sleep(20)
    
    if browser.current_url != 'https://www.linkedin.com/checkpoint/rp/request-password-reset':
	    return "A Linkedin account is associated with this number" 
    else:
	    return "There is No Linkedin account associated with this number"
