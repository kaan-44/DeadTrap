import urllib
import requests
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
            print(data)
            

parser = MyHTMLParser()

def fouroneone(query):
    
    URL = f'https://www.411.com/phone/{query.replace("+", "").replace("" , "-")}'
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
	    parser.feed(resp.content.decode("utf-8"))
	    return "Done"
    
    else:
	    return "No internet Connection"
 
