__author__ = 'Wesley'
from bs4 import BeautifulSoup
import json
import requests

#mobile

#scrapes HTML from webpage
r=requests.get("http://www.amazon.co.uk/s/ref=sr_il_ti_electronics?rh=n%3A560798%2Cn%3A%21560800%2Cn%3A1340509031%2Cn%3A356496011%2Cp_36%3A10000-90000&bbn=356496011&ie=UTF8&qid=1396351847&lo=electronics")
pageHTML=r.text

#defines soup function
soup=BeautifulSoup(r.text)

#finds phone element on webpage
phones=soup.findAll('div', attrs= {'class': 'ilt2'})

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
    