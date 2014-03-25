from bs4 import BeautifulSoup
import json
import requests

products = [
    'http://www.kieskeurig.nl/mobiel/gsm/samsung/galaxy-s4-i9505-zwart/prijzen/1174247',
    'http://www.kieskeurig.nl/mobiel/gsm/samsung/galaxy-s4-i9505-zwart/prijzen/1174247',
    ]

for product in products:
    
    r=requests.get(product)
    pageHTML=r.text
    soup=BeautifulSoup("".join(pageHTML))
    sAll=soup.findAll("td", { "class" : "prijs" })


    for price in sAll:
            for child in price:
                prijs = child.string
                print(prijs[19:])
    
