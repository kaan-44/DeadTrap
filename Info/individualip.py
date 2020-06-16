import requests
import socket
import json
import re

ipv4_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

ipv6_regex = re.compile(r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))')

lapi_key='e97dfc49e0a7a627d36d243dfdf3fc001afe28e6233e3a7d168cf172'

class bcolors:
    RED = '\033[31m'
    ENDC = '\033[0m'

def lookup_ip(ip_address):
    	response = requests.get(f'https://api.ipdata.co/{ip_address}?api-key={lapi_key}')
    	response_json = json.loads(response.text)
    	return f'''
    IP: {str(response_json['ip'])}
    ----------------
    IP LOCATION INFO
    City: {str(response_json['city'])}
    Region: {str(response_json['region'])}
    Region code: {str(response_json['region_code'])}
    Country: {str(response_json['country_name'])}
    Country code: {str(response_json['country_code'])}
    Flag: {str(response_json['emoji_flag'])}
    Continent: {str(response_json['continent_name'])}
    Continent code: {str(response_json['continent_code'])}
    Postal code: {str(response_json['postal'])}
    Latitude: {str(response_json['latitude'])}
    Longitude: {str(response_json['longitude'])}
    Calling code: {str(response_json['calling_code'])}
    Time zone: {str(response_json['time_zone']['name'])}
    Time zone current time: {str(response_json['time_zone']['current_time'])}
    Currency: {str(response_json['currency']['name'])}
    Currency code: {str(response_json['currency']['code'])}
    Currency symbol: {str(response_json['currency']['symbol'])}
    Language: {str(response_json['languages'][0]['name'])}
    Native language: {str(response_json['languages'][0]['native'])}
    BASIC INFO
    ----------------
    asn: {str(response_json['asn']['asn'])}
    Name: {str(response_json['asn']['name'])}
    Domain: {str(response_json['asn']['domain'])}
    Route: {str(response_json['asn']['route'])}
    Type: {str(response_json['asn']['type'])}
    EXTRA INFO
    ----------------
    TOR: {str(response_json['threat']['is_tor'])}
    Proxy: {str(response_json['threat']['is_proxy'])}
    Anonymous: {str(response_json['threat']['is_anonymous'])}
    Abuser: {str(response_json['threat']['is_known_abuser'])}
    Threat: {str(response_json['threat']['is_threat'])}
    Bogon: {str(response_json['threat']['is_bogon'])}'''

print(bcolors.RED + """ ___ ____  ____  _   _    _  _____ ____ _   _ _____ ____  
|_ _|  _ \/ ___|| \ | |  / \|_   _/ ___| | | | ____|  _ \ 
 | || |_) \___ \|  \| | / _ \ | || |   | |_| |  _| | |_) |
 | ||  __/ ___) | |\  |/ ___ \| || |___|  _  | |___|  _ < 
|___|_|   |____/|_| \_/_/   \_\_| \____|_| |_|_____|_| \_\
""" + bcolors.ENDC)

search = input("\nEnter the IP address : ")

try:
	ip_address = socket.gethostbyname(search)
	print(bcolors.RED + lookup_ip(ip_address) + bcolors.ENDC)

except socket.gaierror:
	print('There is no such an ip or domain')

except:
	print("Sorry the program has crashed")

