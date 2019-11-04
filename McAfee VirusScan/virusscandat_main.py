from urllib.request import urlopen
import requests
from zipfile import ZipFile
import re

#str = 'avvdat-9425.zip'

soup = requests.get('http://update.nai.com/Products/CommonUpdater/')
soup_content = soup.text
print(soup_content)


x = re.search(r"\Aavvdat-", soup_content)
print(x.string)


#zipsource = 'http://update.nai.com/Products/CommonUpdater/' + x.string



#zipresp = urlopen(zipsource)

#tempzip = open(x.string, "wb")
#tempzip.write(zipresp.read())
#tempzip.close()