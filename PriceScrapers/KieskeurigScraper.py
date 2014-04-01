from bs4 import BeautifulSoup
import requests

from PriceScrapers import priceToDB


json_file = 'output.json'

# List of products to be scraped
products = [
    'http://www.kieskeurig.nl/mobiel/gsm/samsung/galaxy-s4-i9505-zwart/prijzen/1174247',
    'http://www.kieskeurig.nl/mobiel/gsm/huawei/ascend-p6-zwart/prijzen/1343690',
    ]


itemList = []

with open(json_file, 'a', 1, encoding='utf8') as output_file:
    
    # Loop array
    for product in products:
        
        r=requests.get(product)
        pageHTML=r.text
        soup=BeautifulSoup("".join(pageHTML))
        sAll=soup.findAll("td", { "class" : "prijs" })

        
        # Scrape product name from title
        text = soup.title.text
        head, sep, tail = text.partition(' kopen?')


        prijsArr = [head]
              
        # Output all prices
        for price in sAll:
                for child in price:
                    p = child.string
                    prijs = p[19:]

                    # Convert strings to price only 
                    if prijs.find(',') > 0:
                        end = prijs.find(',')+3
                        prijsInt= prijs[:end]
                        
                        prijsArr.append(prijsInt)

        priceList = prijsArr[0:4]
        priceList.append('Kieskeurig')

        itemList.append(priceList)

    priceToDB.priceToDB(itemList)



                        


