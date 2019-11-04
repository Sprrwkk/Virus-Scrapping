import bs4
import urllib.request
import json

#webpage source
webpage = 'https://downloads.sophos.com/downloads/info/latest_IDE.xml'
sauce = urllib.request.urlopen(webpage).read()
soup = bs4.BeautifulSoup(sauce, 'xml')

#data mining
filename = [file.text for file in soup.find_all('name')]
filename = ''.join(filename)

filesize = [file_size.text for file_size in soup.find_all('size')]
filesize = ''.join(filesize)

datepub = [file_date.text[:10] for file_date in soup.find_all('published')]
datepub = ''.join(datepub)

#save data to list object
file_information = [filename, filesize, datepub]


def ide_sophos_main():
    """Function that write Sophos IDE definition to JSon file"""
    with open(f'{datepub}.json', 'w') as f_obj:
        for file_info in file_information:
            json.dump(file_info, f_obj)
            f_obj.write('\n')
        print("Saved!")

ide_sophos_main()




