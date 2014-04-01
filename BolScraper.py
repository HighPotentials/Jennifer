__author__ = 'Wesley'
from bs4 import BeautifulSoup
import json
import requests

#mobile

#scrapes HTML from webpage
r=requests.get("http://www.bol.com/nl/l/elektronica/bestverkochte-smartphones/N/4004/lijstid/22300019/index.html?promo=smartphones_303_HS-populairste-smartphones-131016-MM_B4_De%20populairste%20smartphones__")
pageHTML=r.text

#defines soup function
soup=BeautifulSoup(r.text)

#finds phone element on webpage
phones=soup.findAll('div', attrs= {'class': 'product_line'})


#amount of phones to include in list
z=5

#creates top x list of phones
def toplst_phones():
    #loops through list of phones
    for phone in phones[0:z]:
        #finds <a> elements
        ps = phone.findAll('a')
        #loops through <a> elements found in phone element
        for link in ps:
            #ensures that 'none' titles are not included
            if link.get('title')==None:
                break
            else:
                print(link.get('title'))

#calls function
toplst_phones()
    