from urllib.request import urlopen
import requests
import re
import zipfile
import json

#website
website = 'https://downloadcenter.trendmicro.com/index.php?clk=tab_pattern&clkval=1&regs=NABU&lang_loc=1&fbclid=IwAR3x-dze8r1Yrc0E-B6ulT-4Vv9_wf7sbANeSrIkjfg5zGazLs6aLmfi7N8'

file_content = requests.get(website)
content = file_content.text

file_href = re.findall("lpt\d{3,4}\.zip", content)



def download_opr_zip_file():
    """Function that download a opr-zip file"""
    #get every file from files with re matching and download it
    for i in set(file_href):
        zipsource = 'http://www.trendmicro.com/ftp/products/aupattern/ent95/' + i
        zipresp = urlopen(zipsource)
        tempzip = open(i, "wb")
        tempzip.write(zipresp.read())
        tempzip.close()


def extract_opr_file():
    """Function that extract opr-zip file and save information about this file in .json"""
    x = set(file_href)
    for file in x:
        zip = zipfile.ZipFile(file)
        x = zip.getinfo('lpt$vpn.' + file.strip('lpt zip .'))

        with open(f"{file.strip('.zip')}.json", 'w') as f_obj:
            json.dump(str(x), f_obj)



download_opr_zip_file()
extract_opr_file()