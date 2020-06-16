import os, math, sys
from pathlib import Path

OS_bit = (round(math.log(sys.maxsize,2)+1))  

os.system("sudo apt install python3-pip")   
os.system("pip3 install -U selenium")
os.system("pip3 install python-dotenv")

print("\n \n {} \n \n".format(OS_bit))


os.system('firefox -v > tmp')                  
result   =  open('tmp', 'r').read()            
marker   = result.find('Firefox') + 8          
version  = result[marker:].splitlines()[0]     
a,b,c = version.split(".")                     
os.remove('tmp')                               

FirefoxVersion = int(a)
second = 0

if FirefoxVersion  < 53:

    first = 16
    second = 1
    OS_bit = 64

elif FirefoxVersion == 53 or FirefoxVersion == 54:

    first = 18

elif FirefoxVersion > 54:

    first = 26
    
geckodriver = Path("usr/local/bin/geckodriver")

if geckodriver.is_file():
    print("geckodriver is preinstalled")
else:
    print("Installing geckodriver")
    os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,OS_bit))
    os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
    os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
    os.system("chmod +x geckodriver")
    os.system("sudo mv geckodriver /usr/local/bin/")
