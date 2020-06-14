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
	    if tag == 'strong':
		    self.countLanguages += 1
		    self.inLink = True
		    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "strong":
            self.inlink = False

    def handle_data(self, data):
        if self.lasttag == 'strong' and self.inLink and data.strip():
            print("Info : " + data)
            

parser = MyHTMLParser()

def risk(number):
    
    optionss = webdriver.FirefoxOptions()
    optionss.headless = True
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")

    browser = webdriver.Firefox(options=optionss)
    
    browser.get('https://spamcalls.net/en/')

    search = browser.find_element_by_css_selector('input.form-control:nth-child(1)')
    search.send_keys(number , Keys.ENTER)

    time.sleep(20)
    parser.feed(browser.page_source)
    return "No risk Detected"
    browser.quit()
