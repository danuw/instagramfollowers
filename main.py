from bs4 import BeautifulSoup
import requests
from settings import *

def main():
    url = 'http://www.instagram.com/'+instaaccount
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")

    title = soup.title.string
    #print ('TITLE IS :', title)

    meta = soup.find_all('meta')

    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            # print ('NAME    :',tag.attrs['name'].lower())
            nb = tag.attrs['content'].split(" ")[0]
            #print ('CONTENT :',tag.attrs['content'])
            print(nb)

if __name__ == '__main__':
    main()