__author__ = 'Alexander'

from bs4 import BeautifulSoup
import json
import requests

r=requests.get('http://www.kieskeurig.nl/mobiel/gsm/apple/iphone-4s-8gb-zwart/prijzen/1568176')
pageHTML=r.text
soup=BeautifulSoup("".join(pageHTML))
sAll=soup.findAll("td", { "class" : "prijs" })


for price in sAll:
        for child in price:
            prijs = child.string
            print(prijs[19:])
    
