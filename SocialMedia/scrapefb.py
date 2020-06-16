import selenium
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.dataArray = []
        self.countLanguages = 0
        self.lasttag = None
        self.lastname = None
        self.lastvalue = None

    def handle_starttag(self, tag, attrs):
        self.inLink = False
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'fsl fwb fcb':
                    self.countLanguages += 1
                    self.inLink = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "div":
            self.inlink = False

    def handle_data(self, data):
	    if self.lasttag == 'div' and self.inLink and data.strip():
		    print("Facebook Name / Number : " + data)
            
            
parser = MyHTMLParser()

def fb(number):
    
    optionss = webdriver.FirefoxOptions()
    optionss.headless = True
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")

    browser = webdriver.Firefox(options=optionss)
    
    browser.get('https://www.facebook.com/login/identify/?ctx=recover')

    search = browser.find_element_by_css_selector('#identify_email')
    search.send_keys(number , Keys.ENTER)

    time.sleep(20)
    
    if browser.current_url != 'https://www.facebook.com/login/identify/?ctx=recover':
	    parser.feed(browser.page_source)
	    return f'A Facebook account is associated with this number'
	    browser.quit()
	    
    else:
	    return "There is No Facebook account associated with this number"
	    browser.quit()
	    
    


