__author__ = 'Alexander'
from bs4 import BeautifulSoup
import json
import requests

#mobile

#scrapes HTML from webpage
r=requests.get("http://tweakers.net/categorie/215/mobiele-telefoons/producten/")
pageHTML=r.text

#defines soup function
soup=BeautifulSoup(r.text)

#finds phone element on webpage
phones=soup.findAll('p', attrs= {'class': 'ellipsis'})


#amount of phones to include in list
x=5
#x is doubled due to website structure
z=int(x*2)

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
    