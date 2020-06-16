import os
from os.path import join,dirname
from dotenv import load_dotenv
import selenium
import requests
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
import time
import sys
from html.parser import HTMLParser
import json
from SocialMedia.scrapefb import fb
from SocialMedia.scrapetwitter import twit
from SocialMedia.scrapelinkedin import linked
from Info.Spamcalls import risk
from Info.fouroneone import fouroneone
from Info.google import trace
from Style.banner import banner

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
api_key = os.getenv('NUMVERIFY_API_KEY')
print(api_key)
n = []

class colors:
    yellow =  '\033[1;33m'
    green =  '\033[1;32m'
    red =   '\033[1;31m'
    magenta = '\033[1;35m'
    darkwhite = '\033[0;37m'

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
        if tag == 'h1':
            for name, value in attrs:
                if name == 'class' and value == 'flex-1 text-xl text-fontPrimaryColor leading-tight':
                    self.countLanguages += 1
                    self.inLink = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "h1":
            self.inlink = False

    def handle_data(self, data):
        if self.lasttag == 'h1' and self.inLink and data.strip():
            print(colors.green + "Name : " + data + colors.green)
            
class HTML(HTMLParser):
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
                if name == 'class' and value == 'flex-1 h-16 leading-16 border-b border-borderColor truncate pr-4':
                    self.countLanguages += 1
                    self.inLink = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "div":
            self.inlink = False

    def handle_data(self, data):
	    if self.lasttag == 'div' and self.inLink and data.strip():
		    if "@" in data:
			    print(colors.magenta + "Email : " + data + colors.magenta)
		    else:
			    pass
		    
banner()
query = input(colors.green + "\n└──=>Enter the phone number (along with prefix) :")

line_1 = "\nRunning Scan..."

for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.1)

request = requests.get(f'http://apilayer.net/api/validate?access_key={api_key}&number={query}')
answer = json.loads(request.text) 

optionss = webdriver.FirefoxOptions()
optionss.headless = True
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")

browser = webdriver.Firefox(options=optionss)

browser.get(f"https://www.truecaller.com/search/{str(answer['country_code']).lower()}/{query.replace('+91', '')}")

parse = HTML()

parser = MyHTMLParser()

if browser.current_url != 'https://www.truecaller.com/auth/sign-in':
    print(colors.red+"\nInfo Scan\n"+colors.red)
    print(colors.red+"------------------------"+colors.red)
    parser.feed(browser.page_source)
    print(colors.green+f'''
Valid : {str(answer['valid'])}
Number: {str(answer['number'])}
Local Format: {str(answer['local_format'])}
International Format: {str(answer['international_format'])}
Country Prefix: {str(answer['country_prefix'])}
Country Code: {str(answer['country_code'])}
Country Name: {str(answer['country_name'])}
Location: {str(answer['location'])}
Carrier: {str(answer['carrier'])}
Line Type: {str(answer['line_type'])}'''+colors.green)
    
else:
    
    actionchains = ActionChains(browser)

    click = browser.find_element_by_xpath('/html/body/div/main/div/a[2]')

    actionchains.move_to_element(click).click().perform()

    time.sleep(20)
    email = browser.find_element_by_css_selector('#i0116')
    email.send_keys(os.getenv('EMAIL_ADDRESS'), Keys.ENTER)

    time.sleep(20)
    password = browser.find_element_by_css_selector('#i0118')
    password.send_keys(os.getenv('EMAIL_PASSWORD'), Keys.ENTER)
    
    time.sleep(30)
    print(colors.red+"\nInfo Scan\n"+colors.red)
    print(colors.red+"------------------------"+colors.red)
    parser.feed(browser.page_source)
    print(colors.green+f'''
Valid : {str(answer['valid'])}
Number: {str(answer['number'])}
Local Format: {str(answer['local_format'])}
International Format: {str(answer['international_format'])}
Country Prefix: {str(answer['country_prefix'])}
Country Code: {str(answer['country_code'])}
Country Name: {str(answer['country_name'])}
Location: {str(answer['location'])}
Carrier: {str(answer['carrier'])}
Line Type: {str(answer['line_type'])}'''+colors.green)
    
print("")
print(colors.magenta + "[*] Scanning Social Media Footprints" + colors.magenta)
print("-------------------------------------")
print("")
print(fb(query))
print("")
print(twit(query))
print("")
print(linked(query))
print("")
parse.feed(browser.page_source)
print("")

print(colors.darkwhite + "Spamcalls.net Search" + colors.darkwhite)
print("------------")
print("")
print(risk(query))

print(colors.darkwhite + "\n411.com search" + colors.darkwhite)
print("------------")
print("")
print(fouroneone(query))

print(colors.red + "\nGoogle Exception Results")
print(colors.red + "-------------")
print("")
print(trace(query))
print("")
browser.quit()
