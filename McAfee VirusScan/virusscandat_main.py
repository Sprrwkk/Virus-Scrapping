from urllib.request import urlopen
import requests
import re
import zipfile
import json


#main website url
soup = requests.get('http://update.nai.com/Products/CommonUpdater/')
#create soup_content object to get text format
soup_content = soup.text
#create list with all matching queries (avvdat-~) using re library
files = re.findall("avvdat-\d{4,6}\.zip", soup_content)

def main_mcafee():
    """Main app function"""
    """Before start, function checks if the file already exists in the txt file"""
    empty_elements = []
    with open('avvdat_all_files.txt', 'r+') as f_obj:
        s = f_obj.readlines()
        for i in s:
            empty_elements.append(i.strip("\n"))

        for i in set(files):
            if i not in empty_elements:
               f_obj.write(i + "\n")
               download_zip_file()
               extract_file()
            else:
                print("Plik został już pobrany!")
                break




def download_zip_file():
    """Function that download a avvdat-zip file"""
    # get every file from files with re matching - save filename in txt and download it
    for i in set(files):
        zipsource = 'http://update.nai.com/Products/CommonUpdater/' + i
        zipresp = urlopen(zipsource)
        tempzip = open(i, "wb")
        tempzip.write(zipresp.read())
        tempzip.close()


def extract_file():
    """Function that extract avvdat-zip file and save information about this file in .json"""
#extract files and save all information in json file
    x = set(files)
    for file in x:
        #print(file)
        zip = zipfile.ZipFile(file)
        x = zip.getinfo("avvscan.dat")
        #print("------")
        with open(f"{file[:11]}.json", 'w') as f_obj:
            json.dump(str(x), f_obj)




main_mcafee()
# download_zip_file()
# extract_file()